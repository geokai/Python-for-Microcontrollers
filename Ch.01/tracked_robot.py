# child class - tracked robot:

from robot import Robot
from move_with_tracks import MoveWithTracks
from sense_with_lidar import SenseWithLidar

class TrackedRobot(Robot):
    """A robot that uses tracked movement"""

    def __init__(self):
        """create a movement with tracks object"""
        move_instance = MoveWithTracks()
        self.set_move_behavior(move_instance)

        sense_instance = SenseWithLidar()
        self.set_sense_behavior(sense_instance)

        desc = "I am a robot with tracks"
        self.set_description(desc)
