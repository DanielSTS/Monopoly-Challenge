from models.Player import Player


class Cautios(Player):
    def check_profile_purchase_property(self, property):
        if self.balance - property.cost_of_sale >= 80:
            property.buy(self)
            return True
        return False