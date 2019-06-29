FROM alpine:3.9
RUN apk add --update python3 py3-pip
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY app.py /src
COPY config.py /src
COPY api /src/api
CMD python3 /src/app.py
