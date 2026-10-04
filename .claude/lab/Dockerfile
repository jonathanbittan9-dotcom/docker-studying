FROM python:3.12-slim
WORKDIR /app
RUN pip install colorlog
RUN pip install discord.py
COPY . .
CMD ["python" , "-m" , "src.main"]
