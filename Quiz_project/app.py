from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/python_quiz.html')
def pythonquiz():
    return render_template('python_quiz.html')

@app.route('/gk_quiz.html')
def gkquiz():
    return render_template('gk_quiz.html')

@app.route('/python_result', methods=['POST'])
def python_result():
    score = 0

    # correct answers
    answers = {
                "Q1": "Gudio Van Rossum",
                "Q2": "Variable"
              }

    for key in answers:
        user_answer = request.form.get(key)
        if user_answer == answers[key]:
            score += 1

    total = len(answers)
    return render_template('result.html', score=score, total=total,quiz_name="Python Quiz")

@app.route('/gk_result',methods=['POST'])
def gk_result():
    score=0
    answers={
              "P1": "Nile River",
              "P2": "Mars"
            }

    for key in answers:
        user_answer1= request.form.get(key)
        if user_answer1== answers[key]:
            score += 1
    total =len(answers)
    return render_template('result.html',score=score,total=total,quiz_name="GK Quiz")
       
if __name__ == '__main__':
    app.run(debug=True)
