#!/bin/python3
import os
import cgi
import html

s = os.environ['QUERY_STRING']
form = cgi.FieldStorage()

print("Content-type: text/html")
print("")

print('<html><head><meta charset="UTF-8"></head><body>')


print('<h1>Обработка формы. Так делать нельзя!</h1>')
print(f" {html.escape(form.getfirst('name'))} ")

print("</body></html>")
