''' from flask import Flask, render_template,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import AutoTokenizer,AutoModelForQuestionAnswering,pipeline
import nltk
nltk.download('vader_lexicon')
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        context = request.form.get("para")
        question = request.form.get("qa")
        # Make predictions with the model
        tokenizer = AutoTokenizer.from_pretrained("D:\\Python\\code\\QA\\best_model")
        model = AutoModelForQuestionAnswering.from_pretrained("D:\\Python\\code\\QA\\best_model")
        question_answerer = pipeline("question-answering", model = model, tokenizer= tokenizer)
        return render_template('index_document.html',qa=question,para=context,message=question_answerer(question=question, context = context)['answer'])
    return render_template('index_document.html',form=form)
if __name__=="__main__":
    app.run(debug=True)
'''
from flask import Flask, render_template,request, redirect, url_for
import PyPDF2
import os
from transformers import AutoTokenizer,AutoModelForQuestionAnswering,pipeline
app = Flask(__name__)
app.config['SECRET_KEY']='supersecretkey'
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])

def home():
    
    if request.method=="POST":
        f = request.files['File'] 
        
    return render_template('index_document.html',note='Please upload for paragraph')
if __name__=="__main__":
    app.run(debug=True)
