FROM python:3.10.7-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update &&\
    apt-get install -y curl &&\
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - &&\
    apt-get install -y nodejs

RUN npm install -g nodemon

COPY . .

# Run using nodemon for development
# Need to use --legacy-watch because Docker running in WSL does not trigger file change notifications
# Open issue here: https://github.com/microsoft/WSL/issues/4739
CMD ["nodemon", "--legacy-watch", "--watch", "*.py", "--exec", "python", "-u", "Server.py"]
