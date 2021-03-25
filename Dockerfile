FROM python:3.9-alpine

ADD * /bnbexplorer-backend/requirements.txt

WORKDIR /bnbexplorer-backend

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "swagger_server"]