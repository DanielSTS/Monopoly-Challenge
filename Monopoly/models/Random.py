from models.Player import Player
import random


class Random(Player):
    def check_profile_purchase_property(self, property):
        if self.balance >= property.cost_of_sale and random.choice([True, False]):
            property.buy(self)
            return True
        return False
