
import operations

# car = "moving", "stopped"
# light = "red", "yellow", "green"
# return = "move", "stop"

def test_light_choice_moving_red():
    assert operations.traffic_light_choice("moving", "red") == "stop"

def test_light_choice_moving_yellow():
    assert operations.traffic_light_choice("moving", "yellow") == "stop"
    
def test_light_choice_moving_green():
    assert operations.traffic_light_choice("moving", "green") == "go"

def test_light_choice_stopped_red():
    assert operations.traffic_light_choice("stopped", "red") == "stop"

def test_light_choice_stopped_yellow():
    assert operations.traffic_light_choice("stopped", "yellow") == "stop"
    
def test_light_choice_stopped_green():
    assert operations.traffic_light_choice("stopped", "green") == "go"

def test_multiple_at_once():        # This method is not advised
    assert operations.traffic_light_choice("stopped", "yellow") == "stop"
    assert operations.traffic_light_choice("stopped", "green") == "go"
    assert operations.traffic_light_choice("stopped", "green") == "break me"
