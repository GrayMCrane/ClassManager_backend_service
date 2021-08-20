FROM python:3.9 AS BASE-PY39-ALPINE310

LABEL maintainer="Canpoint Primary Team<jiangshouming@canpoint.cn>"

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn -i https://pypi.douban.com/simple

COPY ./scripts//start.sh /start.sh
RUN chmod +x /start.sh

COPY ./scripts/gunicorn_conf.py /gunicorn_conf.py

COPY ./scripts/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

WORKDIR /app

COPY app/requirements.txt /app/
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple

#COPY ./app /app
#WORKDIR /app/
#
#ENV PYTHONPATH=/app
#
#EXPOSE 80
#
## Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
## And then will start Gunicorn with Uvicorn
#CMD ["/start.sh"]

FROM BASE-PY39-ALPINE310 AS BACKEND

COPY ./app /app

ENV PYTHONPATH=/app

EXPOSE 80

CMD ["/start.sh"]

FROM BASE-PY39-ALPINE310 AS CELERYWORKER

COPY ./app /app
ENV PYTHONPATH=/app

CMD ["/start.sh"]