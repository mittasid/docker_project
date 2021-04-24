FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

EXPOSE 5000
