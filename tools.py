from datetime import datetime
import os


def cls():
    os.system("cls")


def system(command):
    os.system(command)

def time():
    return datetime.utcnow()
