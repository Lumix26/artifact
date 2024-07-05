FROM python

WORKDIR /artifact

COPY ./app /artifact/app

COPY ./data /artifact/data

EXPOSE 5000

RUN pip install flask

RUN pip install ollama

CMD ["python", "app/app.py"]