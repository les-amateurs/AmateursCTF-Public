FROM php:8.3-alpine

WORKDIR /app

COPY index.php /app
# also copy and host the static folder
COPY static /app/static
# use no one as the user to enhance security

USER nobody:nogroup

EXPOSE 4000

ENTRYPOINT ["php", "-S", "0.0.0.0:4000", "-t", "/app"]