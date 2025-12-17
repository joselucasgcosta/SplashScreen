# Usar uma imagem base Python
FROM python:3.13-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar pacotes do sistema (inclui locales)
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    openjdk-17-jdk \
    wget \
    ca-certificates \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos necessários
COPY . .

# Instalar dependências Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Porta do Streamlit
# EXPOSE 5012

# Comando para rodar a aplicação
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8503", "splash:app" ]
