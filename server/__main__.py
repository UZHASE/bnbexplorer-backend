#!/usr/bin/env python3

import connexion
import os

from flask_cors import CORS
from server import encoder
from dotenv import load_dotenv
from distutils import util

load_dotenv()
env = os.environ


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'NYC AirBnB Explorer'}, pythonic_params=True)
    CORS(app.app)
    app.run(port=int(env.get('PORT', 8080)), debug=bool(util.strtobool(env.get('DEBUG', 'False'))))


if __name__ == '__main__':
    main()
