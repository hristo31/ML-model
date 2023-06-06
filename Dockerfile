FROM python:3.9

WORKDIR /app

COPY ./Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv uvicorn fastapi joblib scikit-learn
RUN pipenv sync

COPY ./decision_tree_main.py /app/
COPY ./decision_tree.ml /app/

CMD ["pipenv",  "run",  "uvicorn", "decision_tree_main:app", "--host", "0.0.0.0", "--port", "8000"]