from Prac8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name='', fuel=0, fanciness=0):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def drive(self, distance):
        return super().drive(distance)

    def start_fare(self):
        super().start_fare()

    def get_fare(self):
        return super().get_fare() + self.flagfall
