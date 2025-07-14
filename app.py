import streamlit as st
from agent_utils import get_search_results

st.set_page_config(page_title="🔎 GenAI Search Agent", page_icon="🤖")

st.title("🔍 Ask Viaan's GenAI Search Agent")

# Initialize session state for the search trigger
if "search_triggered" not in st.session_state:
    st.session_state.search_triggered = False

def trigger_search():
    """Sets the search flag to True when Enter is pressed."""
    st.session_state.search_triggered = True

# Text input with Enter key support
query = st.text_input(
    "Enter your query:",
    placeholder="e.g. What are the latest trends in Generative AI?",
    on_change=trigger_search,  # Triggered on Enter
    key="query_input"  # Helps track changes
)

# Search button (optional, retains button click functionality)
if st.button("Search") or st.session_state.search_triggered:
    if query.strip():
        with st.spinner("Searching..."):
            response = get_search_results(query)
        st.success("✅ Here's what I found:")
        st.write(response)
        st.session_state.search_triggered = False  # Reset the trigger
    else:
        st.warning("⚠️ Please enter a query before searching.")
