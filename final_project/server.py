import json
from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/englishToFrench")
def English_To_French():
    textToTranslate = request.args.get('textToTranslate')
    French_Translation_Text = translator.English_To_French(textToTranslate)
    return  French_Translation_Text

@app.route("/frenchToEnglish")
def French_To_English():
    textToTranslate = request.args.get('textToTranslate')
    English_Translation_Text = translator.French_To_English(textToTranslate)
    return English_Translation_Text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('/home/project/xzceb-flask_eng_fr/final_project/templates/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
