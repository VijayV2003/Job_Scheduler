# Use the official Python 3.9-slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy model AFTER ensuring compatible versions
RUN python -m spacy download en_core_web_sm
RUN pip install pdfplumber
RUN pip install scikit-learn



# Copy the rest of the application files
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
