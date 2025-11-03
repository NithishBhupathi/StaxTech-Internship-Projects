#!/usr/bin/env python3
import cgi
import cgitb

# Enable debugging
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

num1 = float(form.getvalue("num1"))
num2 = float(form.getvalue("num2"))
operation = form.getvalue("operation")

result = None

if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"""
<html>
<head><title>Calculation Result</title></head>
<body style='font-family: Arial; text-align:center; margin-top:50px;'>
    <h1>Result: {result}</h1>
    <a href='/index.html'>Back to Calculator</a>
</body>
</html>
""")
