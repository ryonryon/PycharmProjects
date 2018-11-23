from roboter.views import console


DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    """Base model for robot."""

    def __init__(self, name, username, speak_color):

        self.name = name
        self.username = username
        self.speak_color = speak_color

    def hello(self):
        """Return words to the user that the robot speaks at the beginning."""
        while True:
            template = console
