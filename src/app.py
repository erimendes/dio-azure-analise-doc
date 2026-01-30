import streamlit as st
from services.blob_service import upload_file_to_blob
from services import credit_card_service as show 

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo para upload", type=["png", "jpg", "jpeg", "pdf"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        st.success("Arquivo carregado com sucesso!")
        
        # Faz o upload
        blob_url = upload_file_to_blob(uploaded_file, fileName)
        
        if blob_url:
            st.success(f"Arquivo {fileName} enviado com sucesso!")
            
            # 'show' é o arquivo, então 'show.função'
            credit_card_info = show.analize_credit_card(blob_url)
            
            # Função de exibição que está abaixo
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error(f"Falha ao enviar o arquivo {fileName}.")
    else:
        st.info("Nenhum arquivo foi carregado ainda.")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Arquivo Carregado", width="stretch")
    st.write("Validação do Cartão de Crédito:")
    if credit_card_info:
        st.markdown("### Detalhes do Cartão de Crédito") 
        st.markdown(f"- **Número do Cartão:** {credit_card_info.get('card_number', 'N/A')}")  
        st.markdown(f"- **Nome do Titular:** {credit_card_info.get('cardholder_name', 'N/A')}") 
        st.markdown(f"- **Data de Validade:** {credit_card_info.get('expiry_date', 'N/A')}")
    else:
        st.markdown("<h1 style='color:red;'>Nenhum cartão detectado.</h1>", unsafe_allow_html=True)
        
if __name__ == "__main__":
    configure_interface()