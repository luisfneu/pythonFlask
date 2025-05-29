from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt">
        <head>
            <meta charset="UTF-8">
            <title>LNeu POQUI</title>
        </head>
        <body>
            <h1>Bem-vindo!</h1>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)