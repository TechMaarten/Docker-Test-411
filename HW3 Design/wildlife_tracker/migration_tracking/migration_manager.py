from typing import Optional, List

from wildlife_tracker.migration.migration import Migration

from wildlife_tracker.migration.migration_path import MigrationPath

from wildlife_tracker.habitat_management.habitat import Habitat

from wildlife_tracker.animal_management.animal import Animal

class MigrationManager:
    def __init__(self) -> None:
        self.migrations: dict[int, Migration] = {}
        self.paths: dict[int, MigrationPath] = {}

    def create_migration(self, migration: Migration) -> None:
        # Add a migration to the manager
        self.migrations[migration.migration_id] = migration

    def remove_migration(self, migration_id: int) -> None:
        # Remove a migration by ID
        if migration_id in self.migrations:
            del self.migrations[migration_id]

    def create_migration_path(self, path: MigrationPath) -> None:
        # Add a migration path to the manager
        self.paths[path.path_id] = path

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        # Retrieve a migration by its ID
        return self.migrations.get(migration_id)

    def get_migration_path_by_id(self, path_id: int) -> Optional[MigrationPath]:
        # Retrieve a migration path by its ID
        return self.paths.get(path_id)

    def assign_animal_to_migration(self, migration_id: int, animal: Animal) -> None:
        # Assign an animal to a migration event
        migration = self.get_migration_by_id(migration_id)
        if migration:
            migration.add_animals_to_migration([animal])

    def get_migration_details(self, migration_id: int) -> Optional[dict]:
        # Get details of a migration by its ID
        migration = self.get_migration_by_id(migration_id)
        if migration:
            return migration.get_migration_details()
        return None
