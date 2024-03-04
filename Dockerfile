FROM python:3.11

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=myproject.settings

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
