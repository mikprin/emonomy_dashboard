FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /app
# COPY ../example_data /example_data
RUN mkdir -p /example_data

CMD ["/bin/bash" , "-c" , "/app/deploy.sh"]
# CMD [ "sleep", "100" ]