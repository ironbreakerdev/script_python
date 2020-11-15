import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import os

class Logger(FileSystemEventHandler):
    def __init__(self,path): 
        self.path = path
    
    #def monitor(self): 
    
    def on_any_event(self,event): 
        #print(event.event_type)
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Evento creato: "+str(event.src_path))
            path_file_name = str(event.src_path)
            ext = os.path.splitext(path_file_name)[1]
            #print(str(ext))
            file_name = os.path.basename(str(path_file_name))
            if ( str(ext) == "" ): 
                dir_name = "unknown"
            else:
                dir_name = str(ext[1:])
            if ( not os.path.exists(path+"/"+dir_name) ):
                os.mkdir(path+"/"+dir_name)
            time.sleep(0.1)
            os.rename(path+"/"+file_name,path+"/"+dir_name+"/"+file_name)
            
            

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Logger(path)
    #event_handler.monitor()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()