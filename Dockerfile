FROM ubuntu

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt-get clean && apt-get update
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y python3 \
    nginx python3-pip && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /checkerboard/flaskapp/

RUN pip3 --no-cache-dir install -r /checkerboard/flaskapp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./src/flaskapp /checkerboard/flaskapp
COPY ./src/static /checkerboard/static
WORKDIR /checkerboard

COPY ./gunicorn.conf.py /checkerboard
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

ENTRYPOINT nginx -g "daemon on;" && gunicorn "flaskapp:create_app()" -c ./gunicorn.conf.py