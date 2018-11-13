# ZipTifPairs
This python script was written to zip up sets of files in a given directory.

## Getting Started
This script was designed to run with OSGeo4W64 installed.
"SourceDirectory" is a required parameter.
All *.tif and *.tfw files in the Source Directory are grouped by file name and zipped into an archive by the same name.

### Installing
Copy "zippairs.py" into your OSGeo4W64 folder, then launch the OSGeo4W64 batch file. It can be run from that command line.

### Example: 
"python  zippairs.py  C:\OSGeo4W64\DirZip"
This crawls the source directory and creates 3 zip files.

## Notes


### Questions
What happens if this is run twice on the same folder?
How are sub-directories handled?
What if there is a *.tif without a *.tfw?
What if files match by name with other extensions? (They are ignored)
