from models.Property import Property
from models.Player import Player
import random


class Board:
    def __init__(self):
        self.properties: [Property] = []
        self.players: [Player] = []
        self.round: int = 1

    def add_property(self, property):
        self.properties.append(property)

    def add_players(self, players):
        for player in players:
            player.balance = 300
            player.board_position = 0
            player.in_game = True
            player.qty_played = 0
            self.players.append(player)
        self._draw_players_order

    def _draw_players_order(self):
        random.shuffle(self.players)

    def remove_player(self, player):
        self.players.remove(player)

    def return_property(self, player):
        for property in self.properties:
            if property.owner == player:
                property.return_for_bank()