FROM python:3.12.0-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry 

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8010
CMD ["python","fastapi","run", "app/app/main.py","--port 8010"]