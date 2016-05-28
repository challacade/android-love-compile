# Android LOVE Compile Automation

The script contained in this repository (android_game_comp.py) utilizes love-android-sdl2 (by MartinFelis) and performs all steps necessary to create a debug version APK for a LOVE project.

Directions for use:

1. Download the script and place it in the same directory as your LOVE project.
2. Open the script in a text editor
3. At the top of the file, edit the value of the variable "path_to_love_android" to point to the location of love-android-sdl2
4. Run the script

This script will then do everything for you all at once: zip the contents of the directory (minus the script) into an archive and change it to a LOVE file, move that LOVE file to the love-android-sdl2 directory, run Apache Ant in debug mode to compile the APK, and finally move the resulting APK back to the original directory.
