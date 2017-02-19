# child class - wheeled robot:

from robot import Robot
from move_with_wheels import MoveWithWheels
from sense_with_ping import SenseWithPing

class WheeledRobot(Robot):

    def __init__(self):
        move_instance = MoveWithWheels()
        self.set_move_behavior(move_instance)

        sense_instance = SenseWithPing()
        self.set_sense_behavior(sense_instance)

        desc = "I am a robot with wheels"
        self.set_description(desc)
