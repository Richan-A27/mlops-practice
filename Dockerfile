FROM python:3.10-slim 

WORKDIR /app

COPY requirments.txt .
RUN pip install -r requirments

COPY . .

CMD ["python","app.py"]

