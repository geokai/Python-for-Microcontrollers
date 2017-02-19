# behavior class - sense_with_ping:

from sense_behavior import SenseBehavior

class SenseWithPing(SenseBehavior):

    def sense(self):
        print "I use a Ping sensor to determine distance"
