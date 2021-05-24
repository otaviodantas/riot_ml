FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN python setup.py install

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

