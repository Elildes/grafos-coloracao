import os
import sys
import json
from flask import Flask, render_template, jsonify, request

# --- Configuração de Path ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Importe suas funções de algoritmo
# ----------------------------------------------------
"""
from src.algorithms.prim import prim_mst
from src.algorithms.bellman_ford import bellman_ford 
from src.algorithms.floyd_warshall import floyd_warshall
from src.dot_parser import parse_dot
"""

app = Flask(__name__)

@app.route('/')
def index():
    """Renderiza a página inicial (seleção de algoritmo)."""
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)