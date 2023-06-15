from dataclasses import dataclass
from typing import Optional


@dataclass
class UsefulEntity:
    useful_data: str
    id: Optional[int] = None
