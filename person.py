class Person:
    def __init__(self, name, personality , isSitting, robotOwned) -> None:
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned


    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False
