import fire
from source.folderbackup import FolderBackup


def makebackup(folder: str, exceptions: list = [], verbose: bool =False):

    FolderBackup(folder=folder, exceptions=exceptions, verbose=verbose).makebackup()


if __name__ == '__main__':

    fire.Fire(makebackup, '')
    fire.Fire(makebackup)