from flask import Flask,request, render_template
import codecs
app = Flask(__name__)

@app.route("/")
def bbs():
    message = "hello world"
    file = codecs.open("articles.txt", "r","utf-8")
    lines = file.readlines()
    file.close()
    return render_template("bbs.html",message = message,lines = lines)

@app.route("/result",methods=["POST"])
def result():
    message= "thank you"
    article = request.form["article"]
    name = request.form["name"]
    file = codecs.open("articles.txt", "a","utf-8")
    file.write(article + "," + name+"\n")
    file.close()
    
    return render_template("bbs_result.html",message=message,article = article, name = name)
    

if __name__ == '__main__':
    app.run()