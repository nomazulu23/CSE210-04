from game.casting.actor import Actor


class Artifact(Actor):
    def __init__(self):
        super().__init__()
        self._points = 0

#Calculating the points for the game. 1 point if robot touch gem (*) and -1 point if robot touch a rock (o)
    def get_points(self):
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._ponts = -1

        return self._points
