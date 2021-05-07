FROM python:3.9

ADD . /bnbexplorer-backend/

WORKDIR /bnbexplorer-backend

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "server"]