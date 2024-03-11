# FROM cypress/browsers:latest
# RUN apt-get install python 3 -y
# RUN echo $(python3 -m site --user-base)
# COPY requirements.txt .
# ENV PATH /home/root/.local/bin:${PATH}
# RUN apt-get update && apt-get install -y python3-pip && pip install -r requirements.txt
# COPY ..

# EXPOSE 5000
# # CMD uvicorn main:app --host 0.0.0.0 --port $PORT
# CMD ["flask", "run", "--host", "0.0.0.0"]

FROM selenium/standalone-chrome
# FROM python:3.9
# Download and extract Python source code
RUN wget https://www.python.org/ftp/python/3.9.15/Python-3.9.15.tgz -O python.tgz
RUN tar xzf python.tgz

# Build and install Python
RUN cd Python-3.9.15 && ./configure --enable-optimizations && make -alt install

# Set Python executable path (optional, depends on your application)
RUN ln -s /usr/local/bin/python3.9 /usr/bin/python3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run"]
