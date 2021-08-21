from market import app
from tools import cls

def run():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=8080)

#Checks if the main.py file has executed directly and not imported
try:
    run()

except ImportError:
    import email_validator
    
    run()
    
    cls()