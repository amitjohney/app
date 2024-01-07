FROM ubuntu
RUN apt-get update -y && apt-get install curl -y
WORKDIR  /app
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]