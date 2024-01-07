FROM alpine:latest
RUN apk update && apk add --no-cache curl
COPY entrypoint.sh .
ENTRYPOINT ["/entrypoint.sh"]