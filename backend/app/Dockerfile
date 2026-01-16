# FROM python:3.11-slim

# WORKDIR /app

# # Install Gmail MCP server
# RUN pip install gmail-mcp-server

# # Copy backend code
# COPY . .

# RUN pip install -r requirements.txt

# ENV TRANSPORT=stdio

# #CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
# CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]


FROM python:3.11-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install MCP server
RUN pip install gmail-mcp-server

# Copy app
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV TRANSPORT=stdio

EXPOSE 10000

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
#CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]




