#!/usr/bin/env python3

import connexion
import os
from server import encoder
from flask_cors import CORS
import sqlite3
from dotenv import load_dotenv

load_dotenv()
env = os.environ

def main():
    con = sqlite3.connect(str(env.get('DB_PATH', 'database/bnbexplorer.sqlite')))
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'NYC AirBnB Explorer'}, pythonic_params=True)
    CORS(app.app)
    app.run(port=int(env.get('PORT', 8080)), debug=bool(env.get('DEBUG', False)))


if __name__ == '__main__':
    main()
