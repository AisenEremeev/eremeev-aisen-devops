FROM python:3.12-slim
WORKDIR /app
COPY app/ ./
RUN python -m unittest discover -s . -p 'test_*.py' && useradd --uid 10001 --create-home student
ENV PYTHONUNBUFFERED=1
USER student
EXPOSE 8000
CMD ["python", "main.py"]
