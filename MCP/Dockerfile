# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
# We copy the parent directory to include tc_api_sdk which is a dependency
COPY . /app

# Install any needed packages specified in requirements.txt
# We need to install the local package as well
RUN pip install --no-cache-dir -r MCP/requirements.txt
RUN pip install --no-cache-dir -e .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run sse_server.py when the container launches
# TC_API_KEY is optional:
# - If set here (ENV), it acts as a default/fallback.
# - If not set, clients MUST provide 'Authorization: Bearer <KEY>' header.
CMD ["python", "MCP/sse_server.py"]
