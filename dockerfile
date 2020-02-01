FROM conda/miniconda3
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN conda install --file requirements.txt
COPY . .
CMD ["flask", "run"]



