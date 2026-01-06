import streamlit as st
from backend import process_customer_message

# Configuração simples
st.set_page_config(page_title="Smart Reply Assistant", page_icon="🤖")

st.title("🤖 Smart Reply Assistant 1.0")
st.markdown("Chat com IA local 100% confidêncial para manter os dados da empresa e dos seus clientes seguros.")

# Entrada de texto
customer_input = st.text_area("Mensagem do cliente:", height=150)

if st.button("Gerar Resposta"):
    if customer_input.strip():
        with st.spinner("Processando..."):
            
            opcoes = process_customer_message(customer_input)
            
            st.divider()
            st.subheader("Respostas Geradas:")
            
            tab1, tab2, tab3 = st.tabs(["Curta", "Detalhada", "Comercial"])
            with tab1:
                st.info(opcoes.get("curta", "Erro ao gerar."))
                
            with tab2:
                st.success(opcoes.get("detalhada", "Erro ao gerar."))
                
            with tab3:
                st.warning(opcoes.get("comercial", "Erro ao gerar."))
    else:
        st.error("Por favor, digite uma mensagem.")