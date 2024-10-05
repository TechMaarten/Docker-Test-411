from typing import Any, Optional, List

from wildlife_tracker.habitat_management.habitat import Habitat

from wildlife_tracker.animal_management.animal import Animal

class Migration:
    def __init__(self, migration_id: int, species: str, start_habitat: Habitat, end_habitat: Habitat, duration: int, animals: Optional[List[Animal]] = None) -> None:
        self.migration_id = migration_id
        self.species = species
        self.start_habitat = start_habitat
        self.end_habitat = end_habitat
        self.duration = duration  
        self.animals = animals or []

    def update_migration_details(self, **kwargs: Any) -> None:
        # Update the details of a migration
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def add_animals_to_migration(self, animals: List[Animal]) -> None:
        # Add animals to the migration
        self.animals.extend(animals)

    def get_migration_details(self) -> dict:
        # Return migration details as a dictionary
        return {
            "migration_id": self.migration_id,
            "species": self.species,
            "start_habitat": self.start_habitat.habitat_id,
            "end_habitat": self.end_habitat.habitat_id,
            "duration": self.duration,
            "animals": [animal.animal_id for animal in self.animals]
        }
