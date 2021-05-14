FROM python:3.9-slim

ADD . /bnbexplorer-backend/

WORKDIR /bnbexplorer-backend

RUN apt-get update && apt-get install python3-sphinx -y && apt-get install git

RUN pip3 install --quiet --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "server"]