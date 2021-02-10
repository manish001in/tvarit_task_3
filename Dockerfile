FROM python:2

RUN mkdir /tvarit
WORKDIR /tvarit

COPY requirements.txt ./
RUN pip install -r requirements.txt
ADD tvarit/ /tvarit/

EXPOSE 5000
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]