from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
        <meta charset="UTF-8">
        <title>Painéis com Curiosidades</title>
        <style>
            body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
            margin: 0;
            }

            h1 {
            text-align: center;
            margin-bottom: 30px;
            }

            .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            }

            .card {
            aspect-ratio: 1 / 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 18px;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }

            /* Cores individuais */
            .c1 { background-color: #ff6b6b; }
            .c2 { background-color: #6bc1ff; }
            .c3 { background-color: #51d88a; }
            .c4 { background-color: #f7c948; }
            .c5 { background-color: #a78bfa; }
            .c6 { background-color: #fd9644; }
            .c7 { background-color: #20c997; }
            .c8 { background-color: #845ef7; }
            .c9 { background-color: #f66d9b; }

            @media (max-width: 768px) {
            .grid {
                grid-columns: repeat(2, 1fr);
            }
            }

            @media (max-width: 500px) {
            .grid {
                grid-columns: 1fr;
            }
            }
        </style>
        </head>
        <body>

        <h1>Curiosidades em Números</h1>

        <div class="grid">
        <div class="card c1">
            🌎 A Terra viaja<br>**107.000 km/h** pelo espaço
        </div>
        <div class="card c2">
            💧 O corpo humano é composto por<br>**60% de água**
        </div>
        <div class="card c3">
            🧠 O cérebro humano tem cerca de<br>**86 bilhões de neurônios**
        </div>
        <div class="card c4">
            📚 A Biblioteca do Congresso dos EUA tem<br>**mais de 170 milhões de itens**
        </div>
        <div class="card c5">
            🌡️ A maior temperatura registrada na Terra foi<br>**56,7°C** (Califórnia, 1913)
        </div>
        <div class="card c6">
            🐝 Abelhas visitam até<br>**5.000 flores por dia**
        </div>
        <div class="card c7">
            ⏱️ Um piscar de olhos dura cerca de<br>**0,1 segundo**
        </div>
        <div class="card c8">
            🌌 A luz do Sol leva<br>**8 minutos** para chegar à Terra
        </div>
        <div class="card c9">
            📱 Em média, checamos o celular<br>**96 vezes por dia**
        </div>
        </div>

        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)