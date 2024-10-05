from typing import Any, Optional

class Animal:
    def __init__(self, animal_id: int, species: str, age: int, weight: float) -> None:
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.weight = weight