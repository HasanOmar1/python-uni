from cargo_item import CargoItem

class SpecialCargo(CargoItem):
    def __init__(self,item_id , name, weight , origin_planet, danger_level , requires_cooling):
        super().__init__(item_id, name, weight, origin_planet)
        self.danger_level = danger_level
        self.requires_cooling = requires_cooling

    @property
    def danger_level(self):
        return self.danger_level

    @danger_level.setter
    def danger_level(self, value):
        if value < 1 or value > 5:
            print("danger_level must be between 1 and 5")
            return

        self.__danger_level = value

    @property
    def requires_cooling(self):
        return self.requires_cooling

    @requires_cooling.setter
    def requires_cooling(self, value:bool):
         self.__requires_cooling = value


    def __str__(self):
        return f"Special Cargo: {super.__str__(self)} - {self.item_id} - {self.name} - {self.weight}"
