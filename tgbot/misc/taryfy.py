"""Class for lifecell tariffs data."""


class Tariff:

    def __init__(self, weeks, internet, calls, price):
        self.weeks = weeks
        self.internet = internet
        self.calls = calls
        self.price = price
