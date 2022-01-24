FROM python
RUN pip install flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY run_app.py /home/myapp/
EXPOSE 8000
CMD python3 /home/myapp/run_app.py
