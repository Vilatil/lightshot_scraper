import requests

picture = requests.get("https://i.imgur.com/oegZSot.png").content
with open('image_name.png', 'wb') as handler:
    handler.write(picture)
