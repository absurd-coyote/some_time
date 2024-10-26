import datetime
import json
import pytest
import time

from some_time.domain.time_counter import TimeCounter
from tests.unit.tools import PeriodicRunner

def test_init_default_as_expected(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = False
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)

    # When
    time_counter.init()

    # Then
    assert time_counter.counter == datetime.timedelta()
    assert time_counter.counter_running == False
    assert time_counter.start_count == 0

def test_init_get_values_from_memory_when_present(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = True
    expected_counter = datetime.timedelta(seconds=10)
    expected_running = True
    expected_start_count = datetime.datetime.now()
    input_memory.load_values.return_value = {
        "counter": expected_counter.total_seconds(),
        "counter_running": expected_running,
        "start_count": expected_start_count.isoformat(),

        }
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)

    # When
    time_counter.init()

    # Then
    assert time_counter.counter == expected_counter
    assert time_counter.counter_running == expected_running
    assert time_counter.start_count == expected_start_count

def test_update_time_when_counter_off_does_not_increase_time(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = False
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        time.sleep(2)

    # Then
    assert time_counter.counter.total_seconds() == 0
    assert time_counter.counter_running == False

def test_update_time_when_started_counts_time(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = False
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        time_counter.start()
        time.sleep(2)

    # Then
    assert time_counter.counter.total_seconds() == pytest.approx(2, abs=1e-2)
    assert time_counter.counter_running == True

def test_update_time_from_previously_stopped_adds_to_it(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = True
    input_memory.load_values.return_value = {
        "counter": 10,
        "counter_running": False,
        "start_count": datetime.datetime.now().isoformat(),

        }
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        time_counter.start()
        time.sleep(2)

    # Then
    assert time_counter.counter.total_seconds() == pytest.approx(12, abs=1e-2)
    assert time_counter.counter_running == True

def test_update_time_from_previously_running_catch_up_lost_time(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = True
    input_memory.load_values.return_value = {
        "counter": 10,
        "counter_running": True,
        "start_count": datetime.datetime.now().isoformat(),

        }

    # When
    time.sleep(2)  # loss of time
    # Then load again the counter
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()
    # Run the counter for some time
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        time.sleep(2)

    # Then
    # expect to get "initial counter" + "lost time" + "running time"
    assert time_counter.counter.total_seconds() == pytest.approx(14, abs=1e-1)
    assert time_counter.counter_running == True

def test_add_time_on_stopped_counter_increase_counter(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = False
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    time_counter.add_time(15)

    # Then
    assert time_counter.counter.total_seconds() == 15*60
    assert time_counter.counter_running == False

def test_remove_time_on_stopped_counter_decrease_counter(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = False
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    time_counter.remove_time(15)

    # Then
    assert time_counter.counter.total_seconds() == -15*60
    assert time_counter.counter_running == False

def test_add_time_on_running_counter_combines_with_count(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = True
    input_memory.load_values.return_value = {
        "counter": 10,
        "counter_running": True,
        "start_count": datetime.datetime.now().isoformat(),

        }
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        time_counter.add_time(15)
        time.sleep(2)

    # Then
    # expect to get "initial counter" + "running time" + "add time"
    assert time_counter.counter.total_seconds() == pytest.approx(12 + (15*60), abs=1e-1)
    assert time_counter.counter_running == True

def test_remove_time_on_running_counter_combines_with_count(input_trigger, input_memory, output_display, output_memory):
    # Given
    input_memory.available.return_value = True
    input_memory.load_values.return_value = {
        "counter": 10,
        "counter_running": True,
        "start_count": datetime.datetime.now().isoformat(),

        }
    time_counter = TimeCounter(input_trigger, input_memory, output_display, output_memory)
    time_counter.init()

    # When
    with PeriodicRunner(target=time_counter.update_time, period=0.001):
        time_counter.remove_time(15)
        time.sleep(2)

    # Then
    # expect to get "initial counter" + "running time" + "add time"
    assert time_counter.counter.total_seconds() == pytest.approx(12 - (15*60), abs=1e-1)
    assert time_counter.counter_running == True
