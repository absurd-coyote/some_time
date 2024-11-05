import pytest

from unittest.mock import Mock

from some_time.inputs.web_trigger_adapter import WebTriggerAdapter

@pytest.mark.parametrize("event_id,expected", [
    ("add-15", 15),
    ("add-30", 30),
    ("add-60", 60),
    ])
def test_add_time_on_known_event_call__add_time_with_expected_parameter(time_counter, event_id, expected):
    # Given
    web_trigger = WebTriggerAdapter()
    web_trigger.init_time_counter(time_counter)
    event = Mock()
    event.target.id = event_id

    # When
    web_trigger.add_time(event)

    # Then
    time_counter.add_time.assert_called_with(expected)

@pytest.mark.parametrize("event_id,expected", [
    ("remove-15", 15),
    ("remove-30", 30),
    ("remove-60", 60),
    ])
def test_remove_time_on_known_event_call__remove_time_with_expected_parameter(time_counter, event_id, expected):
    # Given
    web_trigger = WebTriggerAdapter()
    web_trigger.init_time_counter(time_counter)
    event = Mock()
    event.target.id = event_id

    # When
    web_trigger.remove_time(event)

    # Then
    time_counter.remove_time.assert_called_with(expected)

