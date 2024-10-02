# tenative idk if this will work
FROM python:3.11
WORKDIR /usr/app
COPY ./* /usr/app/
COPY ./templates/* /usr/app/templates/
COPY ./static/* /usr/app/static/
COPY ./question_sets/* /usr/app/question_sets/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "bash", "run_prod.sh" ]