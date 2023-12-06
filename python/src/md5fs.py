"""
File storage system for large amount of files.

Uses md5 hashes for file names and a deep directory structure.
Please have a look into README.md for a detailed documentation.
"""
import os
import hashlib

# TODO: Tests mit pytest und pytest_cov erstellen
# TODO: GH Actions Tests und Deployment laufen lassen, siehe https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
# TODO: In PIP bereitstellen und Einbindung dokumentieren

class MD5FileHandler:

    def __init__(self, root_path = "./", depth = 5):
        self.root_path = root_path
        self.depth = depth

    def _calculate_full_path(self, md5_hash, is_metadata):
        filename = md5_hash
        if is_metadata:
            filename += ".json"
        return os.path.join(self.root_path, md5_hash[0], md5_hash[1], md5_hash[2], md5_hash[3], md5_hash[4], filename)

    def create_file(self, filename, content, content_type):
        md5_hash = hashlib.md5(content).hexdigest()
        file_content_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = False)
        file_metadata_path = self._calculate_full_path(md5_hash = md5_hash, is_metadata = True)
        # TODO: Inhalt speichern
        # TODO: Metadatan speichern
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
