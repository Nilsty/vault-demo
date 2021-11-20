FROM python:3.8.1-alpine
RUN apk update
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["vault-demo.py"]