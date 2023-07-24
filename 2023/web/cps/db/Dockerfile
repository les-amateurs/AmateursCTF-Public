FROM mariadb:11.0.2

COPY init/* /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=aa9317c870bb056414951fcb6b3ef2236dca50a2d9cc85c79e1db90f5bd39590
CMD ["mariadbd"]