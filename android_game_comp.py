import os, sys
import zipfile
import subprocess
from shutil import copyfile

# Define the path to love-android-sdl2 here:
path_to_love_android = "C:/Android/love-android-sdl2"

#record the current working directory at the beginning:
start_directory = os.path.realpath(__file__)

def zipgame(path, loveZip):
    for root, dirs, files in os.walk(path):
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension != ".py" and extension != ".love":
                loveZip.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file),
                    os.path.join(path, '.')))

if __name__ == '__main__':
    currDirect = os.path.dirname(os.path.realpath(__file__))
    loveFile = zipfile.ZipFile(
        currDirect + '/game.love',
        'w',
        zipfile.ZIP_DEFLATED)
    zipgame(currDirect, loveFile)
    loveFile.close()
    if os.path.exists(path_to_love_android + '/assets/game.love'):
        os.remove(path_to_love_android + '/assets/game.love')
    os.rename(currDirect + '/game.love', path_to_love_android + '/assets/game.love')

    if not os.path.exists(path_to_love_android):
        os.makedirs(path_to_love_android)

    batch_file = os.path.join(path_to_love_android, "auto_ant.bat")
    with open(batch_file, 'w') as batch:
        batch.write("ant debug")

    os.chdir(path_to_love_android)
    print ("Running Apache Ant debug compilation...")
    p = subprocess.Popen(batch_file, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    #print (stdout)
    #print p.returncode
	
    copyfile(path_to_love_android + '/bin/love-android-debug.apk', currDirect + '/love-android-debug.apk')
    print ("Debug APK created!")
    os.chdir(currDirect)