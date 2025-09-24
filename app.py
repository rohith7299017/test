import os
from flask import Flask, request, render_template_string, redirect, url_for
app = Flask(__name__)


HOME_TEMPLATE = 
'''
<!doctype html>
<html>
<head>
  <title>Simple Polls</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<p>Hello, Cloud!</p>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def home():
  return render_template_string(HOME_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
