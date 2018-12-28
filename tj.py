import os, sys, time
from socket import *
import os.path

__version__="1.6.1"

try:
    from autopy import bitmap
    warning=""
except:
    warning="""\n\n------------------------------------\n\n
WARNING: autopy module is not installed.
Use 'pip install autopy' in command line to install autopy
\n\n------------------------------------\n\n
"""

__doc__='''

 _______ ________
|__   __|___   __| PRODUCTIONS 2018
   | |      | |
   | |    __| |
   |_|    \___/ 

%s

A module that can be used to to multiple common tasks that otherwise you
would do by writing long lines of code
Last modified: %s
File Size: %s %s
Last Accessed: %s
Date Created: %s
Version: %s

Updated on: 28th December 2018 10:15PM

    Edit 1: In this version, support for RGB color values is added
          eg- tj.colors[BLACK]=[0,0,0], tj.colors[WHITE]=[255,255,255], etc.
          To see all available colour values, call tj.allcolors()

    Edit 2: In this version, Communicate class is added. It is useful and
          simple class, which you can use in your programs to communicate between
          two computers locally. Both of these computers should run an instance of this
          class. THE FUNCTIONALITY IS STILL IN ALPHA PHASE.

    Edit 3: Corrected some values in colors.
''' % (warning,
    time.asctime(time.localtime(os.stat(__file__)[-2])),
os.stat(__file__)[6],"Bytes",
time.asctime(time.localtime(os.stat(__file__)[-3])),
time.asctime(time.localtime(os.stat(__file__)[-1])), __version__)





colors = {"BLACK": [0, 0, 0], "WHITE": [255, 255, 255], "GOLD": [255,223,0], "METALLIC GOLD": [212,175,55], "LIGHT YELLOW": [255, 255, 224],
          "YELLOW": [255, 255, 40], "ORANGE": [255, 165, 0], "DARK ORANGE": [255, 140, 0], "RED": [255, 0, 0],
          "DARK RED": [135, 0, 0], "MAROON": [120, 0, 0], "BROWN": [165, 42, 42], "PINK": [255, 192, 203],
          "HOT PINK": [255, 105, 180], "LIGHT PINK": [255, 182, 193], "VIOLET": [148, 0, 211], "PURPLE": [160, 32, 240],
          "INDIGO": [75, 0, 130], "BLUE": [0, 0, 255], "SKY BLUE": [135, 206, 250], "DARK BLUE": [0, 0, 139],
          "LIGHT GREEN": [0, 200, 0], "GREEN":[50,205,50], "DARK GREEN": [0, 139, 0], "LIME": [0, 255, 0], "FOREST GREEN": [35, 140, 35],
          "GRAY": [128, 128, 128], "CRIMSON": [220, 20, 60], "BRICK": [178, 34, 34], "FUCHSIA": [255, 0, 255],
          "LIGHT GRAY": [211, 211, 211], "SILVER": [92, 192, 192], "DARK GRAY": [105, 105, 105], "OLIVE": [128, 128, 0],
          "TEAL": [0, 128, 128], "CYAN": [0, 255, 255], "CHARCOAL": [54, 70, 80], "CHOCOLATE": [210, 105, 30],
          "WOOD": [255, 165, 79], "FERRARI": [255, 40, 0], "PEACH": [255, 218, 185], "CREAM": [245, 255, 250],
          "GRAPE": [110, 45, 168], "DENIM": [21, 96, 189], "ARMY": [75, 83, 32], "COFFEE": [111, 78, 55],
          "IRON": [203, 205, 205], "COPPER": [184, 115, 51]}

color_names = list(colors.keys())



class Communicate:
    """In this class, sockets is used communicate between 2 computers
        Usage:
        1) Define an instance C=Communicate(host_tar)  # host_tar is the local IP address of
                                                       # the target / the other computer
        2) Use this instance in a loop
        3) Use C.sendData(data) # to send data to your partner computer. data should be string
                                 # also the data should not be more than 4096 bytes long.

        4) Use C.getData() # to get the data transmitted from your partner computer
        5) Use C.close() # to close the connections."""
    
    def __init__(self,host_tar):
        """Initializer"""
        self.host_tar=host_tar
        self.host=gethostbyname(gethostname())
        self.port = 13000
        self.buf = 4096
        self.addr = (self.host, self.port)
        self.addr_tar = (self.host_tar, self.port)
        self.UDPSock = socket(AF_INET, SOCK_DGRAM)
        self.UDPSock.bind(self.addr)
              
    def sendData(self,data):
        """Use this method to send data"""
        self.UDPSock.sendto(data.encode(), self.addr_tar)

    def getData(self):
        """Use this method to get data"""
        (data, self.addr) = self.UDPSock.recvfrom(self.buf)
        data=data.decode()
        return data

    def close(self):
        """Use this method to close the socket connection"""
        self.UDPSock.close()


def allcolors(color=None, flag=False):

    """allcolors(color=None)
If called, this function prints all the colors available in the module
If the optional color argument color is given, it will search colors related
    to the given color.
    eg- allcolors("GRAY") returns "GRAY" , "DARK GRAY", etc.

There is another optional argument called flag.
flag is set to False by default, and it prints the results, and doesn't return
flag=True returns the results in a list, and prints nothing."""
    if color == None:
        L = color_names
    else:
        L = []
        color = color.upper()
        for c in color_names:
            if color in c:
                L += [c]

    if flag == False:
        for i in L: print("%-20s   %s" % (i, colors[i]))
    else:
        return color_names


def get_filename(path):
    """Takes full path of the file as argument
Gives the file name from the full path of the file with extension"""
    import ntpath
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def get_foldername(path):
    """Takes a path as a string as argument and returns the name of the folder of the file"""
    s=path[::-1]
    a=0
    s2=''
    for i in s:
        if (i=="//") or (i=="\\"):
            a+=1
        if a>0:
            s2+=i
    s3=s2[::-1]
    return s3


def get_files_in_folder(path):
    """Takes the full path of a folder as argument
Gives the full path of all the files in a folder in a list"""
    L = []

    for root, dirs, files in os.walk(os.path.abspath(path)):
        for file in files:
            L += [os.path.join(root, file)]
    return L


def factorial(num):
    """Takes a number as argument
Gives factorial of that argument"""
    if num < 0:
        raise "Number is less than 0"
    if type(num) != type(1):
        raise "Number is not an integer"
    r = 1
    for i in range(1, num + 1):
        r = r * i
    return r


def email(email_id, password, recievers, body, subject="Email sent by TJ module Python", attachments=[]):
    """syntax:
    email(email_id,password,recievers,body,subject="Email sent by TJ module Python",attachment=False)

    subject and attachment parameters are optional.
    email_id - the email id of the sender
    password - password of the sender
    recievers - the list of email id of recievers
    body - the body of the email in string
    subject - subject of email
    attachments - a list of paths of files which you need to send 
                  as attachment
                  """
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase

    uname = email_id
    pword = password

    emailfrom = email_id
    emailto = recievers

    body = [body]
    subject = subject

    msg = MIMEMultipart()
    msg['From'] = emailfrom
    msg['To'] = ', '.join(emailto)
    msg['Subject'] = subject

    msg.attach(MIMEText(''.join(body)))

    ### ATTACH FILES
    for item in attachments:
        part = MIMEBase('application', "zip")

        f = open(item, "rb")
        datatemp = f.read()

        part.set_payload(datatemp)
        filename = get_filename(item)
        part.add_header('Content-Disposition',
                        'attachment; filename="%s"' % filename)
        msg.attach(part)

        ### SECURE CONNECTION
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(uname, pword)

    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()


def is_Folder(path):
    """Takes the path of the folder as argument
Returns is the path is a of a Folder or not in bool"""
    try:
        f = open(path, "r")
        return True
    except:
        return False


def get_startup_path():
    """Takes no arguments
Gives a list of full startup paths on a computer
eg:
[
 "C:\\Users\\ABC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\",
 "C:\\Users\\John PC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\",
 "C:\\Users\\Monica\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"]

 *[Public, Default ,All Users, Default User] user will not be included in this list
"""

    a = "C:\\Users\\"
    b = "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    user_L = os.listdir(a)
    L = []
    for user in user_L:
        if user in ['Public', 'Default', 'All Users', 'Default User']:
            continue
        if is_Folder(a + user):
            continue
        path = a + user + b
        L += [path]
    return L


def convert_bytes(size):
    L = ["Bytes", "KB", "MB", "GB", "TB"]
    for i in range(len(L)):
        if size // (1024 ** i) == 0:
            break
    s = str(size / 1024 ** (i - 1))
    s = s.split(".")
    s1 = s[0]
    s2 = s[1]
    s2 = s2[:2]
    s = s1 + "." + s2
    return "{s} {x}".format(s=s, x=L[i - 1])


def file_size(file_path, Flag=False):
    """file_size(file_path, Flag=False)

Takes the full path of the file as input
Gives the size of the file in bytes

There is another argument Flag (set to False by default).
If Flag is true, it returns in format like 2.3 GB, 5.0 MB, etc.
    """
    size = os.path.getsize(file_path)
    if Flag:
        return convert_bytes(size)
    else:
        return size


def get_last_modified(path,flag=False):
    '''Get the date the the file was last modified of the.
    Arguments:\n path -> the path of the file
    flag-> Its a bool value, when False, the time is returned in
    Epoch seconds, if flag is True, time is returned in proper format.'''
    try:a=os.stat(path)[-2]
    except:raise "Path not found"
    if flag==False:
        return a
    if flag==True:
        return time.asctime(time.localtime(a))



def passed_time(flag=True):
    '''if flag=False, then returns the time after the function is called
        from the time the function was called first time in the program

    if flag=True, then returns the time in seconds b/w two successive calls
    Use it as a generator function
    You can create different instances to use it as per your convinience
    eg-
    import tj
    a=tj.passed_time()
    print a.next(); time.sleep(5)
    print a.next() #This is used after waiting 5 sec.
    b=tj.passed_time()
    print b.next(); time.sleep(5)
    print a.next(); time.sleep(5)
    print b.next()
>>>0.0
>>>5.0
>>>0.0
>>>5.0
>>>10.0
    '''
    t=time.time()
    while True:

        if flag:
            m=time.time()-t
            t=time.time()
            yield m
        if not flag:
            yield time.time()-t


def take_src(name="src.py", DIR=""):
    if warning!="":
        raise ModuleNotFoundError("autopy module not found.\nInstall autopy mudule using 'pip install autopy'")
    """Args->
    name-> name of the file with .png or .bmp extension
    DIR-> Folder where you want to save the file
    name="src.py" by default and DIR="" by default (same as working directory)
    Prints and saves the screen shot in .png or .bmp format in a location"""
    path=os.path.join(DIR,name)
    bitmap2 = bitmap.capture_screen()
    bitmap2.save(path)


def remove_dir(path):
    '''Deletes a directory which is either empty or non-empty'''
    shutil.rmtree(path)
