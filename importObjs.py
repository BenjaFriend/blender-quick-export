## This purpose of this script is to import all .obj files from a directory,
## and save them as .blend files. This is useful if you are, for example, downloading
## assets off of Google poly, and want to edit the meshess or export it to a different
## format.

import os;
import bpy;
import sys;
import argparse;

# Allows us to print to the terminal in colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Select all and delete, so that we have gauranteee a clean scene
def deleteAll():
    bpy.ops.object.select_all(action='DESELECT');
    bpy.ops.object.select_all(action='SELECT');
    bpy.ops.object.delete();

## Set default values for the location of the object files
def main():
    argv = sys.argv

    if "--" not in argv:
        argv = []; # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1:]; # get all args after "--"

    # When --help or no args are given, print this help
    usage_text = (
    "Run blender in background mode with this script:\n"
    " blender --background --python " + __file__ + " -- [options]"
    );

    parser = argparse.ArgumentParser(description=usage_text);

    parser.add_argument('-o','--output', action='store',
                        type=str, default=os.getcwd(),
                        help='output dir for the blender files. Default is the current directoy');

    parser.add_argument('-d','--objdir', action='store',
                        type=str, default=os.getcwd(),
                        help='The directoy with the .OBJ files in it. Default is the current directoy');


    args = parser.parse_args(argv); # In this example we wont use the args

    # If args don't exist then print help but continue going
    if not argv:
        print(bcolors.WARNING);
        parser.print_help();
        print(bcolors.ENDC);

    path_to_obj_files = args.objdir;
    output_dir = args.output;

    # Get the list of files in this directory
    file_list = os.listdir(path_to_obj_files);

    # reduce the list to files ending in 'obj' using 'list comprehensions'
    obj_list = [item for item in file_list if item[-3:] == 'obj'];

    # loop through the strings in obj_list
    for item in obj_list:
        deleteAll();
        obj_file_path = os.path.join(path_to_obj_files, item);
        # Actually import the object
        bpy.ops.import_scene.obj(filepath=obj_file_path);
        # Remove the old file extension
        output_file_name = os.path.splitext(item)[0];

        # Save as new file
        output_file_name = output_dir + output_file_name + '.blend';
        bpy.ops.wm.save_as_mainfile(filepath=output_file_name);

        print (bcolors.OKGREEN + '     Saved file Success\n      ' + output_file_name + bcolors.ENDC);

#  Entry point for script
if __name__ == '__main__':
    main();
