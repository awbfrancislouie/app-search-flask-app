from flask import Flask, render_template, request     
from elastic_app_search import Client
import json

app = Flask(__name__)

client = Client(
    base_endpoint=config['appsearch']['base_endpoint'],
    api_key=config['appsearch']['api_key'],
    use_https=True)

engine_name = config['appsearch']['engine_name']

@app.route("/")
def home():
    return render_template("home.html")
     
@app.route("/index")
def index():
    # Opening JSON file 
    f = open('data.json',) 

    # returns JSON object as  
    # a dictionary 
    documents = json.load(f)
    data = client.index_documents(engine_name, documents)
    return render_template("about.html" , data=data)
    
if __name__ == "__main__":
    app.run(debug=False)