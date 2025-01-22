from .robot import Robot
from .person import Person

# Create Robot instances
r1 = Robot("obinna", "red", 30)
r2 = Robot("magnus", "yellow", 24)

# Create Person instances
p1 = Person("Alice", "aggressive", False, r1)
p2 = Person("Bob", "talkative", True, r2)



# Introduce the robot owned by p1
p1.robotOwned.introduce_self()

# Introduce the robot owned by p2
p2.robotOwned.introduce_self()
