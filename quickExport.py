# Blender/Python quick export as FBX!

# This is a standalone script to export a single blender file as an FBX

# To use this script, you can use the following format:
# blender myscene.blend --background --python quickExport.py

import bpy;
import os;

# Allows us to print to the terminal in colors
class bcolors:
    OKGREEN = '\033[92m'

blend_file_path = bpy.data.filepath;

# Get the name of this blender file
blend_file_name = bpy.path.basename(bpy.context.blend_data.filepath);

# Remove the .blend extension and add the .fbx extension
blend_file_name = os.path.splitext(blend_file_name)[0];
fbx_file_name = blend_file_name + '.fbx';

directory = os.path.dirname(blend_file_path);

# The end target is the directoy and the file name of the FBX
target_file = os.path.join(directory, fbx_file_name);

# Actually export the scene as an FBX
bpy.ops.export_scene.fbx(filepath=target_file);
print (bcolors.OKGREEN + "Exported file as FBX:\n     " + target_file);
