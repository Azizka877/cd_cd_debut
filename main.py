from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.getenv('NAME', 'Mon App')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Ma Super App</title>
    <style>
        body {{ font-family: Arial; text-align: center; margin-top: 50px; }}
        h1 {{ color: #007bff; }}
    </style>
</head>
<body>
    <h1>Bienvenue sur {name} !</h1>
    <p>Déployée via CI/CD sur EKS 🚀</p>
    <p>Date : 2026</p>
</body>
</html>
"""

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)