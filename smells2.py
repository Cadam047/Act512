class BaseNose:
    def __init__(self):
        self.smelled_smells = set()

    def get_smelled_smells(self):
        """Return a copy of the previously encountered odors."""
        return self.smelled_smells.copy()


class HumanNose(BaseNose):
    def __init__(self, allergies=None):
        super().__init__()
        self.allergies = allergies or []
        self.immune_response = False

    def smell(self, odor):
        if self.immune_response:
            raise RuntimeError("Human nose cannot smell when immune response is active.")

        if odor in self.allergies:
            self.immune_response = True
        else:
            self.smelled_smells.add(odor)

    def rest(self):
        self.immune_response = False


class RobotNose(BaseNose):
    def __init__(self, air_tank_capacity_liters=20):
        super().__init__()
        self.air_tank_capacity_liters = air_tank_capacity_liters
        self.current_air_tank_level = 0

    def smell(self, odor):
        if self.current_air_tank_level >= self.air_tank_capacity_liters:
            raise RuntimeError("Robot nose cannot smell when air tank is full.")
        self.smelled_smells.add(odor)
        self.current_air_tank_level += 1

    def rest(self):
        self.current_air_tank_level = 0


if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")
