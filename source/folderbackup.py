from os import listdir, path, makedirs
from datetime import date
from .filebackup import FileBackup
import logging as log



class FolderBackup:

    def __init__(self, folder: str, verbose: bool, exceptions: list):

        self.folder = folder
        self.exc = ["." + e for e in exceptions]  #To add the dot which os needs to identify it with a file extension
        self.isver = verbose
        self.logfile = "weeko.log"
        self.backupfolder = ""

    def __str__(self):
        print(f"{self.folder}, {self.exc}")

    def makebackup(self):

        files = [e for e in listdir(self.folder) if path.splitext(e)[1] not in self.exc]
        dayreference = {
            0: "Lunes",
            1: "Martes",
            2: "Miercoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sabado",
            6: "Domingo"
        }

        log.basicConfig(filename=self.logfile,
                        filemode="a+",
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:&M:%S',
                        level=log.INFO)

        logger = log.getLogger("main")

        if self.isver:
            logger.addHandler(log.StreamHandler())
        else:
            pass

        FolderBackup.__checkfolder__(self.backupfolder)

        FolderBackup.__checkfolder__(f"{self.backupfolder}/{dayreference[date.weekday(date.today())]}")

        for e in files:
            filename, ext = path.splitext(e)
            route = f"{self.backupfolder}/{dayreference[date.weekday(date.today())]}/" \
                    f"{filename}-{date.isoformat(date.today())}{ext}"
            backup = FileBackup(f"{self.folder}/{e}", route)

            logger.info(backup.logs["start"])

            if self.isver:
                logger.info(backup.logs["verbose"])
            else:
                pass

            result = backup.backup()

            if result: #The backup function won't return anything unless it's failed
                logger.critical(result)
            else:
                logger.info(backup.logs["end"])

    @staticmethod
    def __checkfolder__(folder: str):
        try:
            listdir(folder)
        except FileNotFoundError:
            makedirs(folder)

