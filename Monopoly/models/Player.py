import random


class Player:
    def __init__(self, name, opening_balance=300.00):
        self.name = name
        self.balance = opening_balance
        self.in_game = True
        self.board_position = 0
        self.opening_balance = opening_balance
        self.round_credit = 100
        self.qty_played = 0

    def __repr__(self):
        return f'{self.name}'

    def update_balance(self, amount):
        self.balance = self.balance - amount

    def player_has_enought_balance(self, amount_to_pay):
        return True if self.balance >= amount_to_pay else False

    def validate_player_in_game(self):
        if self.balance < 0:
            self.in_game = False
        return self.in_game

    def move(self):
        game_dice = random.choice(range(1, 7))
        self.board_position += game_dice
        self.qty_played += 1

        if self.board_position > 19:
            self.board_position -= 19
            self.balance += self.round_credit

        return self.board_position
