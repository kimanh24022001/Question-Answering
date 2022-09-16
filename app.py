from flask import Flask, render_template,request, redirect, url_for
import PyPDF2
import os
from transformers import AutoTokenizer,AutoModelForQuestionAnswering,pipeline
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        context = request.form.get("para")
        question = request.form.get("qa")
        # Make predictions with the model
        tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
        model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
        question_answerer = pipeline("question-answering", model = model, tokenizer= tokenizer)
        return render_template('index.html',qa=question,para=context,message=question_answerer(question=question, context = context)['answer'])
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
    
