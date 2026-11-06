FROM python:3.14-slim
WORKDIR /app
COPY requirments.txt .
RUN pip install --n-cach-dir -r req
COPY . .
CMD ["python" , "-m" , "src.main"]


