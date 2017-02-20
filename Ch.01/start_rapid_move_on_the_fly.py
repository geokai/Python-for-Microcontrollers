# interface class - dynamic binding eg:

from move_behavior import MoveBehavior

class StartRapidMoveOnTheFly(MoveBehavior):

    def move(self):
        print "I am now moving rapidly"
