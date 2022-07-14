from flask import Flask
import sys
import random
app = Flask(__name__)


@app.route('/')
def magic_ball():

    ans = True

    while ans:
        question = input("Ask the magic 8 ball a question: (press enter to quit) ")
        
        answers = random.randint(1,8)
        
        if question == "":
            sys.exit()
        
        elif answers == 1:
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

if __name__ == "__main__":
    app.run()