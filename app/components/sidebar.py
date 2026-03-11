"""Shared sidebar navigation."""
import streamlit as st


def render_sidebar():
    """Render the sidebar navigation."""
    with st.sidebar:
        st.title("☕ Sandy's Dashboard")
        st.markdown("*Complete 6-Module Experience*")
        st.markdown("---")

        # Navigation links
        st.page_link("pages/00_How_to_Use.py", label="📖 How to Use")
        st.page_link("pages/01_Dashboard.py", label="📊 Executive Dashboard")
        st.page_link("pages/02_Clients.py", label="👥 Client Intelligence")
        st.page_link("pages/03_Pipeline.py", label="📈 Pipeline Visualizer")
        st.page_link("pages/04_Live_Call.py", label="🎙️ Live Coaching Assistant")
        st.page_link("pages/05_Analysis.py", label="📊 Post-Call Analysis")
        st.page_link("pages/06_Admin.py", label="⚙️ Admin Streamliner")

        st.markdown("---")

        # Show active clients count
        try:
            from utils.database import get_all_clients
            clients = get_all_clients()
            st.metric("Active Clients", len(clients))
        except Exception:
            st.metric("Active Clients", "—")

        st.markdown("---")

        # Dev logs button
        if st.button("🔒 Dev Logs", key="dev_logs"):
            st.switch_page("pages/99_Dev_Logs.py")

        st.caption("For Sandy. Complete experience. ☕")
