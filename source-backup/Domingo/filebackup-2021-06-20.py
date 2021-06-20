import shutil as ut
from hashlib import md5

class FileBackup:

    def __init__(self, file: str, target: str):
        """
        Constructor method for the class

        :param file: the file we are to backup
        :param target: the path to the actual backup
        """
        self.file = file
        self.target = target

        #These are generic log texts to raise in errors and such
        self.logs = {
            "start": f"Starting backup of file {self.file}",
            "end": f"Backup ended for file {self.file}",
            "read_error": "failed on reading the file",
            "verbose": f"filename: {self.file}, md5: {self.__getmd5__()}"
        }

    def backup(self):
        """
        This method copies the original file into the destination one

        :return: None
        """
        try:
            ut.copyfile(self.file, self.target)
        except ut.ReadError:
            return self.logs["read_error"]

    def __getmd5__(self):
        """
        This method gets the file md5

        :return: str. The actual md5 checksum
        """
        with open(self.file, "rb") as readable:
            bytes = readable.read()
            filemd5 = md5()
            filemd5.update(bytes)
            return filemd5.hexdigest()