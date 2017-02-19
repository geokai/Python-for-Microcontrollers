# behavior class - sense_with_lidar:

from sense_behavior import SenseBehavior

class SenseWithLidar(SenseBehavior):

    def sense(self):
        print "I use a Lidar sensor to determine distance"
