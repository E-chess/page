from market import app
from tools import cls
import threading


def page():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=8080)


def run():
    page()
    # thread = threading.Thread(target=page)
    # thread.start()


# code
try:
    run()

except ImportError:
    run()
    cls()
