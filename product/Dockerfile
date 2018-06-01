FROM python:3-onbuild

RUN pip install psycopg2-binary

COPY . /usr/src/app

CMD ["python", "api.py"]