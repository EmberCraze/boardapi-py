FROM python:3.10

RUN export PYTHONPATH=$PWD

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /usr/lib/app

COPY ./boardapi ./boardapi

CMD ["uvicorn", "boardapi.main:app", "--reload", "--host", "0.0.0.0", "--port", "8022"]
