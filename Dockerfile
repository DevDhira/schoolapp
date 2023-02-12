FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
#RUN python -m venv env && source ./env/bin/activate && pip install -r requirements.txt

RUN /bin/bash -c "python -m pip install virtualenv && python -m venv env && chmod +x ./env/bin/activate && ./env/bin/activate  && pip install -r requirements.txt && pip freeze"

COPY . /code/

