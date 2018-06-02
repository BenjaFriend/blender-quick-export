# blender-quick-export
This will be a script that will take a directory of blender files, and export them as FBX files.
It takes a `-o` argument for where to output the file. If left blank the default is the current directory.

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


```
usage: batchExport.py [-h] [-o OUTPUT] [-d MODELSDIR]

Run this script with python: python batchExport.py -- [options]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory of the export. (Default is the
                        current direectory)
  -d MODELSDIR, --modelsdir MODELSDIR
                        Directory of the files to export. (Default is the
                        current directory)
```

## `importObjs.py`

This script will take a direectory of `.obj` files, and save them all as blender files.
This is useful if you are downloading assets from somewhere, but they don't have the
source files with them. Now you can edit your models however you need to, and then
use the bath export script above to export them to FBX.

Here is the useage of the script:

```
usage: blender [-h] [-o OUTPUT] [-d OBJDIR]

Run blender in background mode with this script:
blender --background --python importObjs.py -- [options]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output dir for the blender files. Default is the
                        current directoy
  -d OBJDIR, --objdir OBJDIR
                        The directoy with the .OBJ files in it. Default is the
                        current directoy

```
