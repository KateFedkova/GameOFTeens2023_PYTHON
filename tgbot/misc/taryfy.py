"""Class for lifecell tariffs data."""

from dataclasses import dataclass


@dataclass
class Tariff:

    weeks: int
    internet: int
    calls: int
    price: int
