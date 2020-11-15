import requests,shutil,getpass,os,time

USER = getpass.getuser()

PATH = "/home/"+USER+"/Immagini/"
API_KEY = "N5rN0JGBmy7_BFuj4AWp4XnouViuP_7QfgP9IIUTa0Q"
URL_KEY = "https://api.unsplash.com/photos/random/?client_id="
OPTION = "&orientation=landscape"
url_api_key = URL_KEY+API_KEY+OPTION


request = requests.get(url_api_key)

if request.status_code == 200: 
    json = request.json()
    url_wall = json['urls']['regular']
    image_url = requests.get(url_wall,stream = True)
    image_url.raw.decode_content = True
    with open(PATH+"wallpaper.jpg",'wb') as f: 
        shutil.copyfileobj(image_url.raw,f)  
    
    os.system("gsettings set org.cinnamon.desktop.background picture-uri file:"+PATH+"wallpaper.jpg")
else:
    print("Warning code: "+request.status_code)    
