FROM python:3.8-alpine
COPY . ./app
RUN apk update && pip install -r app/requirements.txt --no-cache-dir
EXPOSE 8100
CMD ["python", "./app/web_app.py"]
