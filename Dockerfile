FROM python:3.12-alpine

WORKDIR /app

# Create a non root user for security
RUN addgroup -S app && adduser -S app -G app

# Copy requirements first
# the dependency layer stays cached as long as requirements.txt does not change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source code last
COPY app.py .

# Do not run as root
USER app

EXPOSE 5000

# run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
