from program import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=False)

#Must be 'debug=False' on production