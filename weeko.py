import fire
from source.folderbackup import FolderBackup


def makebackup(folder: str, exceptions: list = [], verbose: bool = False, logfile="weeko.log"):
    """
    This function is made to call in an organized manner the backup method. More info about it on
    the method Folderbackup.makebackup() on source.folderbackup

    :param folder: The folder we want to make a backup of
    :param exceptions: The list of exceptions we want to make on file extensions
    :param verbose: If we want to have screen logs or not
    :param logfile: File we are writting the file to

    :return: None
    """

    try:
        assert(isinstance(folder, str))
    except AssertionError:
        print("Backup aborted, the folder must be given as a text chain")
        return None

    try:
        assert(isinstance(exceptions, list))
    except AssertionError:
        print("Backup aborted, the exceptions aren't a list. Have you tried with \"[]\" instead?")
        return None

    try:
        assert(isinstance(verbose, bool))
    except AssertionError:
        print("Backup aborted, verbosity isn't a boolean. Notice that writing --verbose works just fine")
        return None

    try:
        assert(isinstance(logfile, str))
    except AssertionError:
        print("Backup aborted, the log file must be given as a text chain")
        return None

    FolderBackup(folder=folder, exceptions=exceptions, verbose=verbose).makebackup()


if __name__ == '__main__':

    fire.Fire(makebackup)