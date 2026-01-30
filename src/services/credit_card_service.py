import re
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
        client = DocumentIntelligenceClient(endpoint=Config.ENDPOINT, credential=credential)
        
        poller = client.begin_analyze_document(
            "prebuilt-read", 
            AnalyzeDocumentRequest(url_source=card_url)
        )
        result = poller.result()

        full_text = ""
        lines = []
        for page in result.pages:
            for line in page.lines:
                full_text += line.content + " "
                lines.append(line.content.strip())
        
        # --- LÓGICA DE EXTRAÇÃO ---
        
        # 1. Número do Cartão
        card_number_match = re.search(r'(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})', full_text)
        
        # 2. Data de Validade
        expiry_match = re.search(r'(0[1-9]|1[0-2])\/([0-9]{2,4})', full_text)

        # 3. Nome do Titular (Busca por padrão de nome em maiúsculas)
        holder_name = None
        # Palavras que devemos ignorar pois não são nomes de pessoas
        blacklist = ["VALID", "THRU", "GOOD", "UNTIL", "CARDHOLDER", "VISA", "MASTERCARD", "BANK"]
        
        for line in lines:
            # Verifica se a linha está toda em maiúsculas, tem mais de uma palavra e não tem números
            if line.isupper() and len(line.split()) >= 2 and not any(char.isdigit() for char in line):
                # Se a linha não contém palavras da blacklist, provavelmente é o nome
                if not any(word in line for word in blacklist):
                    holder_name = line
                    break 

        if card_number_match:
            return {
                "card_number": card_number_match.group(0),
                "expiry_date": expiry_match.group(0) if expiry_match else "Não encontrado",
                "cardholder_name": holder_name if holder_name else "Não identificado"
            }
        
        return None

    except Exception as e:
        print(f"Erro técnico: {e}")
        return None