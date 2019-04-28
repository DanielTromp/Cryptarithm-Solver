FROM pypy:3.6-slim

MAINTAINER "Daniël Tromp" <drpgmtromp@gmail.com>

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY decoder.ipynb /app

RUN apt-get update && apt-get install -q -y apt-utils && apt-get upgrade -q -y
RUN apt-get install -q -y build-essential pkg-config  
#	 git vim nano libcurl4-openssl-dev libgmp-dev libjansson-dev libblas-dev \
#    liblapack-dev libpng-dev libfreetype6-dev autogen autoconf automake gfortran

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install prometheus-client==0.5.0 jupyter 
#RUN pip install  --trusted-host pypi.python.org -r requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888

CMD [ "jupyter", "notebook", "--NotebookApp.token=''", "--ip=0.0.0.0", "--allow-root", "--no-browser", "decoder.ipynb" ]

# 
# docker build -t decoder-pypy .
# docker run -p 8888:8888 decoder-pypy
# docker login
# docker tag decoder-pypy danieltromp/decoder-pypy:latest
# docker push danieltromp/decoder-pypy:latest
# optional # docker pull danieltromp/decoder-pypy
# docker run -p 8888:8888 danieltromp/decoder-pypy
#
# docker rmi -f $(docker images -a -q)