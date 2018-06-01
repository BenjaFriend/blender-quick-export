# Blender/Python quick export as FBX!

# This is a script that go through all blender files in a certain
# directoy, and export them as .FBX files.

# This is depenedany on the quickExport.py script being in the same directoy as
# this, so make sure that it is there!

import os;
from subprocess import call;

# Set the models directoy and output directoy to the current by default
modelsDir = os.getcwd();
outputDir = os.getcwd();

## Print the info about the model location dir and the output dir
def printDirInfo():
    print "\n==== Batch Export Info ====\n";
    print "     Model Dir: " + modelsDir;
    print "     Output Dir: " + outputDir;
    print "\n===========================\n\n"

# Ask the user where their models are
modelsDirInput = raw_input("What directory are your models in? [" + modelsDir + "] ");

# If they just press enter, then use the current directory
if modelsDirInput != '':
    modelsDir = modelsDirInput;

printDirInfo();

# For all the files in this directory
for subdir, dirs, files in os.walk(modelsDir):
    for file in files:
        # If the extension on that file is a blender file
        ext = os.path.splitext(file)[-1].lower();
        if ext == '.blend':
            # Export it in blender
            blendFile = os.path.join(subdir, file);
            print ("     Current exporting: " + blendFile);

            call(["blender", blendFile ,"--background", "--python", "quickExport.py"]);
