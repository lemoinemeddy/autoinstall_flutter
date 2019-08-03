# Lemoine Meddy 2019 - Libre de fork - Free fork - Livre de fork
# Auto install Flutter Debian system
import os

def execute(folder):
    print("Get command line tools")
    os.system("sudo apt install bash  curl  git  unzip   xz-utils ")
    print("start download  Flutter SDK")
    os.system("cd")
    os.system("git clone https://github.com/flutter/flutter.git")
    os.system("""echo export PATH="$PATH:$HOME/flutter/bin" > bash_profile""")
    os.system("source bash_profile")
    os.system("flutter doctor")
    os.system("mkdir " + folder)
    os.system("cd " + folder)
    print("done !")
    os.system("flutter doctor")
    print("PLEASE INSTALL ANDROID SDK MANUALY IF NEEDED !")
    os.system("mkdir " + folder)
    os.system("cd " + folder)
    print("done !")
execute("labs")
