import sqlite3 as db
import sys
from functions import createDatabaseFolder, createDumpFolder

error = open('error.log', 'w+')
try:
    global connect
    database = 'database/main.db'
    connect = db.connect(database,check_same_thread = False)
    cursor = connect.cursor()
    connect.row_factory = db.Row
    connect.text_factory = str
except:
    print 'Error connecting to Database'
    createDumpFolder()
    createDatabaseFolder()
    error.write("Error connecting to the database, check its integrity and if its a valid database \n")
    sys.exit()

def skypeUser():
    try:
        query = "SELECT fullname,skypename,emails,phone_mobile FROM Accounts;"
        cursor.execute(query)
        user = cursor.fetchone()
        return user
    except:
        print "skypeUser: database error, please check its integrity"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()
        
def contacts():
    try:       
        query = "SELECT fullname,skypename FROM Contacts ORDER BY fullname asc;"
        cursor.execute(query)
        contacts = cursor.fetchall()
        return (contacts)
    except:
        print "contacts: database error, please check its integrity"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()

def messagesDump():
    try:
        query = "SELECT datetime(timestamp, 'unixepoch'),chatname,from_dispname,body_xml FROM Messages ORDER BY chatmsg_type,timestamp,chatname asc;"
        cursor.execute(query)
        message = cursor.fetchall()
        return message
    except:
        print "messagesDump: database error, please check its integrity"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()

def messageSearch(key):
    try:
        query = "SELECT datetime(timestamp, 'unixepoch'),chatname,from_dispname,body_xml FROM Messages WHERE body_xml LIKE '%%%s%%' AND chatmsg_type = 3 ORDER BY chatmsg_type,timestamp,chatname asc;" % key
        cursor.execute(query)
        smessage = cursor.fetchall()
        return smessage
    except:
        print "messageSearch: database error, please check its integrity \n"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()
        
def messageByUser(user):
    try:
        query = "SELECT datetime(timestamp, 'unixepoch'),chatname,from_dispname,body_xml FROM Messages WHERE chatname LIKE '%%%s%%' and chatmsg_type = 3 ORDER BY chatmsg_type,timestamp,chatname asc;" % user
        cursor.execute(query)
        umessage = cursor.fetchall()
        return umessage
    except:
        print "messageByUser: database error, please check its integrity \n"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()
        
def videoMessages():
    try:
        query = "SELECT datetime(timestamp, 'unixepoch'),chatname,from_dispname,body_xml FROM Messages WHERE chatmsg_type = 18 AND body_xml LIKE '%<duration>%' ORDER BY chatmsg_type,timestamp,chatname asc;"
        cursor.execute(query)
        umessage = cursor.fetchall()
        return umessage
    except:
        print "videoMessages: database error, please check its integrity \n"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()
        
def fileTransfer():
    try:
        query = "SELECT datetime(finishtime, 'unixepoch'),partner_dispname,filepath,filename FROM Transfers ORDER BY finishtime,partner_dispname asc;"
        cursor.execute(query)
        ftransfer = cursor.fetchall()
        return ftransfer
    except:
        print "fileTransfer: database error, please check its integrity \n"
        error.write("error while processing the database, please check its a valida database \n")
        sys.exit()
        
def contactsIp():
    try:
        query = "SELECT datetime(start_timestamp, 'unixepoch'),identity,dispname,country,ip_address FROM CallMembers WHERE ip_address != 'none' ORDER BY start_timestamp,dispname asc;"
        cursor.execute(query)
        contactsip = cursor.fetchall()
        return contactsip
    except:
        print "Column Ip_Adress does not exist in current Skype database version \n"
        error.write("Current database version does not support ip address dumping \n")