import requests

content = requests.get("http://127.0.0.1:5000/audio")
with open("hello2.mp3", "wb") as f:
    f.write(content.content)