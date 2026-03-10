"""How to Use - User Guide for Sandy's Dashboard."""
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

import streamlit as st
from utils.styles import CUSTOM_CSS
from utils.logger import log_activity
from components.sidebar import render_sidebar

render_sidebar()
log_activity("page_view", page="How to Use")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown("<h1>📖 How to Use Your Dashboard</h1>", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg, #2E5C8A 0%, #4A7BA7 100%);
            padding: 20px; border-radius: 12px; color: white; margin-bottom: 24px;">
    <div style="font-size: 1.1rem;">
        Welcome to your Coaching Intelligence Dashboard! This guide will help you navigate
        and get the most out of your coaching tools.
    </div>
</div>
""", unsafe_allow_html=True)

# Section 1: Dashboard Overview
st.markdown("## 📊 Dashboard - Your Daily Overview")

st.markdown("""
The **Dashboard** is your home screen. Here's what you'll see:

**📅 Today's Schedule**
- See your upcoming calls and meetings
- Each item shows the client name and what type of call it is

**📈 Pipeline Health**
- Visual view of where all your clients are in the process
- From Discovery (first meeting) to Launching (signed deal)

**🎯 This Week's Goals**
- Track your progress on key metrics
- IC Calls: How many new prospects you've contacted
- C1→C2: How many clients are moving forward
- New C4: How many are ready to commit

**🔥 Hot Prospects**
- Your most engaged clients (5-star interest level)
- These need your attention first!

**⚠️ Alerts**
- Clients you haven't contacted in 7+ days
- Don't let prospects go cold!
""")

# Section 2: My Clients
st.markdown("## 👥 Client Intelligence - Deep Client Profiles")

st.markdown("""
The **Client Intelligence** page is where you dive deep into each prospect.

**How to use it:**
1. Select a client from the dropdown
2. Review their complete profile:

**💰 I.L.W.E. Goals**
- **Income**: What they want to earn
- **Lifestyle**: How they want to live
- **Wealth**: Long-term financial goals
- **Equity**: What ownership means to them

**🎭 DISC Profile**
- Shows their communication style (D, I, S, or C)
- Use this to adapt your coaching approach!

**🚩 Red/Green Flags**
- Green = Positive signs (funding ready, spouse supportive)
- Red = Concerns to address (health issues, timeline uncertain)

**📋 Next Steps**
- Your action items for this client
- Check these off as you complete them

**Action Buttons:**
- 📞 Log Call: Record a coaching call
- ✉️ Send Email: Quick email template
- ➡️ Move Stage: Advance them to next stage
- 📊 View Analysis: See call quality scores
""")

# Section 3: Pipeline
st.markdown("## 📈 Pipeline - Visual Sales Funnel")

st.markdown("""
The **Pipeline** page shows where ALL your clients are in the journey.

**The 8 Stages:**

| Stage | Name | What It Means |
|-------|------|---------------|
| **Discovery** | First Meeting | Getting to know each other |
| **Learning** | Education | Teaching about franchises |
| **Exploring** | Deep Dive | Narrowing down options |
| **Researching** | Validation | Researching specific brands |
| **Deciding** | Serious | Reviewing FDDs, close to decision |
| **Committing** | Ready | About to sign agreement |
| **Launching** | Signed | In training, starting up |
| **Complete** | Done | Deal closed or disqualified |

**How to use it:**
- See how many clients are in each stage
- Select a stage to see who's there
- Identify where you need more prospects
""")

# Section 4: Live Coaching & Analysis
st.markdown("## 🎙️ Live Coaching & Post-Call Analysis")

st.markdown("""
**Live Coaching Assistant** - Real-time call guidance with timer and suggested questions.

**Post-Call Analysis** - Score your calls using the CLEAR method and track improvements.
""")

# Section 5: Quick Tips
st.markdown("## 💡 Quick Tips")

st.markdown("""
**Daily Routine:**
1. ☕ Start with Dashboard - check today's schedule and alerts
2. 📞 Make your calls - use Live Coaching for guidance
3. 📝 Log each call - notes help you remember details
4. 🎯 Review Pipeline - see who's ready to move forward

**Key Success Factors:**
- **Follow up within 48 hours** after every call
- **Use the DISC profile** to adapt your communication
- **Address red flags early** before they become blockers
- **Celebrate wins** when clients move stages!

**Need Help?**
- Click the 🔒 **Dev Logs** button in the sidebar for technical logs
- Password: `sandydev2026`
""")

# Section 6: FAQ
st.markdown("## ❓ Frequently Asked Questions")

faq = {
    "What do the stars mean?": "⭐ = Interest level (1-5). More stars = more engaged client.",
    "What is I.L.W.E.?": "Income, Lifestyle, Wealth, Equity - the 4 goals every client has.",
    "What are Red/Green Flags?": "Green = good signs. Red = concerns you need to address.",
    "How do I move a client to the next stage?": "Use the 'Move Stage' button on their profile.",
    "What if a client goes cold?": "Check the Dashboard alerts - follow up within 7 days!",
}

for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6B7280;'>Happy Coaching! ☕</div>", unsafe_allow_html=True)
