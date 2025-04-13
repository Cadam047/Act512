import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from smells2 import HumanNose, RobotNose  # updated import

ROSE = "rose"
DAISY = "daisy"
TULIP = "tulip"

def test_human_nose_can_smell():
    n = HumanNose()
    n.smell(ROSE)
    assert ROSE in n.get_smelled_smells()

def test_robot_nose_can_smell():
    n = RobotNose()
    n.smell(ROSE)
    assert ROSE in n.get_smelled_smells()

def test_human_nose_has_allergies():
    n = HumanNose([ROSE])

    # Can smell non-allergy odor
    n.smell(TULIP)
    assert TULIP in n.get_smelled_smells()

    # Tries to smell an allergy, immune response activates
    n.smell(ROSE)
    assert ROSE not in n.get_smelled_smells()

    # Immune response blocks further smelling
    with pytest.raises(RuntimeError):
        n.smell(DAISY)

    # Reset
    n.rest()

    # Now can smell again
    n.smell(DAISY)
    assert set([DAISY, TULIP]) == n.get_smelled_smells()

def test_robot_nose_has_air_capacity():
    n = RobotNose(air_tank_capacity_liters=2)

    n.smell(ROSE)
    n.smell(DAISY)

    # Should raise error on full tank
    with pytest.raises(RuntimeError):
        n.smell(TULIP)

    # Reset tank
    n.rest()

    n.smell(TULIP)
    assert set([ROSE, DAISY, TULIP]) == n.get_smelled_smells()
