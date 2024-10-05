from typing import List, Optional

from wildlife_tracker.habitat_management.habitat import Habitat

from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    def __init__(self) -> None:
        # Dictionary to store habitats by habitat ID
        self.habitats: dict[int, Habitat] = {}

    def create_habitat(self, habitat: Habitat) -> None:
        # Add a new habitat to the manager
        self.habitats[habitat.habitat_id] = habitat

    def remove_habitat(self, habitat_id: int) -> None:
        # Remove a habitat by its ID
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        # Get a habitat by its ID
        return self.habitats.get(habitat_id)

    def assign_animal_to_habitat(self, habitat_id: int, animal: Animal) -> None:
        # Assign an animal to a habitat by habitat ID
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            habitat.assign_animals_to_habitat([animal])

    def get_animals_in_habitat(self, habitat_id: int) -> Optional[List[Animal]]:
        # Return the list of animals in a habitat by habitat ID
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            return habitat.get_animals_in_habitat()
        return None
