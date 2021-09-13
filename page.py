from market import app
from tools import cls, system


def run():
	if __name__ == '__main__':
		app.run(host="0.0.0.0", port=8080)

#Checks if the main.py file has executed directly and not imported
try:
	run()

except ImportError:
	run()
	cls()
