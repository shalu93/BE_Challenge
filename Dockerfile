FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV APP_SETTINGS="config.DevelopmentConfig"
ENV DATABASE_URL="postgresql://shaluchandwani:shalu@localhost:5432/users"

CMD ["python","manage.py", "runserver","-h","0.0.0.0","-p","5000"]