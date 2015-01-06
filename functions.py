import os

def createDumpFolder():
    if not os.path.exists("dump"):
        os.makedirs("dump")
              
def createDatabaseFolder():
    if not os.path.exists("database"):
        os.makedirs("database")