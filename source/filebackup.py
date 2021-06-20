import shutil as ut
from hashlib import md5

class FileBackup:

    def __init__(self, file: str, target: str):
        self.file = file
        self.target = target
        self.logs = {
            "start": f"Starting backup of file {self.file}",
            "end": f"Backup ended for file {self.file}",
            "read_error": "failed on reading the file",
            "verbose": f"filename: {self.file}, md5: {self.__getmd5__()}"
        }

    def backup(self):
        try:
            ut.copyfile(self.file, self.target)
        except ut.ReadError:
            return self.logs["read_error"]

    def __getmd5__(self):
        with open(self.file, "rb") as readable:
            bytes = readable.read()
            filemd5 = md5()
            filemd5.update(bytes)
            return filemd5.hexdigest()