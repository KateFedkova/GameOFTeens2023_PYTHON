"""Class for lifecell tariffs data."""

from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Tariff:

    name: str
    weeks: int
    internet: Optional[Union[int, float]]
    calls: Optional[Union[int, float]]
    price: int
