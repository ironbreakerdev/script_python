#!/usr/bin/python3
import os,hashlib,sys

dict_file = {}
unique_file = []

if ( len(sys.argv) < 2 ):
    print("Attenzione devi inserire il path da analizzare")
    exit()

if not os.path.exists(sys.argv[1]):
    print("Attenzione, il path inserito non è una directory")
    exit()

path = sys.argv[1]
dir = os.listdir(path)

print("-"*35)
print("All'interno del path: "+path+": ci sono "+str(len(dir))+" files")
for file in dir:    
    with open(path+"/"+file,"rb") as f: 
        bytes = f.read()
        hash = hashlib.md5(bytes).hexdigest()
        dict_file[hash] = file

if str(len(dict_file)) == str(len(dir)):
    print("Di questi non esistono file duplicati")
    exit()
else:
    print("Di questi solo "+str(len(dict_file))+" non hanno duplicati e sono: \n")
    for key,value in dict_file.items(): 
        print(value)

    esito = input("\nVuoi eliminare tutti i file che sono duplicati? [s/n]: ")
    if esito.lower() == 's': 
        for file in os.listdir(path): 
                if file not in dict_file.values():
                    os.remove(path+"/"+file)
    else:
        exit()