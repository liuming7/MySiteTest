from os import environ
from MySiteTest import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5005'))
    except ValueError:
        PORT = 5005
    app.run(HOST, PORT, debug=True)
