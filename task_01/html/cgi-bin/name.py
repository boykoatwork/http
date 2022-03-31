#!/bin/python3
import os

print("Content-type: text/html")
print("")

print('<html><head><meta charset="UTF-8"></head><body>')

q = ''
for key in os.environ:
    if key == "QUERY_STRING":
        print(f" <b>{key}</b> : {os.environ[key]} <br/>")
        q = os.environ[key]
        
        
print(f'Ваше имя: {q.replace("name=","")}')


print("</body></html>")
