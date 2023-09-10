FROM python:3.9

WORKDIR /app

COPY requirement.txt ./requirement.txt

RUN pip install -r requirement.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]