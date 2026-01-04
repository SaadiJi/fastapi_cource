FROM python:3.11.14
WORKDIR /usr/src/app
COPY requirements.txt ./ 
#(/usr/src/app)

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "fastapi", "dev","app/main.py", "--host", "0.0.0.0", "--port", "8000" ]

#13.48