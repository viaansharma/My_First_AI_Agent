# app.py
import streamlit as st
from agent_utils import get_search_results
import os

# Set page config
st.set_page_config(
    page_title="🔎 GenAI Search Agent", 
    page_icon="🤖",
    layout="centered"
)

st.title("🔍 Ask Viaan's GenAI Search Agent")

# Load API key (prefer Streamlit secrets)
api_key = st.secrets.get("LLAMA_API_KEY") or os.getenv("LLAMA_API_KEY")

# Input query
query = st.text_input(
    "Enter your query:", 
    placeholder="e.g. What are the latest AI trends?",
    key="query_input"
)

if st.button("Search", type="primary"):
    if not query.strip():
        st.warning("⚠️ Please enter a query.")
    else:
        with st.spinner("🔍 Searching..."):
            try:
                if not api_key:
                    st.error("❌ API Key missing. Set `LLAMA_API_KEY` in secrets.")
                else:
                    response = get_search_results(query, api_key=api_key)
                    st.success("✅ Results:")
                    st.markdown("---")
                    st.write(response)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("ℹ️ Check your API key or try again later.")
                
