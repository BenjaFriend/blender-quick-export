## This purpose of this script is to import all .obj files from a directory,
## and save them as .blend files. This is useful if you are, for example, downloading
## assets off of Google poly, and want to edit the meshess or export it to a different
## format.

import os;
import bpy;
import sys;
import argparse;

parser = argparse.ArgumentParser();
parser.parse_args();

#print("\n\n++++++++++++++++\n");
#    print(argv);
#print("\n++++++++++++++++\n\n");


# Select all and delete, so that we have gauranteee a clean scene
def deleteAll():
    bpy.ops.object.select_all(action='DESELECT');
    bpy.ops.object.select_all(action='SELECT');
    bpy.ops.object.delete();

# Path to the object files
full_path_to_directory = os.path.join(os.getcwd(), 'obj');

# Get the list of files in this directory
file_list = os.listdir(full_path_to_directory);

# reduce the list to files ending in 'obj' using 'list comprehensions'
obj_list = [item for item in file_list if item[-3:] == 'obj'];

# loop through the strings in obj_list
for item in obj_list:
    deleteAll();
    full_path_to_file = os.path.join(full_path_to_directory, item);
    blend_file_name = os.path.splitext(full_path_to_file)[0];
    bpy.ops.import_scene.obj(filepath=full_path_to_file);
    print ("=============== Import object ====================");
    # Save as new file
    blend_file_name = blend_file_name + '.blend';
    print("-----------" + blend_file_name + '.blend');

    bpy.ops.wm.save_as_mainfile(filepath=blend_file_name);
    print ("+++++++++++ Saved file +++++++++++ " + blend_file_name + '.blend');
