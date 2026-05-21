from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        file = request.files['resume']
        text = extract_text(file)

        skills = ["python", "java", "c++", "sql", "html", "css"]
        found = [skill for skill in skills if skill in text.lower()]

        result = f"Skills found: {', '.join(found)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)