import os


def createFolders():
    if not os.path.exists("database") and not os.path.exists("dump"):
        os.makedirs("database")
        os.makedirs("dump")        
        