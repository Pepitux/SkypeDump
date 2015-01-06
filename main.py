import sys
from database import contacts,skypeUser,messagesDump,messageSearch,messageByUser,videoMessages,fileTransfer,contactsIp

def main():
    print '   _________  ___       _____ ____    _____ _____________ ______________                   '
    print '  |         ||   \     /    //    \  /    ||            ||             |                   '
    print '  |      ___||    \   /    / \     \/    / |     ____   ||      _______|                   '
    print '  |     |    |     \_/    /   \         /  |    |   |   ||     |_____                      '
    print '  |     \___ |           |     \       /   |    |___|   ||          |                      '
    print '  |___     | |     __    \      \     /    |            ||      ____|                      '
    print '   ___|    | |    |  \    \     |    |     |     _______||     |________                   '
    print '  |        | |    |   \    \    |    |     |    |        |             |                   '
    print '  \________| |____|   |_____\   |____|     |____|        |_____________|                   '
    print '\n                                                                                         '
    print '   __________    ____      ____  ____          ____  _____________ ____                    '
    print '  |          \  |    |    |    ||    \        /    ||            ||   |                    '
    print '  |    ___    \ |    |    |    ||     \      /     ||     ____   ||   |                    '
    print '  |   |   \    \|    |    |    ||      \    /      ||    |   |   ||   |                    '
    print '  |   \   |    ||    |    |    ||       \__/       ||    |___|   ||   |                    '
    print '  |    \_/     ||    |    |    ||   |\        /|   ||            ||   |                    '
    print '  |           / |    |____|    ||   | \______/ |   ||     _______||___|                    '
    print '  |          /  |              ||   |          |   ||    |         ___                     '
    print '  |_________/   |______________||___|          |___||____|        |__|  By @Pepitux        '
    print '\n\n                                                                                       '
        
    raw_input('Press ENTER to start \n')

    print 'DATABASE LOCATIONS: \n                                                                         '
    print '      - WINDOWS COMPUTER: C:\Users\%USER%\AppData\Roaming\Skype\%SKYPE_USER% \n                '
    print '      - APPLE IPOD IOS: /User Applications/Skype/Library/Application Support/%SKYPE_USER% \n   '
    print '      - LINUX OS: /home/user/.Skype/%SKYPE_USER% \n                                            '
    print '      - MAC OS X: /Users/%USER%/Library/Application Support/Skype/%SKYPE_USER% \n              '
    print '      - ANDROID(ROOTED DEVICE): System/data/data/com.skype.%%/files/%SKYPE_USER% \n            '
    print '      - MOVE ANY SKYPE DATABASE TO THE DATABASE DIRECTORY AND START DUMPING!                   '
    
    while True:
        option = -1
        while ((int(option) != 0)  and(int(option) != 1)  and (int(option) != 2)  and 
                   (int(option) != 3)  and (int(option) != 4) and (int(option) != 5) and (int(option) != 6) and (int(option) != 7) and (int(option) != 8)):
                print 'SELECT AN OPTION:'            
                print '\n'
                print '1)  Skype user information '
                print '2)  Contacts '
                print '3)  Messages '
                print '4)  Messages by keyword '
                print '5)  Messages by contact '
                print '6)  Video/Audio messages '
                print '7)  Sent/Received files '
                print '8)  contacts IP address '
                print '0)  exit '
                print '\n'
                
                choice = raw_input('Insert an option: ')
                
                try:
                    option = int(choice)
                except:
                    raw_input('Invalid input, try again .. \n')
                print '\n\n'
        if (option == 1):
            fUser = open('dump/skypeUser.txt', 'w+')
            fUser.write("NAME" + '   |   ' + "SKYPE_USER" + '   |   ' + "EMAIL" + '   |   ' + "PHONE_NBR" + '\n\n')
            for row in skypeUser():
                print row
                sUser = str(row).decode('string_escape')
                fUser.write(sUser + '   |   ')
            fUser.close()
        else:
            if (option == 2):
                fContacts = open('dump/skypeContacts.txt','w+')
                fContacts.write("NAME" + '   |   ' + "SKYPE_USER" + '\n\n')
                for row in contacts():
                        print str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape')
                        sContacts = str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape')
                        fContacts.write(sContacts + '\n')
                fContacts.close()
            else:
                if (option == 3):
                    fMessages = open('dump/skypeMessages.txt', 'w+')
                    fMessages.write("DATE" + '   |   ' + "CHAT_NAME" + '   |   ' + "FROM" + '   |   ' + "TEXT" + '\n\n')
                    for row in messagesDump():
                        print str(row[0]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[1]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[2]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[3]).replace('\\','//').decode('string_escape')
                        sMessages = str(row[0]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[1]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[2]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[3]).replace('\\','//').decode('string_escape')
                        fMessages.write(sMessages + '\n')
                    fMessages.close()
                else:
                    if (option == 4):
                        key = raw_input('Insert a key word: ')
                        fMessagesKey = open('dump/messagesByKeyWord.txt', 'w+')
                        fMessagesKey.write("DATE" + '   |   ' + "CHAT_NAME" + '   |   ' + "FROM" + '   |   ' + "TEXT" + '\n\n')
                        for row in messageSearch(key):
                            print str(row[0]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[1]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[2]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[3]).replace('\\','//').decode('string_escape')
                            sMessagesKey = str(row[0]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[1]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[2]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[3]).replace('\\','//').decode('string_escape')
                            fMessagesKey.write(sMessagesKey + '\n')
                        fMessagesKey.close()
                    else:
                        if (option == 5):
                            user = raw_input('Insert Skype user to display messages: ')
                            fMessagesByUser = open('dump/messagesByUser.txt', 'w+')
                            fMessagesByUser.write("DATE" + '   |   ' + "CHAT_NAME" + '   |   ' + "FROM" + '   |   ' + "TEXT" + '\n\n')
                            for row in messageByUser(user):
                                print str(row[0]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[1]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[2]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[3]).replace('\\','//').decode('string_escape')
                                sMessagesByUser = str(row[0]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[1]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[2]).replace('\\','//').decode('string_escape') + '   |   ' + str(row[3]).replace('\\','//').decode('string_escape')
                                fMessagesByUser.write(sMessagesByUser + '\n')
                            fMessagesByUser.close()
                        else:
                            if (option == 6):
                                fVideoMessages = open('dump/videoMessages.txt', 'w+')
                                fVideoMessages.write("DATE" + '   |   ' + "CHAT_NAME" + '   |   ' + "FROM" + '   |   ' + "INFORMATION" + '\n\n')
                                for row in videoMessages():
                                    print str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape') + '   |   ' + str(row[2]).decode('string_escape') + '   |   ' + str(row[3]).decode('string_escape')
                                    sVideoMessages = str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape') + '   |   ' + str(row[2]).decode('string_escape') + '   |   ' + str(row[3]).decode('string_escape')
                                    fVideoMessages.write(sVideoMessages + '\n')
                                fVideoMessages.close()
                            else:
                                if (option == 7):
                                    fFileTransfer = open('dump/fileTransfer.txt', 'w+')
                                    fFileTransfer.write("DATE" + '   |   ' + "FROM" + '   |   ' + "FILE_LOCATION" + '   |   ' + "FILE_NAME" + '\n\n')
                                    for row in fileTransfer():
                                        print str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape') + '   |   ' + str(row[2]).decode('string_escape') + '   |   ' + str(row[3]).decode('string_escape')
                                        sfileTransfer = str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape') + '   |   ' + str(row[2]).decode('string_escape') + '   |   ' + str(row[3]).decode('string_escape')
                                        fFileTransfer.write(sfileTransfer + '\n')
                                    fFileTransfer.close()
                                else:
                                    if (option == 8):
                                        try:
                                            fContactsIp = open('dump/contactsIP.txt', 'w+')
                                            fContactsIp.write("DATE" + '   |   ' + "USER_NAME" + '   |   ' + "NAME" + '   |   ' + "COUNTRY" + '   |   ' + "IP_ADRESS" + '\n\n')
                                            for row in contactsIp():
                                                if str(row[4] != 'none'):
                                                    print str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape') + '   |   ' + str(row[2]).decode('string_escape') + '   |   ' + str(row[3]).decode('string_escape') + '   |   ' + str(row[4]).decode('string_escape')
                                                    sContactsIp = str(row[0]).decode('string_escape') + '   |   ' + str(row[1]).decode('string_escape') + '   |   ' + str(row[2]).decode('string_escape') + '   |   ' + str(row[3]).decode('string_escape') + '   |   ' + str(row[4]).decode('string_escape')
                                                    fContactsIp.write(sContactsIp + '\n')
                                            fContactsIp.close()
                                        except:
                                            print "Try another option !"   
                                    else:
                                        if (option == 0):
                                            leave = ""
                                            while (leave != 'y') and (leave != 'n'):
                                                leave = raw_input('Are you sure you want to exit? yes(y)/no(n): ')
                                            if leave == 'y':
                                                break
                                                sys.exit(0)
                                            else:
                                                return(main())
                                            
        
main()




