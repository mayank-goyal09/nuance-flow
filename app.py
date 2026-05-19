import streamlit as st
import pandas as pd
import plotly.express as px
from engine import EmotionEngine

# --- Pro Page Config ---
st.set_page_config(page_title="Emotion Pro Analytics", page_icon="🧠", layout="wide")

# Custom Premium Glassmorphism & Funky Emoji Background Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    /* Background and global elements */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #151624 0%, #0a0b10 100%) !important;
        font-family: 'Outfit', sans-serif !important;
        color: #ffffff !important;
    }
    
    /* Blurry Emojis Background */
    .emoji-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        overflow: hidden;
        pointer-events: none;
    }
    .emoji {
        position: absolute;
        font-size: 140px;
        opacity: 0.12;
        filter: blur(12px);
        user-select: none;
        animation: float 25s infinite ease-in-out;
    }
    .emoji-1 { top: 8%; left: 4%; animation-delay: 0s; font-size: 160px; }
    .emoji-2 { top: 58%; left: 82%; animation-delay: -3s; font-size: 210px; }
    .emoji-3 { top: 78%; left: 12%; animation-delay: -6s; font-size: 150px; }
    .emoji-4 { top: 18%; left: 74%; animation-delay: -9s; font-size: 190px; }
    .emoji-5 { top: 38%; left: 48%; animation-delay: -12s; font-size: 170px; }
    .emoji-6 { top: 82%; left: 48%; animation-delay: -15s; font-size: 140px; }
    .emoji-7 { top: 4%; left: 38%; animation-delay: -18s; font-size: 130px; }
    .emoji-8 { top: 48%; left: 8%; animation-delay: -5s; font-size: 150px; }

    @keyframes float {
        0%, 100% { transform: translateY(0) translateX(0) rotate(0deg) scale(1); }
        33% { transform: translateY(-30px) translateX(20px) rotate(8deg) scale(1.05); }
        66% { transform: translateY(15px) translateX(-15px) rotate(-8deg) scale(0.95); }
    }

    /* Glassmorphism Containers */
    div[data-testid="stExpander"], 
    div[data-testid="metric-container"],
    .glass-card {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
        animation: slideIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    div[data-testid="stExpander"]:hover, 
    div[data-testid="metric-container"]:hover,
    .glass-card:hover {
        transform: translateY(-5px) !important;
        border-color: rgba(255, 75, 75, 0.3) !important;
        box-shadow: 0 12px 40px 0 rgba(255, 75, 75, 0.15) !important;
    }

    /* Header styling with animated text gradient and shadow glow */
    .glow-header {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #ff4b4b 0%, #ff8c8c 50%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        filter: drop-shadow(0px 4px 20px rgba(255, 75, 75, 0.25));
        animation: shine 5s ease-in-out infinite;
    }
    
    @keyframes shine {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    /* Clean modern subtitles */
    .dashboard-subtitle {
        text-align: center;
        font-weight: 400;
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 40px;
    }

    /* Handcrafted Signature / Repository Badge */
    .handcrafted-badge {
        background: rgba(255, 75, 75, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px dashed rgba(255, 75, 75, 0.3);
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(255, 75, 75, 0.05);
        animation: pulse 4s infinite ease-in-out;
        transition: all 0.3s ease;
    }
    .handcrafted-badge:hover {
        background: rgba(255, 75, 75, 0.08);
        border-color: rgba(255, 75, 75, 0.6);
        box-shadow: 0 8px 32px 0 rgba(255, 75, 75, 0.15);
        transform: scale(1.02);
    }
    .handcrafted-title {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #ff4b4b;
        font-weight: 800;
        margin-bottom: 6px;
    }
    .handcrafted-repo {
        font-family: 'Outfit', sans-serif;
        font-size: 1.05rem;
        font-weight: 600;
        color: #ffffff;
    }

    /* Form Fields Styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 12px 18px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ff4b4b !important;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.35) !important;
        background: rgba(255, 255, 255, 0.07) !important;
    }

    /* Buttons styling */
    div.stButton > button {
        background: linear-gradient(135deg, #ff4b4b 0%, #ff7575 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.3) !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }
    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.03) !important;
        box-shadow: 0 8px 25px rgba(255, 75, 75, 0.5) !important;
    }
    div.stButton > button:active {
        transform: translateY(-1px) scale(0.98) !important;
    }

    /* Entrance keyframes */
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(24px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulse {
        0%, 100% { border-color: rgba(255, 75, 75, 0.3); }
        50% { border-color: rgba(255, 75, 75, 0.65); }
    }

    /* Plotly and Sidebar styling adjustments */
    section[data-testid="stSidebar"] {
        background: rgba(10, 11, 16, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Premium Title for metrics and subtitles */
    h3, h4, h2 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Inject Background Emojis Div
st.markdown("""
    <div class="emoji-bg">
        <div class="emoji emoji-1">🧠</div>
        <div class="emoji emoji-2">💖</div>
        <div class="emoji emoji-3">🔥</div>
        <div class="emoji emoji-4">😢</div>
        <div class="emoji emoji-5">😱</div>
        <div class="emoji emoji-6">😂</div>
        <div class="emoji emoji-7">🥰</div>
        <div class="emoji emoji-8">⚡</div>
    </div>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <h1 class="glow-header">🚀 Nuanced Sentiment Analytics</h1>
    <p class="dashboard-subtitle">Transforming Customer Emotions into Business Strategy</p>
    """, unsafe_allow_html=True)

# Initialize the Engine
@st.cache_resource
def load_brain():
    return EmotionEngine()

engine = load_brain()

# --- Sidebar: Data Input ---
st.sidebar.markdown("""
    <div class="handcrafted-badge">
        <div class="handcrafted-title">✍️ Handcrafted Workspace</div>
        <div class="handcrafted-repo">project 62 Emotion-Analytics</div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.header("📂 Data Source")
uploaded_file = st.sidebar.file_uploader("Upload Customer Reviews (CSV)", type="csv")

# Initialize session state for loaded dataframe
if "df" not in st.session_state:
    st.session_state.df = None

# Load data if a new file is uploaded
if uploaded_file is not None:
    try:
        st.session_state.df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.sidebar.error(f"Error loading file: {e}")
elif st.sidebar.button("Use Sample Google Data"):
    st.session_state.df = pd.read_csv("mock_data.csv")

# Optional: Add a clean way to reset/clear data
if st.session_state.df is not None:
    if st.sidebar.button("🧹 Clear/Reset Data", type="secondary"):
        st.session_state.df = None
        st.rerun()

# --- Main Dashboard Logic ---
if st.session_state.df is not None:
    df = st.session_state.df
    
    st.write("### 🔍 Real-time Analysis")

    # --- 1. Single Comment Analysis (The "Manager's Playground") ---
    with st.expander("💬 Analyze a Single Customer Comment", expanded=True):
        st.markdown("Try it out! Paste a recent review below to see how the AI interprets it.")
        
        col_input, col_btn = st.columns([4, 1])
        with col_input:
            user_input = st.text_input("Review Text:", placeholder="e.g. I waited 3 hours for my delivery and the food was cold.")
        with col_btn:
            st.write("") # Spacer
            st.write("") # Spacer
            analyze_btn = st.button("Analyze Text", type="primary")

        if analyze_btn and user_input:
            res = engine.predict(user_input)
            
            # Display Result Card
            st.markdown("---")
            r1, r2, r3 = st.columns(3)
            with r1:
                st.info(f"**Emotion:** {res['label'].upper()}")
            with r2:
                st.metric("Confidence Score", f"{res['score']:.2f}")
            with r3:
                # Dynamic Color for Action
                action_color = "red" if res['action'] in ['CRITICAL', 'URGENT'] else "green"
                st.markdown(f"**Action Required:**")
                st.markdown(f":{action_color}[**{res['action']}**]")
    
    st.divider()
    
    # --- 2. Bulk Analysis Section ---
    st.markdown("### 📂 Bulk Analysis (CSV Upload)")
    
    # 3. Analyze Data
    if st.button("Run Bulk AI Analysis"):
        with st.spinner(" analyzing emotions..."):
            # Limit to 50 rows for performance
            df_slice = df.head(50).copy()
            df_slice['analysis'] = df_slice['text'].apply(lambda x: engine.predict(x))
            
            # Flatten results
            df_slice['Emotion'] = df_slice['analysis'].apply(lambda x: x['label'])
            df_slice['Action'] = df_slice['analysis'].apply(lambda x: x['action'])
            df_slice['Score'] = df_slice['analysis'].apply(lambda x: x['score'])
            
            # --- Top metrics ---
            col1, col2, col3 = st.columns(3)
            critical_count = len(df_slice[df_slice['Action'] == 'CRITICAL'])
            promoter_count = len(df_slice[df_slice['Action'] == 'PROMOTER'])
            urgent_count = len(df_slice[df_slice['Action'] == 'URGENT'])
            
            col1.metric("🚨 Critical Issues", critical_count, delta_color="inverse")
            col2.metric("❤️ Likely Promoters", promoter_count)
            col3.metric("⚠️ Urgent Attention", urgent_count, delta_color="inverse")
            
            st.divider()

            # --- Visualizations ---
            c1, c2 = st.columns(2)
            
            # Custom Colors
            color_map = {
                'joy': '#2ecc71', 'love': '#27ae60', 
                'anger': '#e74c3c', 'sadness': '#c0392b',
                'fear': '#f39c12', 'surprise': '#3498db'
            }
            
            with c1:
                st.markdown("#### 📊 Emotion Distribution")
                fig = px.pie(df_slice, names='Emotion', hole=0.4, 
                             color='Emotion', color_discrete_map=color_map)
                st.plotly_chart(fig, use_container_width=True)
                
            with c2:
                st.markdown("#### 🚨 Business Priority")
                action_colors = {'PROMOTER': '#2ecc71', 'CRITICAL': '#e74c3c', 'URGENT': '#e67e22', 'MONITOR': '#3498db'}
                fig2 = px.bar(df_slice, x='Action', color='Action', 
                              category_orders={'Action': ['URGENT', 'CRITICAL', 'MONITOR', 'PROMOTER']},
                              color_discrete_map=action_colors)
                st.plotly_chart(fig2, use_container_width=True)

            # --- Detailed Insights ---
            st.subheader("📝 Review Explorer")
            tab1, tab2 = st.tabs(["🔥 Critical/Urgent", "❤️ Promoters"])
            
            with tab1:
                criticals = df_slice[df_slice['Action'].isin(['CRITICAL', 'URGENT'])]
                if not criticals.empty:
                    for i, row in criticals.iterrows():
                        st.error(f"**{row['Emotion'].upper()}** (Score: {row['Score']}): {row['text']}")
                else:
                    st.success("No critical issues found in this batch! 🎉")
            
            with tab2:
                partners = df_slice[df_slice['Action'] == 'PROMOTER']
                if not partners.empty:
                    for i, row in partners.iterrows():
                        st.success(f"**{row['Emotion'].upper()}** (Score: {row['Score']}): {row['text']}")
                else:
                    st.info("No clear promoters identified yet.")

else:
    st.info("👋 Welcome, Mayank! Please upload a file or click 'Use Sample Google Data' in the sidebar to begin.")

# Bottom section removed to avoid redundancy