dockerfile_content = """FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "bot.py"]
"""

with open("Dockerfile", "wb") as f:
    f.write(dockerfile_content.replace("\r\n", "\n").encode("utf-8"))

print("Dockerfile written with LF line endings successfully.")
