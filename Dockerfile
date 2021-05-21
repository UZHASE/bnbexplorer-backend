FROM python:3.9-slim

ADD . /bnbexplorer-backend/

WORKDIR /bnbexplorer-backend

RUN apt-get update && apt-get install --yes --no-install-recommends \
    python3-sphinx \
    git \
    build-essential

RUN pip3 install --quiet --no-cache-dir -r requirements.txt

# This is required by sphinx apidoc. Otherwise documentation for test code can't be generated.
RUN pip3 install --quiet --no-cache-dir -r test-requirements.txt

CMD ["python3", "-m", "server"]