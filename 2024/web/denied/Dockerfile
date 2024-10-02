FROM node:21
WORKDIR /usr/app
COPY package*.json ./
RUN npm install
COPY index.js ./
EXPOSE 3000
CMD [ "node", "index.js" ]
