# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Tell the container to listen on port 8000
EXPOSE 8000

# Command to run the app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]