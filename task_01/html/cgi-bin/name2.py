#!/bin/python3
import os
import cgi
import html
import datetime

s = os.environ['QUERY_STRING']
form = cgi.FieldStorage()

print("Content-type: text/html")
print("Set-Cookie: test_cookie=test")
print(f"Set-Cookie: date_of_last_visit={datetime.datetime.now().isoformat()}")
print("")

print('<html><head><meta charset="UTF-8"></head><body>')


print('<h1>Обработка формы. Так делать нельзя!</h1>')
print(f" {html.escape(form.getfirst('name'))} ")

print("</body></html>")
