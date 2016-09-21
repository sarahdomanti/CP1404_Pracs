from Prac7.Car import Car


class Taxi(Car):
    price_per_km = 1.2

    def __init__(self, name="", fuel=0):
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                             self.price_per_km)

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance = distance_driven
        return distance_driven

    def start_fare(self):
        self.current_fare_distance = 0

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance
