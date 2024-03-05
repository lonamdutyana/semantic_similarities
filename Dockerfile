# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy and its English model
RUN python -m spacy download en_core_web_md

# Copy the Python script into the container
COPY semantics.py /app/semantics.py

# Run the Python script when the container launches
CMD ["python", "semantics.py"]

