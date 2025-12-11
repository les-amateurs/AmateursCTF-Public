FROM node:24-alpine

RUN apk add --no-cache chromium iptables

WORKDIR /app
COPY package.json ./

ENV PUPPETEER_SKIP_DOWNLOAD=true
RUN npm i

COPY index.mjs ./
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
