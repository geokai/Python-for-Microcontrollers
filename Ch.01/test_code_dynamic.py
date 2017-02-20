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
from start_rapid_move_on_the_fly import StartRapidMoveOnTheFly
from start_extended_sense_on_the_fly import StartExtendedSenseOnTheFly

if __name__ == "__main__":
    print
    print '_' * 48
    print
    print "\tWheeled Robot"
    print
    wheeled = WheeledRobot()
    wheeled.perform_move()
    wheeled.perform_sense()
    print "\tNow dynamically changing the move:"
    move_instance = StartRapidMoveOnTheFly()
    wheeled.set_move_behavior(move_instance)
    wheeled.perform_move()
    print
    print '_' * 48
    print
    print "\tTracked Robot"
    print
    tracked = TrackedRobot()
    tracked.perform_move()
    tracked.perform_sense()
    print "\tNow dynamically changing the sense:"
    sense_instance = StartExtendedSenseOnTheFly()
    tracked.set_sense_behavior(sense_instance)
    tracked.perform_sense()
    print
    print '_' * 48
    print
