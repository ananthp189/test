
import requests
import pandas as pd
import json
import pyodbc
#Test
#Initialization
from flask import Flask
from flask import request
import webbrowser


app = Flask(__name__)
@app.route('/',methods=["POST","GET"])
def insights():
    domain= request.args.get('url')
    return domain
    
app.run()
