FROM python:3.10-slim
WORKDIR /app/rekruto
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 8080
ENV TZ Europe/Moscow
CMD ["python", "app.py"]

