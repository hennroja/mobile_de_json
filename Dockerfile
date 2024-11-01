# Use a lightweight Python image as the base
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy   
 the Python script
COPY script.py script.py

# Command to run the script
CMD ["python", "script.py"]
