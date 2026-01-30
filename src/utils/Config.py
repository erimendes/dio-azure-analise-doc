import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class Config:
    # Azure Document Intelligence (ou Cognitive Services)
    ENDPOINT = os.getenv("ENDPOINT")
    SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
    
    # Azure Storage
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    
    # Se no blob_service.py estiver Config.Container_Name, use o nome abaixo:
    Container_Name = os.getenv("CONTAINER_NAME")