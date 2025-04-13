from models.action import Action
from models.player import Player
from models.quality import Quality

class UserInputs:
    def __init__(self, players: list[Player], actions: list[Action], action_qualities: list[Quality], raw_data_file_paths: list[str]):
        self.players = players
        self.actions = actions
        self.action_qualities = action_qualities
        self.raw_data_file_paths = raw_data_file_paths