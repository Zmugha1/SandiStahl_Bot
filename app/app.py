"""
Sandy's Complete 6-Module Coaching Dashboard
Main entry point
"""
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

import streamlit as st

st.set_page_config(
    page_title="Sandy's Coaching Dashboard",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Render sidebar
from components.sidebar import render_sidebar
render_sidebar()

# Show welcome message
st.title("☕ Welcome to Sandy's Coaching Dashboard")
st.markdown("""
### 👋 Hello Sandy!

This is your **Coaching Intelligence Dashboard** - a complete 6-module experience designed to help you:

- 📊 **Track your clients** through the coaching pipeline
- 👥 **Understand client profiles** with DISC analysis
- 📈 **Visualize your pipeline** from Discovery to Launch
- 💡 **Get coaching tips** based on client personality types
- 📝 **Log calls and activities** for better follow-up

### 🚀 Get Started

Use the **sidebar on the left** to navigate:
- 📖 **How to Use** - Learn how to use the dashboard
- 📊 **Dashboard** - Your daily overview and priorities
- 👥 **My Clients** - Deep client intelligence
- 📈 **Pipeline** - Visual sales funnel
- 💡 **Coaching Helper** - DISC-based guidance

---

*For technical support, click the 🔒 Dev Logs button in the sidebar.*
""")

# Show quick stats
try:
    from utils.database import get_dashboard_stats
    stats = get_dashboard_stats()

    st.markdown("---")
    st.subheader("📊 Quick Stats")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Clients", stats.get('active_clients', 0))
    with col2:
        st.metric("In Committing", stats.get('c4_clients', 0))
    with col3:
        pipeline = stats.get('pipeline_value', 0) / 1000000
        st.metric("Pipeline Value", f"${pipeline:.1f}M")
    with col4:
        st.metric("Closed YTD", stats.get('closed_ytd', 0))

except Exception as e:
    st.error(f"Could not load stats: {e}")
