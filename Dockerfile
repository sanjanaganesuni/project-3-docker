# Use a minimal Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /home/data

# Copy the Python script and text files into the container
COPY scripts.py /home/data/scripts.py
COPY IF-1.txt /home/data/IF-1.txt
COPY AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt

# Install required packages
RUN pip install --no-cache-dir nltk

# Define the command to run the script
CMD ["python", "/home/data/scripts.py"]
