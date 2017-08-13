FROM python:3.6.2

ADD requirements.txt /survey-processor/
WORKDIR /survey-processor
RUN pip install -r requirements.txt

ADD . /survey-processor
