# Blender/Python quick export as FBX!

# This is a script that go through all blender files in a certain
# directoy, and export them as .FBX files.

# The command below is how to run a python script in blender without actually
# having to open the blender GUI
# blender myscene.blend --background --python myscript.py

import bpy
import os

blend_file_path = bpy.data.filepath
directory = os.path.dirname(blend_file_path)
target_file = os.path.join(directory, 'test_file.fbx')

bpy.ops.export_scene.fbx(filepath=target_file)
