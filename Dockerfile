FROM python:3.9-alpine

ADD heroku /bnbexplorer-backend/

WORKDIR /bnbexplorer-backend

RUN ls -la
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "swagger_server"]