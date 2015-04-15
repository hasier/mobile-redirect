__author__ = 'hasier'

from app import app

SERVER_NAME = "0.0.0.0"
SERVER_PORT = 8080

if __name__ == "__main__":
    app.run(SERVER_NAME, SERVER_PORT, debug=True)