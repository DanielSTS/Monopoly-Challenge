from models.Player import Player


class Property:
    def __init__(self, name, buy_price, rent_price, owner=None):
        self.name = name
        self.cost_of_sale = buy_price
        self.rent_price = rent_price
        self.owner = owner

    def __repr__(self):
        return f'{self.name}'

    def available_for_buy(self):
        return self.owner is None

    def buy(self, player: Player):
        if self.available_for_buy():
            if player.player_has_enought_balance(self.cost_of_sale):
                player.update_balance(self.cost_of_sale)
                self.owner = player
                return True
        return False

    def receive_rent(self, player: Player):
        if player.player_has_enought_balance(self.rent_price):
            player.update_balance(self.rent_price)
            self.owner.balance += self.rent_price
        else:
            player.update_balance(self.rent_price)

    def return_for_bank(self):
        self.owner = None
        return True