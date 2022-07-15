from flask import Flask
import sys
import random
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)



@app.route('/')
def main():
     
    ans = True

    while ans:
        question = print("Ask the magic 8 ball a question: (Ask question verbally) ")
        
        answers = random.randint(1,8)
        
        if answers == 1:
            return "It is certain"
        
        elif answers == 2:
            return "Outlook good"
        
        elif answers == 3:
            return "You may rely on it"
        
        elif answers == 4:
            return "Ask again later"
        
        elif answers == 5:
            return "Concentrate and ask again"
        
        elif answers == 6:
            return "Reply hazy, try again"
        
        elif answers == 7:
            return "My reply is no"
        
        elif answers == 8:
            return "My sources say no"
        else:
            return "broken"
        



@app.route("/health")
def health():
    return "Healthy"

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
