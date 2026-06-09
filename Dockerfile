FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    discord.py>=2.4.0 \
    aiohttp>=3.13.5

COPY yf_bot.py .

RUN useradd -m -u 1000 botuser && chown -R botuser:botuser /app
USER botuser

CMD ["python", "yf_bot.py"]
