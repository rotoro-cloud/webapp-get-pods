# Simple Web Application Get PODs

This simple web application using [Python Flask](http://flask.pocoo.org/) use for education purposes.
  
  There are the steps required to get it working on linux.
  
  - Установи зависимости ОС
  - Установи зависимости приложения
  - Разверни исходный код приложения
  - Запусти веб-сервер
   
## 1. Install OS dependencies

    apt-get install -y python3 python3-pip


## 2. Install app dependencies

    pip3 install -r requirements.txt

## 3. Deploy the app source code

  Copy source to /opt dir

    cp app.py /opt

## 4. Start the webserver

Start web command

    FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
    
## 6. Test

Open a browser and try URL

    http://<IP>:8080                        => Hello!
