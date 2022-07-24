FROM python:3.10

COPY ./requirements.txt /src/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src

EXPOSE 8060

WORKDIR src

CMD ["python", "-u", "manage.py", "makemigrations"]
CMD ["python", "-u","manage.py", "migrate"]
CMD ["python", "-u","manage.py", "runserver",  "0.0.0.0:8060"]