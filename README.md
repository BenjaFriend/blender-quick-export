# blender-quick-export
This will be a script that will take a directory of blender files, and export them as FBX files.


## `quickexport.py`

This script can be used on it's own to export a single `.blend` to a `.fbx` file.
Why make two different scripts instead of just one? Well, it is sometimes easier
for me to just do one file at a time, or maybe you don't need to do an entire directory
of files yet.

## `batchExport.py`

This script will go through the specified directory and look for any `.blend` files.
For each file, it will call the `quickExport.py` script through blender for it, thus exporting
it as an FBX file.

This script requires `quickExport.py` to be in the same directory as it.
