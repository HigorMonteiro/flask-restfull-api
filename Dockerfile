FROM python:3.7.4

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry==1.0.3 && \
    poetry export --without-hashes -f requirements.txt -n -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install -r requirements.txt

COPY . /app

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]