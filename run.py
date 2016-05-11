import os

from asana_ticket_maker.app import app


def main():
    if os.getenv('APP_ENV') == 'debug':
        app.run(debug=True)
        app.testing = True
    else:
        app.run()


if __name__ == '__main__':
    main()

