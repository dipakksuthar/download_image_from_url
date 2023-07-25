# Updated by Github
import urllib
import os
import sys
if len(sys.argv)>1: #Check for arguments for url list file
    f = open(sys.argv[1],'r')
    i = 0
    for line in f:
        i = i + 1
        file_name = str(line).split('/')[-1]
        download_dir = '/home/software/Desktop/'#Set default download path for local machine
        if os.path.exists(download_dir+str(file_name)) :
            f_name = file_name[:str(file_name).rfind('.')]
            f_ext = file_name[str(file_name).rfind('.'):]#Added logic if both file name are same.
            file_name = f_name + '_'+str(i) + f_ext
        img = open(download_dir+str(file_name),'wb')
        try:
            img.write(urllib.urlopen(line).read()) # Download image from url and write into local file.
        except:
            print "Url is not supported..."
        img.close()
    f.close()
else:
    print "Please add file path in command line..."
