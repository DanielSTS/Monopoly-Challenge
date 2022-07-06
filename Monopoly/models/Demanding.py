from models.Player import Player


class Demanding(Player):
    def check_profile_purchase_property(self, property):
        if self.balance >= property.cost_of_sale and property.rent_price > 50:
            property.buy(self)
            return True
        return False