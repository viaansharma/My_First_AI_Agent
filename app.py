# app.py
import streamlit as st
from agent_utils import get_search_results
from typing import Optional

# Constants
APP_TITLE = "🔍 Ask Viaan's GenAI Search Agent"
DEFAULT_PROMPT = "e.g. What are the latest trends in Generative AI?"

def display_results(response: str) -> None:
    """Display formatted search results."""
    st.success("✅ Here's what I found:")
    st.markdown("---")
    st.write(response)
    st.markdown("---")

def main() -> None:
    """Main application function."""
    # Configure page
    st.set_page_config(
        page_title="🔎 GenAI Search Agent", 
        page_icon="🤖",
        layout="centered"
    )
    
    st.title(APP_TITLE)
    st.caption("Powered by advanced AI search technology")
    
    # Session state initialization
    if "last_query" not in st.session_state:
        st.session_state.last_query = ""
    
    # Search interface
    query = st.text_input(
        "Enter your query:", 
        placeholder=DEFAULT_PROMPT,
        key="search_input"
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        search_clicked = st.button(
            "Search", 
            type="primary",
            use_container_width=True
        )
    with col2:
        clear_clicked = st.button(
            "Clear", 
            use_container_width=True
        )
    
    # Handle actions
    if clear_clicked:
        st.session_state.last_query = ""
        st.rerun()
    
    if search_clicked:
        if query.strip():
            if query == st.session_state.last_query:
                st.info("ℹ️ Same query as last search. Refreshing results...")
            
            st.session_state.last_query = query
            
            with st.spinner("🔍 Searching across knowledge sources..."):
                try:
                    response = get_search_results(query)
                    display_results(response)
                except Exception as e:
                    st.error(f"❌ Error occurred: {str(e)}")
                    st.warning("Please try again or rephrase your query.")
        else:
            st.warning("⚠️ Please enter a query before searching.")

if __name__ == "__main__":
    main()
