FROM python:3.11-slim

WORKDIR /app

# Copia os arquivos necessários
COPY backend/ ./backend/
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Railway vai usar
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
