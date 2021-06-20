## README

The purpose of this document is to serve as a manual. 
As such, it will follow the style of the ISO rule 9001,
as to ensure the best understanding of everyone that may have
access to it

###INTRODUCTION

We are tasked with the creation of such a script that,
upon a simple execution, can make a backup of every
file in a folder. Said script shall only take four parameters upon execution,
one mandatory, the folder, and three optional, a list of exceptions ,
if we want to have screen output or not and the file we want to write the logs to

###VOCABULARY

#####Python:

High-level, interpreted programming language

#####Fire

Module for Python designed by Google
which makes it mossible to turn a file into a CCommand Line Interface

#####Hashlib

Module for Python which holds objects and methods related to security
checks such as checksums

#####Checksum

Computing redundant function used to assert the integrity of data

#####MD5

Short for "Message Digest Algorithm 5". Checksum algorithm used in security

#####Datetime

Python module which holds methods and objects related to time and date

#####Shutils

Python module which holds system utilities

#####Os

Python module which contains objects and methods in consonancy with the operative system,
such as the ones related to filepaths

#####Logging

Python module which allows to make use of an advanced logs system,
which can, verbi gratia, write the log to a file instead of
just showing it on-screen

#####Handler

Object of the Logging module which sets a channel to drop the logs.
There are two kinds, FileHandler, which writes to a file, and StreamHandler,
which shows on-screen

#####Flag

Kind of command parameter which holds a boolean value and whose single presence
already means it's valued as True (and recirpocally its abscence means it's valued as False)

###NOTE

As per the tasker's wishes, the folders to hold the backup files
are to be named in Spanish, as such, Lunes is Monday, Martes is Thursday,
Miercoles is Wednesday, Jueves is Tuesday, Viernes is Friday,
Sabado is Saturday and Domingo is Sunday

###Preparations

#### 1. Virtual environment

Python isn't used raw most of the time, and a virtual environment (venv for short), sort of a specialized
interpreter made by cloning the original, is used instead.
The documentation for the creation of it, both on Windows and unix systems,
is here: https://docs.python.org/3/library/venv.html

#### 2. Activating the virtual envitonment
Once we have created it, we'll activate it. On Windows, go to the Scripts folder
inside the venv and execute activate.bat. On Unix, go to the bin folder and write
`source activate`

#### 3. Installing the requirements

Once all this is done, we have to install the files needed for execution.
cd to the folder where we have Weeko and write on the terminal 
`pip install -r requirements.txt`. On some Unix systems, which hold both Python 2.X and Python 3.X,
use `pip3 install -r requirements.txt` instead


###Description

Our script will accept on the call three arguments, a folder, a list of exceptions and a flag.

The format is as follows: python weeko.py --folder --exceptions --verbose

--folder refers to the folder we want to backup. It's mandatory

--exceptions is a list of file extensions we don't want to backup. 
A list is depicted as in "[elements]". Were it to fail to gett it as empty
(noticeable because an error advising of a wrong file path will arise)
write it as "[]". Also, extensions go without the dot

--verbose means if we want the logs to also show on-screen or not

--logfile is the file where we want to write our logs into

As a practical example, were we to want to backup the folder called
Azbuka situated in the root of our hard drive C, but we wouldn't want to backup
batch execution files (.bat), and we want to have screen output, 
but with the log file being one called mylog.log
which is on "C:\logs\"
our command call would look like this:

`python weeko.py C:\Azbuka "[bat]" --verbose C:\logs\mylog.log`

Now, getting into the code, it goes like this.

1. It will check that all the parameters type match. They do
2. It'll get, from the folder we have given him open with os,
all the files whose extension don't match with any on the exceptions
3. It'll instantiate the log prompt wth logging, using as options for the config a single Handler,
a FileHandler pointing towards the logfile by default, and using as a header of each log the time
(given in HH-MM-SS format), the log prompt (by default it's called root) and the kind of log it is
(INFO by default)
4. If we are verbose, it's going to add a StreamHandler to write the information on the screen
5. Then, for each of the backup folder and the current weekday folder, it'll check if they exist.
If they don't, it'll create them
6. Using shutils it'll each file into the destination file, with a filename indicating the date
of the backup. All of this preceded of logs indicating the starting time and the ending one.
7. Were it to fail, it'll write a Warning log with a preset text according to what has failed
