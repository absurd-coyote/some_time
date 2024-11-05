import pytest
import time
from unittest.mock import call, Mock

from pyscript import display

from some_time.domain.time_counter import TimeCounter
from some_time.inputs.cookie_memory_adapter import CookieMemoryAdapter as InputCookie
from some_time.inputs.web_trigger_adapter import WebTriggerAdapter
from some_time.outputs.cookie_memory_adapter import CookieMemoryAdapter as OutputCookie
from some_time.outputs.web_display_adapter import WebDisplayAdapter
from tests.unit.tools import PeriodicRunner

def test_basic_init_when_do_not_start_and_empty_memory(store):
    # Given
    store.__contains__.return_value = False

    # When
    input_cookie = InputCookie(store)
    web_trigger = WebTriggerAdapter()
    output_cookie = OutputCookie(store)
    web_display = WebDisplayAdapter()

    time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

    time_counter.init()
    input_cookie.init_time_counter(time_counter)
    web_trigger.init_time_counter(time_counter)
    output_cookie.init_time_counter(time_counter)
    web_display.init_time_counter(time_counter)

    # Then
    assert len(display.call_args_list) == 0
    assert time_counter.counter.total_seconds() == 0
    assert time_counter.counter_running == False

def test_display_expected_and_store_expected_when_run_from_empty_memory(store):
    # Given
    store.__contains__.return_value = False

    input_cookie = InputCookie(store)
    web_trigger = WebTriggerAdapter()
    output_cookie = OutputCookie(store)
    web_display = WebDisplayAdapter()

    time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

    time_counter.init()
    input_cookie.init_time_counter(time_counter)
    web_trigger.init_time_counter(time_counter)
    output_cookie.init_time_counter(time_counter)
    web_display.init_time_counter(time_counter)

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        web_trigger.start()
        time.sleep(2)
        web_trigger.stop()

    # Then
    display.assert_called()
    assert display.call_args_list[-1] == call(str(time_counter.counter), target='time', append=False)
    assert time_counter.counter.total_seconds() == pytest.approx(2, abs=1e-2)
    assert time_counter.counter_running == False

@pytest.mark.parametrize("event_id,minute_value", [
    ("add-15", 15),
    ("add-30", 30),
    ("add-60", 60),
    ])
def test_display_expected_and_store_expected_when_add_while_running(store, event_id, minute_value):
    # Given
    store.__contains__.return_value = False

    input_cookie = InputCookie(store)
    web_trigger = WebTriggerAdapter()
    output_cookie = OutputCookie(store)
    web_display = WebDisplayAdapter()

    time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

    time_counter.init()
    input_cookie.init_time_counter(time_counter)
    web_trigger.init_time_counter(time_counter)
    output_cookie.init_time_counter(time_counter)
    web_display.init_time_counter(time_counter)
    event = Mock()
    event.target.id = event_id

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        web_trigger.start()
        time.sleep(1)
        web_trigger.add_time(event)
        time.sleep(1)
        web_trigger.stop()

    # Then
    display.assert_called()
    assert display.call_args_list[-1] == call(str(time_counter.counter), target='time', append=False)
    assert time_counter.counter.total_seconds() == pytest.approx(minute_value*60 + 2, abs=1e-2)
    assert time_counter.counter_running == False

@pytest.mark.parametrize("event_id,minute_value", [
    ("remove-15", -15),
    ("remove-30", -30),
    ("remove-60", -60),
    ])
def test_display_expected_and_store_expected_when_remove_while_running(store, event_id, minute_value):
    # Given
    store.__contains__.return_value = False

    input_cookie = InputCookie(store)
    web_trigger = WebTriggerAdapter()
    output_cookie = OutputCookie(store)
    web_display = WebDisplayAdapter()

    time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

    time_counter.init()
    input_cookie.init_time_counter(time_counter)
    web_trigger.init_time_counter(time_counter)
    output_cookie.init_time_counter(time_counter)
    web_display.init_time_counter(time_counter)
    event = Mock()
    event.target.id = event_id

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        web_trigger.start()
        time.sleep(1)
        web_trigger.remove_time(event)
        time.sleep(1)
        web_trigger.stop()

    # Then
    display.assert_called()
    assert display.call_args_list[-1] == call(str(time_counter.counter), target='time', append=False)
    assert time_counter.counter.total_seconds() == pytest.approx(minute_value*60 + 2, abs=1e-2)
    assert time_counter.counter_running == False

@pytest.mark.parametrize("event_id,minute_value", [
    ("add-15", 15),
    ("add-30", 30),
    ("add-60", 60),
    ])
def test_display_expected_and_store_expected_when_add_while_stopped(store, event_id, minute_value):
    # Given
    store.__contains__.return_value = False

    input_cookie = InputCookie(store)
    web_trigger = WebTriggerAdapter()
    output_cookie = OutputCookie(store)
    web_display = WebDisplayAdapter()

    time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

    time_counter.init()
    input_cookie.init_time_counter(time_counter)
    web_trigger.init_time_counter(time_counter)
    output_cookie.init_time_counter(time_counter)
    web_display.init_time_counter(time_counter)
    event = Mock()
    event.target.id = event_id

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        web_trigger.start()
        time.sleep(1)
        web_trigger.stop()
        web_trigger.add_time(event)
        time.sleep(0.01)  # wait a bit for another call to display

    # Then
    display.assert_called()
    assert display.call_args_list[-1] == call(str(time_counter.counter), target='time', append=False)
    assert time_counter.counter.total_seconds() == pytest.approx(minute_value*60 + 1, abs=1e-1)
    assert time_counter.counter_running == False

@pytest.mark.parametrize("event_id,minute_value", [
    ("remove-15", -15),
    ("remove-30", -30),
    ("remove-60", -60),
    ])
def test_display_expected_and_store_expected_when_remove_while_running(store, event_id, minute_value):
    # Given
    store.__contains__.return_value = False

    input_cookie = InputCookie(store)
    web_trigger = WebTriggerAdapter()
    output_cookie = OutputCookie(store)
    web_display = WebDisplayAdapter()

    time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

    time_counter.init()
    input_cookie.init_time_counter(time_counter)
    web_trigger.init_time_counter(time_counter)
    output_cookie.init_time_counter(time_counter)
    web_display.init_time_counter(time_counter)
    event = Mock()
    event.target.id = event_id

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        web_trigger.start()
        time.sleep(1)
        web_trigger.stop()
        web_trigger.remove_time(event)
        time.sleep(0.01)  # wait a bit for another call to display

    # Then
    display.assert_called()
    assert display.call_args_list[-1] == call(str(time_counter.counter), target='time', append=False)
    assert time_counter.counter.total_seconds() == pytest.approx(minute_value*60 + 1, abs=1e-1)
    assert time_counter.counter_running == False
