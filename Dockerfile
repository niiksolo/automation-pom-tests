FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver \
    libnss3 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--alluredir=reports/allure"]