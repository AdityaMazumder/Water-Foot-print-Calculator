from flask import Flask, request, render_template
import subprocess

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('instructions.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     input1 = request.form['input1']
#     input2 = request.form['input2']
    
#     # Call the C++ program with input values
#     result = subprocess.run(['./calculator', input1, input2], stdout=subprocess.PIPE)
#     output = result.stdout.decode('utf-8')
    
#     return render_template('result.html', result=output)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('instructio.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input1 = request.form['input1']
    input2 = request.form['input2']
    
    # Call the C++ program with input values
    result = subprocess.run(['./calculator', input1, input2], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    return render_template('result.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('instructio.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input1 = request.form['input1']
    input2 = request.form['input2']
    
    # Call the C++ program with input values
    result = subprocess.run(['./calculator', input1, input2], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    return render_template('reslt.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)


def calculate():
    input1 = request.form['input1']
    input2 = request.form['input2']

def calculate():
    input1 = request.form['input1']
    input2 = request.form['input2']


    # Call the C++ program with input values
    result = subprocess.run(['./calculator', input1, input2], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    return render_template('reslt.html', result=output)


