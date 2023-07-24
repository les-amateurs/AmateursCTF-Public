FROM node:20-bullseye-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
    libxkbcommon0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 \
    libasound2 libxshmfence1 libx11-xcb1


WORKDIR /app
COPY .puppeteerrc.cjs package.json package-lock.json ./
RUN npm i

ENV FLAG 'amateursCTF{s@nit1zer_ap1_pr3tty_go0d_but_not_p3rf3ct}'

COPY index.js index.html ./
COPY views/ ./views/

USER node

CMD [ "node", "index.js" ]