# Program FORHAD
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")

# Encoding FORHAD
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "# Obfuscated with PyObfuscate\n# https://www.github.com/htr-tech\n# Time : %s\n# -----------------------------\n" % time.ctime()

def banner():
    print("\033[91m ________  ______   _______   __    __   ______   _______        \033[0m")
    print("\033[92m/        |/      \\ /       \\ /  |  /  | /      \\ /       \\       \033[0m")
    print("\033[93m$$$$$$$$//$$$$$$  |$$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$  |      \033[0m")
    print("\033[94m$$ |__   $$ |  $$ |$$ |__$$ |$$ |__$$ |$$ |__$$ |$$ |  $$ |      \033[0m")
    print("\033[95m$$    |  $$ |  $$ |$$    $$< $$    $$ |$$    $$ |$$ |  $$ |      \033[0m")
    print("\033[96m$$$$$/   $$ |  $$ |$$$$$$$  |$$$$$$$$ |$$$$$$$$ |$$ |  $$ |      \033[0m")
    print("\033[91m$$ |     $$ \\__$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |__$$ |      \033[0m")
    print("\033[92m$$ |     $$    $$/ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$/       \033[0m")
    print("\033[93m$$/       $$$$$$/  $$/   $$/ $$/   $$/ $$/   $$/ $$$$$$$/        \033[0m")
    print("\033[38;5;46m═══════════════════════════════════════\033[0m")
    print("\033[34;1m✮⃝ NAME     ➽ \033[32;1mFORHAD\033[0m")
    print("\033[34;1m✮⃝ TELEGRAM ➽ \033[31;1m@f_forha\033[0m")
    print("\033[34;1m✮⃝ TOOLS    ➽ \033[36;1mFORHAD ENCODER\033[0m")
    print("\033[34;1m✮⃝ FROM     ➽ \033[35;1mBANGLADESH\033[0m")
    print("\033[38;5;46m═══════════════════════════════════════\033[0m")

def menu():
    print("""\033[1;36m [01] \033[0;36mEncode Marshal
\033[1;36m [02] \033[0;36mEncode Zlib
\033[1;36m [03] \033[0;36mEncode Base16
\033[1;36m [04] \033[0;36mEncode Base32
\033[1;36m [05] \033[0;36mEncode Base64
\033[1;36m [06] \033[0;36mEncode Zlib,Base16
\033[1;36m [07] \033[0;36mEncode Zlib,Base32
\033[1;36m [08] \033[0;36mEncode Zlib,Base64
\033[1;36m [09] \033[0;36mEncode Marshal,Zlib
\033[1;36m [10] \033[0;36mEncode Marshal,Base16
\033[1;36m [11] \033[0;36mEncode Marshal,Base32
\033[1;36m [12] \033[0;36mEncode Marshal,Base64
\033[1;36m [13] \033[0;36mEncode Marshal,Zlib,B16
\033[1;36m [14] \033[0;36mEncode Marshal,Zlib,B32
\033[1;36m [15] \033[0;36mEncode Marshal,Zlib,B64
\033[1;36m [16] \033[0;36mSimple Encode
\033[1;31m [17] \033[0;36mExit
""")

class FileSize:
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size : %s\n" % self.datas(dts))

def Encode(option,data,output):
    loop = int(eval(_input % " [-] Encode Count : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n Invalid Option!")
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)

def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        py_compile.compile(output,output)

def MainMenu():
    try:
        os.system('clear') 
        banner()
        menu()
        try:
            option = int(eval(_input % " [-] Option : "))
        except ValueError:
            sys.exit("\n Invalid Option !")
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n Thanks For Using this Tool")
            os.system('clear') 
            banner()
        else:
            sys.exit('\n Invalid Option !')
        try:
            file = eval(_input % " [-] File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")
        output = file.lower().replace('.py', '') + '_FORHAD-EHC99.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n [-] ENCODE-ED  %s" % file)
        print(" [-] SAVED AS  %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
