FROM node:24-alpine

RUN apk add --no-cache chromium

WORKDIR /app
COPY package.json ./

ENV PUPPETEER_SKIP_DOWNLOAD=true
RUN npm i

COPY index.js /app
EXPOSE 5000

ENTRYPOINT ["node", "index.js"]