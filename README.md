<div align="center">

# 🧠 Emotion Pro Analytics — Nuanced Sentiment & Business Alignment AI

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Outfit&weight=700&size=32&duration=3500&pause=1000&color=FF4B4B&center=true&vCenter=true&width=900&height=50&lines=Fine-Grained+Emotion+Classification;Mapping+Customer+Emotions+to+Business+Action;DistilBERT+%7C+PyTorch+%7C+Streamlit+UI)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-Orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

<br/>

[![🚀 Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Emotion_Pro_AI-ff4b4b?style=for-the-badge&labelColor=151624)](https://nuance-flow-app.streamlit.app/)
[![GitHub Stars](https://img.shields.io/github/stars/mayank-goyal09/nuance-flow?style=for-the-badge&color=ffd700)](https://github.com/mayank-goyal09/nuance-flow/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mayank-goyal09/nuance-flow?style=for-the-badge&color=87ceeb)](https://github.com/mayank-goyal09/nuance-flow/network)

<br/>

![Emotion Pro Analytics Dashboard](dashboard.png)

<br/>

### 🧠 **Using Fine-Tuned DistilBERT embeddings to route customer emotions to action** 

### **From Raw Feedback Reviews → Real-Time Strategic Response Workflows** 🚀

</div>

---

## ⚡ **THE ANALYSIS AT A GLANCE**

<table>
<tr>
<td width="50%">

### 🎯 **What This Project Does**

Emotion Pro is an **AI-powered intelligence pipeline** designed to go far beyond binary positive/negative sentiment. It identifies **6 complex human emotions** in customer reviews and dynamically routes predictions directly to distinct operational response workflows.

**The Complete Pipeline:**
- 📡 **Dataset Harvesting** → Downloads Google's GoEmotions from Hugging Face
- ✂️ **Tokenization & Preprocessing** → Sentence encoding via lightweight PyTorch loaders
- 🧠 **Supervised Fine-Tuning** → Retrains pre-trained **DistilBERT** architectures
- 📊 **Strategic Response Routing** → Maps emotion labels to action priority badges
- 🛡️ **Uncertainty Classification Gate** → Isolates ambiguous entries for human audit
- 🎨 **Glassmorphic UI Dashboard** → Renders real-time gauges, tab panels, and donuts

</td>
<td width="50%">

### ✨ **Key Highlights**

| Feature | Details |
|---------|---------|
| 🔬 **Fine-Grained NLP** | Classifies 6 business-critical emotions |
| 🛡️ **Uncertainty Safety** | Autodetects Ambiguity under 60% confidence |
| 🚨 **Priority Escalation** | Direct matching to 4 operational response buckets |
| 📂 **CSV Bulk Processing** | Batch updates visualizing reviews in seconds |
| 🍩 **Interactive Plots** | Real-time Plotly charts & detailed metrics |
| 🎨 **UI Aesthetics** | Premium Dark Glassmorphism & Floating Emojis |
| 💻 **Responsive** | Built on Streamlit for desktop and mobile runs |
| ⚡ **Performance** | Resource optimized caching for quick model runs |

</td>
</tr>
</table>

---

## 🛠️ **TECHNOLOGY STACK**

<div align="center">

![Tech Stack](https://skillicons.dev/icons?i=python,pytorch,github,vscode)

</div>

| **Category** | **Technologies** | **Purpose** |
|:------------:|:-----------------|:------------|
| 🐍 **Core Language** | Python 3.8+ | Primary backend development language |
| 🧠 **Deep Learning** | PyTorch (torch) | Core framework supporting tensor arithmetic |
| 🤗 **NLP / Transformers** | Hugging Face (transformers, datasets) | Pre-trained model loading, tokenization & fine-tuning |
| 🎨 **Frontend UI** | Streamlit | Glassmorphic web interface and control dashboard |
| 📈 **Data Visualization** | Plotly / Pandas | Interactive donut and bar priority diagrams |
| 🧬 **Data Science** | Scikit-Learn | Training/validation split & scoring computations |

---

## 🔬 **HOW EMOTION PRO WORKS**

```mermaid
graph TD
    A[📂 CSV Review / Input Text] --> B[🧠 EmotionEngine Classifier]
    B --> C{Confidence Score >= 60%?}
    
    C -->|No| D[🔍 Category: Ambiguous]
    D --> E[⚠️ ACTION: Human Review Required]
    
    C -->|Yes| F[🎭 Map Top Class to Emotion]
    F --> G{Emotion Type?}
    
    G -->|Joy / Love| H[🟢 ACTION: PROMOTER]
    G -->|Anger / Sadness| I[🔴 ACTION: CRITICAL]
    G -->|Fear| J[🟠 ACTION: URGENT]
    G -->|Surprise| K[🔵 ACTION: MONITOR]
    
    E --> L[🎨 Glassmorphic Streamlit Dashboard]
    H --> L
    I --> L
    J --> L
    K --> L
    
    style A fill:#ff4b4b,color:#fff
    style B fill:#151624,color:#fff,stroke:#ff4b4b
    style D fill:#f39c12,color:#fff
    style H fill:#2ecc71,color:#fff
    style I fill:#e74c3c,color:#fff
    style J fill:#e67e22,color:#fff
    style K fill:#3498db,color:#fff
    style L fill:#9b59b6,color:#fff
```

### **The Strategic Actions Breakdown:**

<table>
<tr>
<td>

#### 🟢 **1. Promoters (Joy, Love)**
Identifies highly satisfied customer brand advocates. Routable directly to marketing channels for referral signups, testimonial acquisition, or discount coupons.

</td>
<td>

#### 🔴 **2. Critical Issues (Anger, Sadness)**
Captures frustrated or disappointed customers experiencing product breakdowns or shipping delays. Routes directly to active Customer Service queues for instant resolution.

</td>
</tr>
<tr>
<td>

#### 🟠 **3. Urgent Alarms (Fear)**
Identifies extreme security, payment failure, account hacking, or safety concerns (e.g., overheating issues). Escalates straight to senior developers or executives.

</td>
<td>

#### 🔵 **4. General Monitoring (Surprise)**
Catches customers shocked by unexpected product behavior (negative or positive), helping product managers track unexpected UX outcomes or feature discoverability.

</td>
</tr>
</table>

---

## ⚠️ **KEY PROBLEMS FACED & STRATEGIC FIXES**

Developing and deploying a deep learning model locally presented several interesting integration bugs. Here is how they were systematically resolved:

### 1. The Missing Tokenizer Bug ⚠️
* **The Bug**: During local model serialization inside the training pipeline, only raw model weights and structural parameters were written to `./final_emotion_model`. Running prediction scripts caused immediate execution crashes because the Hugging Face pipeline could not identify tokenizer assets (`tokenizer.json`, `vocab.txt`).
* **The Fix**: Patched `train.py` to systematically export the vocabulary assets alongside the weights using:
  ```python
  from preprocess import tokenizer
  tokenizer.save_pretrained("./final_emotion_model_v2")
  ```

### 2. Unmapped Raw Classifier Classes (`LABEL_X` Output) 🏷️
* **The Bug**: Predictions initially output generic indices (`LABEL_0`, `LABEL_1`, etc.) because the saved configuration file lacked custom emotion definitions. This ruined analytics mapping as the frontend expected raw strings.
* **The Fix**: Configured exact labeling hashes directly in the initialization phase of the classification model head:
  ```python
  TARGET_EMOTIONS = ['joy', 'love', 'anger', 'sadness', 'fear', 'surprise']
  id2label = {i: label for i, label in enumerate(TARGET_EMOTIONS)}
  label2id = {label: i for i, label in enumerate(TARGET_EMOTIONS)}
  ```

### 3. Streamlit Page Rerun State Losses 🔄
* **The Bug**: Due to Streamlit's structural layout rendering model, standard buttons behave as instantaneous triggers. Clicking custom text analysis triggered page refreshes which immediately dropped uploaded CSV inputs, throwing the user back to the starting dashboard menu.
* **The Fix**: Refactored `app.py` utilizing Streamlit's `st.session_state` API to bind data frames globally:
  ```python
  if "df" not in st.session_state:
      st.session_state.df = None
  ```
  This retains datasets indefinitely until cleared by the user via a dedicated sidebar **🧹 Clear/Reset** widget.

### 4. Over-Automating Mixed Reviews (False Positives) 🛡️
* **The Bug**: Sarcastic, mixed, or poorly structured comments (e.g., *"I hate this app, but I love the support team"*) returned low prediction confidence values, leading to incorrect routing.
* **The Fix**: Embedded a custom **Uncertainty Filter Gate** directly into prediction modules. Any top-tier prediction scoring a confidence coefficient of `< 0.60` is flagged as **"Ambiguous"**, mapping automatically to **"Human Review Required 🔍"** to prevent automated response failures.

### 5. Streamlit Deployment: Missing Local Weights (Hugging Face Hub Migration) 🚀
* **The Bug**: To keep the GitHub repository lightweight and prevent pushing 260MB model binaries, `.gitignore` excludes `final_emotion_model_v2/`. Consequently, Streamlit Cloud deployments crashed on startup because they couldn't find the model weights locally.
* **The Fix**: Created a secure [upload_to_hf.py](file:///c:/my_local_data%28one%20drive%29/Attachments/Ambition%20course/my_all_projects/project%2062%20Emotion-Analytics/upload_to_hf.py) script to automatically login and push the local fine-tuned model to the Hugging Face Model Hub under `mayankg09/emotion-analytics-distilbert`. Patched [engine.py](file:///c:/my_local_data%28one%20drive%29/Attachments/Ambition%20course/my_all_projects/project%2062%20Emotion-Analytics/engine.py) to implement a **hybrid loader** that searches for the local model folder first, dynamically falling back to download from Hugging Face Hub when deployed online.

### 6. Hidden Floating Emoji Background (CSS Stack Layering) 🎨
* **The Bug**: Standard Streamlit structural container viewports (`stAppViewContainer` and `stMainViewContainer`) render with default solid background layers, overlapping and completely hiding the fixed custom `.emoji-bg` layout (at `z-index: -1`).
* **The Fix**: Refactored the dashboard styling inside [app.py](file:///c:/my_local_data%28one%20drive%29/Attachments/Ambition%20course/my_all_projects/project%2062%20Emotion-Analytics/app.py) to bind the radial gradient to the base `html` tag, making all internal Streamlit wrappers completely transparent (`background: transparent !important`). This exposes the floating emojis behind all content cards without affecting the page's interactivity.

### 7. NLP Case Study: Semantic Ambiguity & Machine Bias (Curiosity vs. Surprise) 🔬
* **The Inquiry**: To test the boundaries of our pipeline, we inputted a complex, grammatically structured freelance query:
  > *"so, as you know, I have texted with you so many things about freelancing earlier. On the basis of my history, can you please find out without the drawbacks?"*
* **The Model Output**: It classified the sentence as **`surprise`** with **`67.03%` confidence** (routing to the `MONITOR` action bucket).
* **The MLOps Insight**: While a human reads this as a polite request/inquiry based on *Curiosity*, the transformer model associates structural components (e.g. the conversational starting tag *"so, as you know..."*, direct negation *"without"*, and final question mark) with statistical characteristics of "surprise" and "confusion" present in GoEmotions. This case study demonstrates why the **60% Uncertainty Gate** and non-disruptive priority mapping (like **`MONITOR`**) are critical for real-world deployments to prevent automated customer workflow failures.

---

## 📂 **PROJECT STRUCTURE**

```text
🧠 Emotion-Analytics/
│
├── 📂 final_emotion_model_v2/   # Fine-tuned model weights, config, and tokenizer assets
├── 📂 emotion_model_results/    # Saved checkpoint outputs generated during training epochs
├── 📂 logs/                     # Local training logs
│
├── ⚙️ engine.py                 # Prediction pipeline class & Strategic Action mapper
├── 📊 app.py                    # Streamlit Glassmorphic dark UI layout
│
├── 📈 preprocess.py             # GoEmotions tokenization & train/test dataset splits (80/20)
├── 🧬 train.py                  # PyTorch model trainer using Hugging Face's Trainer API
├── 📡 data_loader.py            # Dataset fetcher isolating targeted business-critical labels
│
├── 🧪 generate_test_data.py     # Generates balanced mock datasets for QA evaluations
├── 📦 requirements.txt          # Python package requirements
├── 📊 dashboard.png             # UI interface preview asset
└── 📖 README.md                 # Project documentation (You are here!) 🚀
```

---

## 🚀 **QUICK START GUIDE**

<div align="center">

![Quick Start](https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif)

</div>

### **Step 1: Clone the Repository** 📥

```bash
git clone https://github.com/mayank-goyal09/nuance-flow.git
cd nuance-flow
```

### **Step 2: Create a Virtual Environment** 🐍

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Required Packages** 📦

```bash
pip install -r requirements.txt
```

### **Step 4: Download and Fine-Tune the Brain** 🧠

```bash
# 1. Harvest & filter Google's GoEmotions Dataset
python data_loader.py

# 2. Preprocess text, split, and run fine-tuning on DistilBERT
python train.py
```
*Note: Training spans 6 full epochs to guarantee convergence. Optimization results in saving the fine-tuned classifier to `./final_emotion_model_v2`.*

### **Step 5: Launch the Streamlit Dashboard** 🖥️

```bash
streamlit run app.py
```

---

## 📚 **SKILLS DEMONSTRATED**

| **Category** | **Skills** |
|:-------------|:-----------|
| 🧠 **Deep Learning** | Supervised Fine-Tuning, Transformer Architecture (DistilBERT), PyTorch tensor mapping |
| 📊 **NLP Engineering** | Sequence tokenization, Vocabulary configuration, Custom label mapping, Multi-class filtering |
| 🎨 **UI/UX Craftsmanship** | Dark Mode design, HTML/CSS layout configuration, Custom keyframe animations, Glassmorphism panels |
| 📈 **Data Visualization** | Plotly charts, Multi-class donut distribution mapping, Real-time metrics visualization |
| 🚀 **MLOps & Engineering** | Local model serializations, tokenizer caching, UI State Management configurations |

---

## 🔮 **FUTURE ENHANCEMENTS**

- [ ] 🤖 **Generative Auto-Replies**: Use LLMs to draft context-appropriate responses matching predicted emotions.
- [ ] 📈 **Sentiment Chronology**: Track dynamic emotional changes inside multi-paragraph ticket updates.
- [ ] 📧 **Zapier/CRM Connectors**: Automatically trigger alerts in Slack, Salesforce, or Zendesk based on action labels.
- [ ] 🌐 **Multi-Lingual Inference**: Add support for French, Spanish, German, and Hindi feedback inputs.

---

## 👨‍💻 **CONNECT WITH ME**

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-mayank--goyal09-181717?style=for-the-badge&logo=github)](https://github.com/mayank-goyal09)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mayank_Goyal-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mayank-goyal-4b8756363/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Site-8e44ad?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mayank-goyal09.github.io/)

**Mayank Goyal**  
🧠 AI Engineer | 📊 NLP Specialist | ⚖️ Machine Learning Developer

</div>

---

<div align="center">

### 🧠 **Built with PyTorch, Streamlit & ❤️ by Mayank Goyal**

*"Decoding customer emotions, automating business action."* 🧠🚀

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:ff4b4b,100:ff7575&height=120&section=footer)

</div>
