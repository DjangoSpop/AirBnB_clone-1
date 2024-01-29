import shutil

def create_database_backup(source_path, destination_path):
    shutil.copy2(source_path, destination_path)

# Usage example
source_path = "/path/to/source/database.db"
destination_path = "/path/to/backup/database_backup.db"

create_database_backup(source_path, destination_path)
