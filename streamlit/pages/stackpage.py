import streamlit as st

def stack_page():
    st.title('Technology stack')
    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.image('logo/langchain.jpg', caption="LangChain", use_column_width=True)

    with col2:
        st.image('logo/ollama.jpg', caption="Ollama", use_column_width=True)

if __name__ == "__main__":
    stack_page()