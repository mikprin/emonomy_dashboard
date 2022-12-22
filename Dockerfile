FROM python:3.9-slim

LABEL name="emonomy dashboard" \
      version="1.0" \
      maintainer="Mikhail Solovyanov <" \
      description="This is the Dockerfile for emonomy dashboard Streamlit app"

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/* &&\
    apt-get clean

COPY emonomy_dashboard/streamlit_app /app

COPY requirements.txt /app

# Temp

COPY example_data /example_data

RUN pip3 install -r requirements.txt

CMD ["streamlit", "run", "dashboard_app.py", "--server.port=8501", "--server.address=0.0.0.0"]