#!/usr/bin/env python3

import os,sys
from datetime import date

arg = str(sys.argv)

if len(sys.argv) == 0 or len(sys.argv) == 1 or len(sys.argv) > 2: 
    print ("Attenzione, passare il path della cartella")
    exit()

path = sys.argv[1]

if ( os.path.isdir(path) ):
    
    if ( not os.path.isdir(path+"/log") ):
        os.mkdir(path+"/log")
    
    file_log = open(path+"/log/log.txt","a") 

    arr = os.listdir(path)

    dir_without_ext = "unknown"

    for file in arr: 
        file_name,file_extension = os.path.splitext(file)
        if ( os.path.isfile(path+"/"+file) ):
            if ( not file_extension ):
                if ( not os.path.isdir(path+"/"+dir_without_ext) ):
                    os.mkdir(path+"/"+dir_without_ext)
                os.rename(path+"/"+file,path+"/"+dir_without_ext+"/"+file)    
                file_log.write("Il file: "+file+" è stato spostato in -> "+path+"/"+dir_without_ext+"\n")
            else:
                if ( not os.path.isdir(path+"/"+file_extension[1:]) ):
                    os.mkdir(path+"/"+file_extension[1:])
                os.rename(path+"/"+file,path+"/"+file_extension[1:]+"/"+file)
                file_log.write("Il file: "+file+" è stato spostato in -> "+path+"/"+file_extension[1:]+"\n")
    file_log.close(); 
else:
    print ("Attenzione, la directory non è valida")

