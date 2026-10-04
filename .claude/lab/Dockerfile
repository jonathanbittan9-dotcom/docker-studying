FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install discord.py
RUN pip install colorlog
CMD ["python" , "-m" , "src.main"]
