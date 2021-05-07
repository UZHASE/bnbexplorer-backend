FROM python:3.9-slim

ADD . /bnbexplorer-backend/

WORKDIR /bnbexplorer-backend

RUN pip3 install --quiet --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "server"]