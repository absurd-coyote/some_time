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

def test_start_from_init_default_count_time(input_trigger, input_memory, output_display, output_memory):
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
    # assert that the start count is close to now
    start_count_diff = time_counter.start_count - datetime.datetime.now()
    assert start_count_diff.total_seconds() == pytest.approx(0, abs=1e-2)
