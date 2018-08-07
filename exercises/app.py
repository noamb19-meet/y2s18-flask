from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    music=["the paz band","pink floyd","theangelcy"]
    return render_template("index.html",music=music)
 
if __name__ == '__main__':
   app.run(debug = True)