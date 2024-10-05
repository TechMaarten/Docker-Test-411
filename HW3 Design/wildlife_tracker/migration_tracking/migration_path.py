from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, path_id: int, start_habitat: Habitat, end_habitat: Habitat, species: str) -> None:
        self.path_id = path_id
        self.start_habitat = start_habitat
        self.end_habitat = end_habitat
        self.species = species

    def get_path_details(self) -> dict:
        # Return details of the migration path
        return {
            "path_id": self.path_id,
            "start_habitat": self.start_habitat.habitat_id,
            "end_habitat": self.end_habitat.habitat_id,
            "species": self.species
        }
