FROM python:3.10.6
 
WORKDIR /app
COPY . /app
EXPOSE 80
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["/app/main.py"]