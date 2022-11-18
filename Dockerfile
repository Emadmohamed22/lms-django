# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8000

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
