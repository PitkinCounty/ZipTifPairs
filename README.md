# ZipTifPairs
This python script was written to zip up sets of files in a given directory.

## Getting Started
All *.tif and *.tfw files in the Source Directory are grouped by file name and zipped into an archive by the same name.

Pitkin County uses this script for posting to a public downloads directory. This will be run when new imagery is available.

### Installing
Confirm Python is installed.

Download "zippairs.py" into your python root directory, then call from a python command line.

## Usage
	usage: python zippairs.py [-h] SOURCE
	
	Zip sets of files in the source directory
	
	required arguments:
	  SOURCE      Full directory path
	
	optional arguments:
	  -h, --help	show this help message and exit

### Example 
Below is a screenshot of the example directory. (before executing the script)

![source directory before](ZipTifPairs-Before.PNG)

Next we run the script.

	python zippairs.py  C:\OSGeo4W64\DirZip

The script crawls the source directory and creates a zip file for each name. (as shown below)

![source directory after](ZipTifPairs-After.PNG)

## FAQ
* What happens if this is run twice on the same folder?
  * The zip archives are overwritten
* How are sub-directories handled?
  * Requires testing
* What if there is a *.tif without a *.tfw?
  * The archive will be removed if it doesn't have 2 files
* What if files match by name with other extensions?
  * They are ignored
