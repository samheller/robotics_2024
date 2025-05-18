import importlib
import sys
import unittest
from types import ModuleType

import tests.fake_vex as fake_vex

# Insert fake vex module so imports succeed
sys.modules['vex'] = fake_vex

from standardized_code import state_machine


def _run_with_config(config: ModuleType, iterations: int = 5) -> None:
    """Run the state machine for a few iterations using the given config."""
    fake_vex.wait_counter = 0
    fake_vex.wait_max = iterations

    controller = config.controller
    # Press B once to switch out of manual mode
    controller.buttonB.sequence = [True, False]
    if hasattr(controller, 'buttonA'):
        controller.buttonA.sequence = [False] * iterations
    if hasattr(controller, 'buttonR1'):
        controller.buttonR1.sequence = [False] * iterations
    if hasattr(controller, 'buttonR2'):
        controller.buttonR2.sequence = [False] * iterations

    distance = getattr(config, 'distance_sensor', getattr(config, 'front_distance', None))
    if distance is not None:
        distance.detected = True
        distance.distance_value = 100

    optical = getattr(config, 'optical_sensor', None)
    if optical is not None:
        optical.hue_value = 0

    try:
        state_machine.run_state_machine(
            config.brain,
            controller,
            config.drive_train,
            config.left_drive,
            config.right_drive,
            getattr(config, 'arm_drive', None),
            distance,
            optical,
        )
    except StopIteration:
        # Expected exit after wait_max iterations
        pass


class StateMachineConfigTests(unittest.TestCase):
    def test_robot_team_iis(self) -> None:
        config = importlib.import_module('standardized_code.robot_team_iis')
        _run_with_config(config)

    def test_diddy(self) -> None:
        config = importlib.import_module('standardized_code.diddy_standard')
        _run_with_config(config)

    def test_team4(self) -> None:
        config = importlib.import_module('standardized_code.team4_standard')
        _run_with_config(config)

    def test_woody(self) -> None:
        config = importlib.import_module('standardized_code.woody_standard')
        _run_with_config(config)


if __name__ == '__main__':
    unittest.main()
