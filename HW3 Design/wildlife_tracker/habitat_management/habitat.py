from typing import Any, List, Optional

class Habitat:
    def __init__(self, habitat_id: int, geographic_area: str, size: int, environment_type: str, animals: Optional[List[Animal]] = None) -> None:
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        self.animals = animals or []

    def update_habitat_details(self, **kwargs: Any) -> None:
        # Update habitat details
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        # Assign a list of animals to the habitat
        self.animals.extend(animals)

    def get_animals_in_habitat(self) -> List[Animal]:
        # Get a list of animals in the habitat
        return self.animals

    def get_habitat_details(self) -> dict:
        # Return the habitat details as a dictionary
        return {
            "habitat_id": self.habitat_id,
            "geographic_area": self.geographic_area,
            "size": self.size,
            "environment_type": self.environment_type,
            "animals": [animal.animal_id for animal in self.animals]
        }
