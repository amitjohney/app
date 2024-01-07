FROM ubuntu
RUN apt-get update -y && apt-get install curl -y
WORKDIR  /app
COPY entrypoint.sh ./entrypoint.sh
RUN cat ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]