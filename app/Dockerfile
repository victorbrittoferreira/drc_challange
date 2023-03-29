# version args
ARG base=python
ARG tag=3.11.1-alpine

# pull official base image
FROM $base:$tag

# labeling
ARG base
ARG tag
LABEL baseimage=$base:$tag
LABEL maintainer=victorbrittoferreira@gmail.com

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the appropriate directories
WORKDIR /paint_mall_service

# install dependencies
COPY requirements.txt requirements.txt
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# exposed port
EXPOSE 5000

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "5000", "--workers", "1", "--timeout-keep-alive", "0", "--log-level", "info" ,"run:api" ]
