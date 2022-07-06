from models.Player import Player


class Impulsive(Player):
    def check_profile_purchase_property(self, property):
        if self.balance >= property.cost_of_sale:
            property.buy(self)
            return True
        return False