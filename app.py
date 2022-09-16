from flask import Flask, render_template,request, redirect, url_for
import PyPDF2
import os
from transformers import AutoTokenizer,TFAutoModelForQuestionAnswering,pipeline
app = Flask(__name__)
app.config['SECRET_KEY']='supersecretkey'
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])

def home():
    
    if request.method=="POST":
        f = request.files['File'] 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        pdfFileObj = open(os.path.join(app.config['UPLOAD_FOLDER'], f.filename), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        extract = pageObj.extractText()
        if len(str(request.form.get("para")))>4:
            tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
            model = TFAutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
            question_answerer = pipeline("question-answering", model = model, tokenizer= tokenizer)
            return render_template('index_document.html',note='See the results. You want it?  ',qa=extract,para=request.form.get("para"),message=question_answerer(question=extract, context = request.form.get("para"))['answer'])
        else:
            return render_template('index_document.html',note='Please upload for question',para=extract)
    return render_template('index_document.html',note='Please upload for paragraph')
if __name__=="__main__":
    app.run(debug=True)
    
