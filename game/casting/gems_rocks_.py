from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Gems_Rock(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""
        self._score = 0
        
    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    def get_score(self):
        if 