FROM python:3

WORKDIR /usr/src/app/
COPY 'main.py' /usr/src/app/
COPY 'requirements.txt' /usr/src/app/
RUN mkdir -p /usr/src/app/resources/

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ Europe/Kiev

EXPOSE 8010

CMD ["python", "main.py"]