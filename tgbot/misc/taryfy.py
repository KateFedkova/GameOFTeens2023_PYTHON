"""Class for lifecell tariffs data."""

from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Tariff:

    weeks: int
    internet: Optional[Union[int, float]]
    calls: Optional[Union[int, float]]
    price: int
