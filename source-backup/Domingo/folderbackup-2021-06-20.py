from os import listdir, path, makedirs
from datetime import date
from .filebackup import FileBackup
import logging as log



class FolderBackup:

    def __init__(self, folder: str, exceptions: list,  verbose: bool):
        """
        Constructor method for the class

        :param folder: path to the folder we are going to backup
        :param exceptions: list of file extensions not to be used
        :param verbose: if we want console output or not

        """
        self.folder = folder
        self.exc = [f".{e}" for e in exceptions]  #To add the dot which os needs to identify it with a file extension
        self.isver = verbose

        #File we are writting the logs to
        self.logfile = "weeko.log"

        #Main folder where the backup folders are to be held
        self.backupfolder = f"{folder}-backup/"

    def __str__(self):
        print(f"{self.folder}, {self.exc}")

    def makebackup(self):
        """
        Method for making the backup

        :return: None, or a string if anything has failed
        """

        #This means "all whiles whose extensions aren't in the exceptions list"
        files = [e for e in listdir(self.folder) if path.splitext(e)[1] not in self.exc]

        #Reference of weekdays in Spanish to use as folders for the backups
        dayreference = {
            0: "Lunes",
            1: "Martes",
            2: "Miercoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sabado",
            6: "Domingo"
        }

        #Initial configuration for our logger
        log.basicConfig(filename=self.logfile,
                        filemode="a+",
                        format='%(asctime)s %(name)s %(levelname)s %(message)s', #Time - name - log level
                        datefmt='%H:%M:%S',
                        level=log.INFO)

        logger = log.getLogger("main")

        #If it is verbose, we are going to add a handler which uses the console
        if self.isver:
            logger.addHandler(log.StreamHandler())
        else:
            pass

        FolderBackup.__checkfolder__(self.backupfolder)

        FolderBackup.__checkfolder__(f"{self.backupfolder}/{dayreference[date.weekday(date.today())]}")

        #This is what does the backup
        for e in files:

            #With this we fetch the target file
            filename, ext = path.splitext(e)
            route = f"{self.backupfolder}/{dayreference[date.weekday(date.today())]}/" \
                    f"{filename}-{date.isoformat(date.today())}{ext}"

            backup = FileBackup(f"{self.folder}/{e}", route)

            logger.info(backup.logs["start"])

            #If verbose, it will output in log the file name and the md5
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
        """
        This method checks if a folder exists and if not, it creates it

        :param folder: Folder we are trying to make if not there
        :return: None
        """
        try:
            listdir(folder)
        except FileNotFoundError:
            makedirs(folder)
