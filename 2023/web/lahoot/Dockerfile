FROM node:16
COPY ./* /home/node/app/
COPY ./public/* /home/node/app/public/
COPY ./flavor/* /home/node/app/flavor/
WORKDIR /home/node/app
# engine fix or something
RUN npm uninstall friendly-words
RUN npm install
RUN npm install --force friendly-words
ENV PORT=8081
RUN chown -R node:node /home/node/app
USER node
CMD ["bash", "launch.sh"]
EXPOSE 8081