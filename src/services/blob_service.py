import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config

def upload_file_to_blob(file, file_name):
    try:
        # 1. Validação da String de Conexão
        conn_str = Config.AZURE_STORAGE_CONNECTION_STRING
        if not conn_str or "DefaultEndpointsProtocol" not in conn_str:
            st.error("Erro: A Connection String no Config.py está inválida ou vazia.")
            return None

        # 2. Inicialização do Cliente
        blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        
        # 3. Referência ao Blob (Usando o nome do container do print anterior)
        blob_client = blob_service_client.get_blob_client(container=Config.Container_Name, blob=file_name)
        
        # 4. Upload dos bytes (Importante: usamos getvalue() para o Streamlit)
        data = file.getvalue()
        blob_client.upload_blob(data, overwrite=True)
        
        # Retorna a URL pública
        return blob_client.url

    except Exception as e:
        # Exibe o erro exato para facilitar o diagnóstico
        st.error(f"Erro ao enviar arquivo para o Blob Storage: {e}")
        return None