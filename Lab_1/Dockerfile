FROM python:3

COPY requirements.txt .
COPY main.py .
COPY calculator.py .
COPY even_list.py .
COPY say_hello.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
