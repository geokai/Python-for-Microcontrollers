# client - test_code:

from robot import Robot
from wheeled_robot import WheeledRobot
from tracked_robot import TrackedRobot
from move_behavior import MoveBehavior
from sense_behavior import SenseBehavior
from move_with_wheels import MoveWithWheels
from move_with_tracks import MoveWithTracks
from sense_with_ping import SenseWithPing
from sense_with_lidar import SenseWithLidar

if __name__ == "__main__":
    print
    print '_' * 48
    print
    print "Wheeled Robot"
    print
    wheeled = WheeledRobot()
    wheeled.perform_move()
    wheeled.perform_sense()
    print
    print '_' * 48
    print
    print "Tracked Robot"
    print
    tracked = TrackedRobot()
    tracked.perform_move()
    tracked.perform_sense()
    print
    print '_' * 48
    print
