FROM debian:latest

RUN apt install -y openssl && \
    mkdir /pyapp && \
    openssl req -x509 -newkey rsa:2048 -keyout /pyapp/key.pem -out /pyapp/cert.pem -days 365

COPY pyapp/http_server.py /pyapp/http_server.py
COPY pyapp/htdocs /pyapp

EXPOSE 4443
CMD python3 /pyapp/http_server.py &
