FROM python:3.8.8-alpine3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
RUN mkdir /webapp
COPY webapp webapp
WORKDIR /webapp
RUN pip install --upgrade pip
COPY requirements.txt /webapp/
RUN pip install -r requirements.txt
COPY . /webapp/
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]