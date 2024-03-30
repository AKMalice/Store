FROM python:3.10

WORKDIR /home/ec2-user/Store/appstore

RUN pip install Django==3.2.17

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
