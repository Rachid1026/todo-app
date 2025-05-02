# Use the official lightweight Python image.
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from current directory to /app in the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
