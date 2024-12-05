# Step 1: Use a Python base image
FROM python:3.8-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file to the container
COPY requirements.txt /app/

# Step 4: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application files
COPY . /app/

# Step 6: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 7: Set the command to run the Flask app
CMD ["python", "app.py"]
