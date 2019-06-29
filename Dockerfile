FROM alpine:3.9
RUN apk add --update python3 py3-pip postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY *.py /src
COPY config.py /src
COPY manage.py /src
COPY models.py /src
COPY api /src/api
COPY routes /src/routes
CMD python3 /src/app.py
