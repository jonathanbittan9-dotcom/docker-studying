FROM python:3.14-slim
WORKDIR /lapis 
COPY ..
RUN pip install discord.py
RUN pip install deepagents
RUN pip install pandas
RUN pip install colorlog 
CMD ["python" "-m" "bot.main"]