# Released 11/12/2018 at 2pm

# importing required modules 
import zipfile
from zipfile import ZipFile 
import os 
from os.path import basename
import sys 
  
def main(directory): 
    # initializing empty file paths list 
    file_paths = [] 
    zips = {  }
    
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
        
            # We only care if the file is .tif or .tfw
            if filename.endswith('.tif') or filename.endswith('.tfw'):
            
                # build the zip path (common for files with the same basename) 
                zipname = os.path.join(root, filename.replace('.tif','').replace('.tfw','') + '.zip')
                
                #build the filepath for this file
                filepath = os.path.join(root, filename) 
                
                # if we do not have an archive by this name, then create one
                if not zipname in zips:
                    zips[zipname] = ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED, True)
                
                # add this file to the archive
                zips[zipname].write(filepath, basename(filepath))
                
                # print a log of the archive path and file path
                print('[' + zipname + '] src: ' + filepath )
                
            # print a log that we are ignoring this file
            else:
                print('ignoring: ' + filename)
    
    # loop through each zip, validate contents, and close the archive file
    for z in zips:
        count = len(zips[z].infolist())
        zips[z].close()
        
        # we should only have 2 files in a valid archive
        if (count == 2):
            print('closing: ' + z)
            zips[z].printdir()
        # if archive is invalid, delete the zip file
        else:
            print('invalid zip: ' + str(count) + ' files, ' + z)
            os.remove(z)
        
    print('All files zipped successfully!')         
  
# Main Entry Point of Code
if __name__ == "__main__": 
    # default value for directory
    dir = 'NO DIRECTORY PROVIDED'
    
    # check that we received an argument
    if len(sys.argv) > 1:
        if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
            print('ZipPairs.py HELP:')
            print('  Zip sets of files in the source directory')
            print('')
            print('  usage: python zippairs.py SOURCE')
            print('    SOURCE\t*Required*\tFull directory path')
            print('    -h, --help\t Optional\tshow this help message and exit')
            print
            
        else:
            # set variable with directory argument
            dir = sys.argv[1]
            
            # we could validate that the directory exists?
            
            # log the directory provided
            print("Source Directory: " + dir)
            print('')
            
            #call the main method
            main(dir) 
    else:
        print(dir)