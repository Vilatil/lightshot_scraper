import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get("https://i.imgur.com/oegZSot.png", headers=headers)
if response.status_code != 200:
    print("Failed to download image!")
    exit()

with open("bla.png", 'wb') as file:
    file.write(response.content)

print("Image downloaded successfully!")
