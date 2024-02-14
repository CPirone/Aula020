from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!<br><br><b>Aluno:</b> Cleber Pirone<br><b>Prontuário:</b> PT3008649'

if __name__ == '__main__':
    app.run(debug=True)
