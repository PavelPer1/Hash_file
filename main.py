import hashlib
import shutil
import os


class HashPath:
    def __init__(self):
        pass

    def add_hash(self, path):
        hash_path = hashlib.sha256(path.encode())

        name = os.path.basename(shutil.copy2(path, 'hash'))

        extension = os.path.splitext(name)[1]

        os.rename(f'hash/{name}', f'hash/{hash_path.hexdigest()}{extension}')
        return hash_path.hexdigest()

    def remove_hash(self, path):
        try:
            os.remove(path)
        except:
            return 'Path is not a file'

    def change_index(self, index, index_new):
        os.rename(f'hash/{index}', f'hash/{index_new}')





