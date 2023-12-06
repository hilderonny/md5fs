"""
File storage system for large amount of files.

Uses md5 hashes for file names and a deep directory structure.
Please have a look into README.md for a detailed documentation.
"""
import os
import hashlib
import json

# TODO: Tests mit pytest und pytest_cov erstellen
# TODO: GH Actions Tests und Deployment laufen lassen, siehe https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
# TODO: In PIP bereitstellen und Einbindung dokumentieren

class MD5FileHandler:

    def __init__(self, root_path = "./", depth = 5):
        self.root_path = root_path
        self.depth = depth

    def _calculate_path(self, md5_hash):
        hash_parts = list(md5_hash)[:self.depth]
        return os.path.join(self.root_path, *hash_parts)

    def create_file(self, filename, content, content_type):
        md5_hash = hashlib.md5(content).hexdigest()
        file_path = self._calculate_path(md5_hash = md5_hash)
        os.makedirs(file_path, exist_ok=True)
        # Save content file
        with open(os.path.join(file_path, md5_hash), "wb") as file:
            file.write(content)
        # Save metadata
        metadata = {
            "filename" : filename,
            "contenttype" : content_type
        }
        with open(os.path.join(file_path, md5_hash + ".json"), "w") as file:
            json.dump(metadata, file)
        return md5_hash

    def delete_file(self, md5_hash):
        file_content_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = False)
        file_metadata_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = True)
        # TODO: Inhalt löschen
        # TODO: Metadaten löschen
        pass

    def get_file_content(self, md5_hash):
        file_content_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = False)
        # TODO: Inhalt herausgeben
        pass

    def get_file_metadata(self, md5_hash):
        file_metadata_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = True)
        # TODO: Metadaten herausgeben
        pass

    def save_file_content(self, md5_hash, content):
        file_content_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = False)
        # TODO: Inhalt speichern
        # TODO: Dokumentieren, dass hierüber das Generieren eines Hashes und das Erzeugen von Metadaten umgangen werden kann. Nützlich für IPED Tasks
        pass

    def save_file_metadata(self, md5_hash, metadata):
        file_metadata_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = True)
        # TODO: Metadaten speichern
        pass
