class CargoItem:
    def init(self, item_id , name , weight , origin_planet):
        self.__item_id = item_id
        self.name = name
        self.weight = weight
        self.origin_planet = origin_planet


    @property
    def item_id(self):
        return self.item_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name:str):
        if len(name) < 2:
            print("Name must be at least 2 characters")
            return

        self.__name = name

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            print("Weight must be greater than 0")
            return

        self.__weight = weight

    @property
    def origin_planet(self):
        return self.origin_planet

    @origin_planet.setter
    def origin_planet(self, planet):
        self.__origin_planet = planet

    def __str__(self):
        return f"Cargo Item: {self.item_id} - {self.name} - {self.weight} - {self.origin_planet}"

