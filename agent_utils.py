# app.py
import streamlit as st
import os
from agent_utils import get_search_results
from typing import Optional

# Configuration - Load API key from environment variables
API_KEY = os.getenv("LLAMA_API_KEY")  # Recommended: Set in environment
# OR from Streamlit secrets:
# API_KEY = st.secrets["LLAMA_API_KEY"]

def display_results(response: str) -> None:
    st.success("✅ Here's what I found:")
    st.markdown("---")
    st.write(response)
    st.markdown("---")

def main() -> None:
    st.set_page_config(page_title="🔎 GenAI Search Agent", page_icon="🤖")
    st.title("🔍 Ask Viaan's GenAI Search Agent")
    
    # API Key Check
    if not API_KEY:
        st.error("❌ API Key not configured. Please set LLAMA_API_KEY environment variable.")
        return
    
    query = st.text_input("Enter your query:", placeholder="e.g. AI trends 2024")
    
    if st.button("Search", type="primary"):
        if query.strip():
            with st.spinner("Searching..."):
                try:
                    response = get_search_results(query, api_key=API_KEY)  # Pass API key
                    display_results(response)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("ℹ️ Please check your API key and try again")
        else:
            st.warning("⚠️ Please enter a query")

if __name__ == "__main__":
    main()
    
