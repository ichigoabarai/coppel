FROM ubuntu:20.04

RUN apt update
RUN apt install python3-pip -y
RUN python3 --version
RUN pip3 --version

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip3 install pymongo[srv]
CMD ["python3", "app.py"]

