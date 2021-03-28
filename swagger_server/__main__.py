#!/usr/bin/env python3

import connexion
import os
from swagger_server import encoder
from flask_cors import CORS


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'NYC AirBnB Explorer'})
    CORS(app.app)
    app.run(port=int(os.environ.get('PORT', 8080)))


if __name__ == '__main__':
    main()
