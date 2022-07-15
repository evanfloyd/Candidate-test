# Magic 8 Ball

Provides a response to a yes or no question (must be asked verbally/mentally)

## Installation and use

(Must have docker installed)

- Clone repo
- Navigate into repo
- Run ```docker build -t <image name>```
- Run ```docker run -p 5000:5000 -d magic-8ball```
- Ask your question verbally or mentally and go to ```http://127.0.0.1:5000/```
- Refresh page to receive more answers