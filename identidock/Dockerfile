FROM python:latest

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
# deps should go to requirements.txt
RUN pip install Flask uWSGI requests redis
COPY app /app
COPY cmd.sh /
RUN chmod +x /cmd.sh

EXPOSE 9090 9191

# prevent CMD|ENTRYPOINT from running as root account
USER uwsgi

WORKDIR /app
CMD ["/cmd.sh"]