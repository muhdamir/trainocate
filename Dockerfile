FROM python

WORKDIR /app
COPY ./ch05 ./

CMD ["ls"]
