#!/usr/bin/python
import requests
import shutil


url_img_json = "https://picsum.photos/v2/list"

response = requests.get(url_img_json)

if response.ok: 
    json_data = response.json()
    for key in json_data: 
        download_url = key['download_url']
        id_image = key['id']
        image_url = requests.get(download_url,stream = True)
        image_url.raw.decode_content = True
        
        with open(id_image+".jpg",'wb') as f: 
            shutil.copyfileobj(image_url.raw,f)   
else: 
    print ("Errore")

#print (url_img_json)