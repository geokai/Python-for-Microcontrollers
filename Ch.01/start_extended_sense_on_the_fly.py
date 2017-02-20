# interface class - dynamic binding eg:

from move_behavior import MoveBehavior

class StartExtendedSenseOnTheFly(MoveBehavior):

    def sense(self):
        print "I am now using extended sensing"
