from os import listdir, path
from datetime import date
import logging as log
import filebackup


class FolderBackup:

    def __init__(self, folder: str, exceptions: list = [], verbose: bool = False):

        self.folder = folder
        self.exc = exceptions
        self.isver = verbose

    def __str__(self):
        print(f"{self.folder}, {self.exc}")

    def makebackup(self):

        files = [e for e in listdir(self.folder) if path.splitext(e)[1] not in self.exc]

        formatter = log.Formatter("%(asctime)")
        logger = log.getLogger("main")
        logger.setLevel(log.INFO)

        if self.isver:
            pass
        else:
            pass
