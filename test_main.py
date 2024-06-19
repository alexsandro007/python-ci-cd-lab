import pytest
from main import WatchFactory

def test_create_smart_watch():
    watch = WatchFactory.create_watch("smart")
    assert watch.display_time() == "Displaying time on a smart watch with additional features"

def test_create_analog_watch():
    watch = WatchFactory.create_watch("analog")
    assert watch.display_time() == "Displaying time on an analog watch"

def test_create_watch_invalid():
    with pytest.raises(ValueError):
        WatchFactory.create_watch("digital")
