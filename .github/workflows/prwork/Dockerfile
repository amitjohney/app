FROM ubuntu
RUN apt-get update -y && apt-get install curl -y
WORKDIR  /app
ADD entrypoint.sh .
RUN cat ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]