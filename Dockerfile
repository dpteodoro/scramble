FROM python:3.9.12-slim-bullseye

RUN apt-get update
RUN addgroup --system --group reader && adduser --no-create-home --system --shell /bin/false --group reader

WORKDIR /app
COPY scramble/ scramble/

RUN chown -R reader:reader /app
USER reader

CMD ["python3", "scramble/src/main.py"]