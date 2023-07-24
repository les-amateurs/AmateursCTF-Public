FROM denoland/deno:1.35.0

EXPOSE 8000

WORKDIR /app

USER deno

ADD . .
RUN deno cache main.ts

CMD ["run", "--allow-net", "--allow-read", "main.ts"]