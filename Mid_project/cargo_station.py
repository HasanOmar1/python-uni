from cargo_item import CargoItem


class CargoStation:
    def __init__(self):
        self.cargo_items = []

    def add_item(self,item:CargoItem):
        self.cargo_items.append(item)

    def remove_item(self,item_id):
        self.cargo_items.remove(item_id)

    def find_item(self,item_id):
        for item in self.cargo_items:
            if item.item_id == item_id:
                return item

    def get_total_weight(self):
        total_weight = 0
        for item in self.cargo_items:
            total_weight += item.weight

        return total_weight