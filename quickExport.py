# Blender/Python quick export as FBX!

# This is a standalone script to export a single blender file as an FBX

# To use this script, you can use the following format:
# blender myscene.blend --background --python quickExport.py

import bpy;
import os;
import sys;
import argparse;


# Allows us to print to the terminal in colors
class bcolors:
    OKGREEN = '\033[92m'


## setup the arguments for this script
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
                    help='Output dir of the export. (Default is the current directory)');


args = parser.parse_args(argv); # In this example we wont use the args

# If args don't exist then stop
if not argv:
    print(bcolors.WARNING);
    parser.print_help();
    print(bcolors.ENDC);

output_dir = args.output;


blend_file_path = bpy.data.filepath;

# Get the name of this blender file
blend_file_name = bpy.path.basename(bpy.context.blend_data.filepath);

# Remove the .blend extension and add the .fbx extension
blend_file_name = os.path.splitext(blend_file_name)[0];
fbx_file_name = blend_file_name + '.fbx';

#directory = os.path.dirname(blend_file_path);

# The end target is the directoy and the file name of the FBX
target_file = os.path.join(output_dir, fbx_file_name);

# Actually export the scene as an FBX
bpy.ops.export_scene.fbx(filepath=target_file);
print (bcolors.OKGREEN + "Exported file as FBX:\n     " + target_file + bcolors.ENDC);
