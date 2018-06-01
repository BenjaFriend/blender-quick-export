## this script will import an obj file and then save it as a Blender file.

import os
import bpy

# Select all and delete, so that we have gauranteee a clean scene
def deleteAll():
    bpy.ops.object.select_all(action='DESELECT');
    bpy.ops.object.select_all(action='SELECT');
    bpy.ops.object.delete();

# Path to the object files
full_path_to_directory = os.path.join(os.getcwd(), 'obj');

file_list = os.listdir(full_path_to_directory);

# reduce the list to files ending in 'obj'
# using 'list comprehensions'
obj_list = [item for item in file_list if item[-3:] == 'obj']



# loop through the strings in obj_list.
for item in obj_list:
    deleteAll();
    full_path_to_file = os.path.join(full_path_to_directory, item);
    bpy.ops.import_scene.obj(filepath=full_path_to_file);
    # Save as new file
    #bpy.ops.save_as_mainfile(full_path_to_file + '.blend');
