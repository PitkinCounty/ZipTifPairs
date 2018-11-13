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
            if filename.endswith('.tif') or filename.endswith('.tfw'):
                # join the two strings in order to form the full filepath. 
                zipname = os.path.join(root, filename.replace('.tif','').replace('.tfw','') + '.zip')
                filepath = os.path.join(root, filename) 
                
                if not zipname in zips:
                    zips[zipname] = ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED, True)
                
                zips[zipname].write(filepath, basename(filepath))
                
                print('[' + zipname + '] src: ' + filepath )
                # print('zip: ' + os.path.join(root, zipname))
    
    for z in zips:
        print('closing: ' + z)
        zips[z].close()
        zips[z].printdir()
    print('All files zipped successfully!')         
  
  
if __name__ == "__main__": 
    # print "This is the name of the script: ", sys.argv[0]
    # print "Number of arguments: ", len(sys.argv)
    # print "The arguments are: " , str(sys.argv)
    # print "The directory provided is: " , sys.argv[1]
    
    dir = 'C:\\OSGeo4W64\\DirZip1'
    
    if len(sys.argv) > 1 : dir = sys.argv[1]
    print("Source Directory: " + dir)
    print
    
    #call the main method
    main(dir) 