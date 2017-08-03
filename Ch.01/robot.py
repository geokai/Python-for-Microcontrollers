# parent class:

class Robot(object):

    def __init__(self):
        pass

    def set_description(self, desc):
        self.description = desc

    def get_description(self):
        return self.description

    def set_move_behavior(self, mb):
        self.move_behavior = mb

    def set_sense_behavior(self, sb):
        self.sense_behavior = sb

    def perform_move(self):
        self.move_behavior.move()

    def perform_sense(self):
        self.sense_behavior.sense()
