from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENT: float = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOOD = ["Meat", "Vegetable", "Fruit", "Seed"]
    WEIGHT_INCREMENT: float = 0.35

    def make_sound(self):
        return "Cluck"


