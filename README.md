# 🌾 FarmGuard AI
### AI-Powered Climate Resilience & Early-Warning Assistant for Smallholder Farmers

FarmGuard AI is an intelligent, multi-agent climate preparedness platform designed to help smallholder farmers understand changing weather conditions, identify potential climate risks, and receive actionable farming recommendations.

Built using **AWS Strands Agents SDK, Amazon Bedrock, Python and Streamlit**, FarmGuard AI transforms weather observations into understandable climate-risk assessments and personalized farm-preparedness guidance.

> Built for the AWS Builder Center – Strands SDK: Workshop to Ship Hackathon 2026.

---

## 🌍 Problem Statement

Smallholder farmers face increasing challenges due to climate change, including:

- Unexpected heatwaves and extreme temperatures.
- Irregular rainfall and prolonged dry spells.
- Water scarcity and irrigation difficulties.
- Limited access to personalized agricultural guidance.
- Difficulty interpreting weather forecasts and converting them into practical farming decisions.

Traditional weather applications provide forecast information, but farmers often need additional guidance to understand what actions they should take.

## 💡 Our Solution

FarmGuard AI addresses these challenges through a collaborative AI-agent system.

The platform analyzes weather forecast information, calculates transparent climate-risk indicators, and uses specialized AI agents to generate practical recommendations.

Its primary objective is to make climate-preparedness information more accessible, understandable and actionable for smallholder farmers.

---

## ✨ Key Features

### 1. Climate Risk Assessment
- Analyzes seven-day weather forecast information.
- Identifies potential heat and dry-spell conditions.
- Calculates an explainable climate-risk score.
- Classifies risk into Low, Moderate and High categories.

### 2. Multi-Agent AI Architecture
Uses AWS Strands Agents SDK to coordinate specialized AI agents.

- **Climate Intelligence Agent:** Interprets temperature, rainfall and other weather indicators.
- **Crop Advisory Agent:** Generates practical crop-preparedness recommendations.
- **Water Conservation Agent:** Suggests water-management and conservation practices.
- **Coordinator Agent:** Delegates tasks to specialist agents and combines their findings into a unified advisory.

### 3. Smart Farm Advisory
- Generates prioritized farming preparedness recommendations.
- Considers crop type and growth stage.
- Considers irrigation methods and water availability.
- Provides worker heat-safety guidance.
- Explains uncertainties and limitations.

### 4. Evidence-to-Action Intelligence
Connects climate observations with identified risks and recommended actions.

Every recommendation should be traceable to the supplied weather evidence rather than relying on unsupported AI-generated assumptions.

### 5. Water Conservation Planning
- Suggests practical water-saving approaches.
- Encourages soil-moisture monitoring.
- Highlights water-management considerations.
- Promotes responsible irrigation practices.

### 6. Multilingual Advisory Support
Designed to provide understandable guidance in:
- English
- Hindi
- Marathi

### 7. Impact Dashboard
- Tracks completed climate assessments.
- Displays high-risk assessment counts.
- Records crop and location information.
- Maintains local assessment history using SQLite.

### 8. Rule-Based Baseline Comparison
Compares deterministic recommendations against the richer multi-agent advisory workflow.

### 9. Offline Demonstration Mode
Provides an illustrative sample scenario for testing the interface without requiring an AWS connection.

---

## 🏗️ System Architecture

```text
                  FARMER
                     |
                     v
             STREAMLIT INTERFACE
                     |
                     v
             WEATHER DATA SERVICE
                     |
              OPEN-METEO API
                     |
                     v
             CLIMATE RISK ENGINE
                     |
          HEAT / DRY-SPELL / RAINFALL
                     |
                     v
             STRANDS COORDINATOR
                (Amazon Bedrock)
                     |
          +----------+----------+
          |          |          |
          v          v          v
       CLIMATE     CROP       WATER
       AGENT       AGENT      AGENT
          |          |          |
          +----------+----------+
                     |
                     v
              FARM ADVISORY
                     |
          +----------+----------+
          |                     |
          v                     v
     BASELINE                SQLITE
     COMPARISON              STORAGE
          |                     |
          +----------+----------+
                     |
                     v
             IMPACT DASHBOARD
```

---

## 🧮 Climate Risk Scoring

FarmGuard AI uses a transparent weighted scoring model.

**Risk Score Formula:**

`Risk = (0.40 × Heat) + (0.35 × Dry Spell) + (0.25 × Low Rainfall)`

| Indicator | Weight |
|---|---:|
| Heat Indicator | 40% |
| Dry-Spell Indicator | 35% |
| Low-Rainfall Indicator | 25% |

### Risk Classification

| Score | Risk Level |
|---|---|
| 0–34 | Low |
| 35–64 | Moderate |
| 65–100 | High |

These are prototype screening thresholds, not scientifically validated agricultural warning thresholds. They require local agronomic calibration before real-world deployment.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| AWS Strands Agents SDK | Multi-agent orchestration |
| Amazon Bedrock | Foundation model integration |
| Streamlit | Interactive web interface |
| Open-Meteo API | Weather forecast and geocoding |
| SQLite | Local database |
| Pandas | Weather data processing |
| Pytest | Automated testing |
| Git & GitHub | Version control and collaboration |

---

## 📁 Project Structure

```text
FarmGuardAI/
│
├── app.py
│
├── farmguard/
│   ├── __init__.py
│   ├── agents.py
│   ├── weather.py
│   ├── risk_engine.py
│   ├── baseline.py
│   └── storage.py
│
├── tests/
│   └── test_risk_engine.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── BUILDER_CENTER_ARTICLE.md
└── DEMO_SCRIPT.md
```

---

## ⚙️ Installation and Setup

### Prerequisites

Before running FarmGuard AI, install:

- Python 3.10 or later.
- Visual Studio Code.
- Git.
- AWS CLI.
- An AWS account with Amazon Bedrock model access.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/FarmGuard-AI.git

cd FarmGuard-AI
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### Step 4: Configure AWS Credentials

Configure AWS CLI:

```bash
aws configure
```

Provide your AWS credentials and preferred region.

Ensure that:
- Amazon Bedrock is available in your selected region.
- Your chosen foundation model is enabled.
- Your IAM identity has appropriate model invocation permissions.

Alternatively, configure an Amazon Bedrock API key through the `AWS_BEARER_TOKEN_BEDROCK` environment variable.

### Step 5: Configure Environment Variables

Copy `.env.example` to `.env`.

Example:

```env
AWS_REGION=us-west-2
AWS_DEFAULT_REGION=us-west-2

DEMO_MODE=false
```

Optional model configuration:

```env
BEDROCK_MODEL_ID=your-enabled-bedrock-model-id
```

Never upload AWS credentials, API keys or your `.env` file to GitHub.

### Step 6: Run the Application

```bash
streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

---

## 🚀 How to Use FarmGuard AI

1. Open the FarmGuard AI dashboard.
2. Enter your village or town.
3. Select your primary crop.
4. Choose the crop growth stage.
5. Select water availability and irrigation method.
6. Choose your preferred advisory language.
7. Click **Assess Climate Risk**.
8. Review the seven-day forecast and climate-risk indicators.
9. Click **Generate Multi-Agent Advisory**.
10. Review the climate, crop and water recommendations.
11. Visit the Impact Dashboard to view recorded assessments.

### Offline Demo

Enable **Use illustrative demo scenario (offline)** in the sidebar.

This mode:
- Uses sample weather data.
- Calculates a sample climate-risk score.
- Displays deterministic advisory text.
- Does not require AWS credentials.

The offline demonstration is not a live foundation-model invocation.

---

## 🧪 Testing

Run the automated tests:

```bash
pytest -q
```

The current test suite checks:
- High-risk classification under a hot and dry sample scenario.
- Lower risk classification under a mild and wetter sample scenario.

These tests validate the deterministic risk engine, not the live Bedrock integration or external weather API.

---

## 🌱 Social Impact

FarmGuard AI aims to contribute to climate resilience by making preparedness information more accessible to smallholder farmers.

Potential impact areas include:

- Better awareness of heat and dry-spell conditions.
- Improved understanding of weather information.
- Greater access to practical water-conservation guidance.
- Improved farm-worker heat-safety awareness.
- More accessible agricultural preparedness information.

### Impact Measurement

The prototype tracks:
- Number of climate assessments.
- Number of high-risk assessments.
- Crop categories.
- Advisory language selections.

These are usage indicators, not proof of reduced crop losses or improved yields. Field studies and expert evaluation would be needed to establish those outcomes.

---

## 🔐 Responsible AI and Limitations

FarmGuard AI is an experimental climate-preparedness decision-support prototype.

Important limitations:

- It does not provide official weather warnings.
- It does not diagnose crop diseases.
- It does not guarantee agricultural outcomes.
- Its risk thresholds are not validated for specific crops or regions.
- AI-generated recommendations may contain errors.
- It does not replace qualified agricultural professionals.

Always verify weather information through the India Meteorological Department (IMD) and crop-specific recommendations through local agricultural departments or Krishi Vigyan Kendras (KVKs).

---

## 🔮 Future Enhancements

Planned improvements include:

- Integration of verified IMD weather alerts.
- Satellite-based vegetation and crop-health indicators.
- Soil-moisture monitoring integration.
- Voice-based farmer assistance.
- Improved Marathi and Hindi conversational support.
- Crop-specific risk calibration with agricultural experts.
- Community-level climate-risk mapping.
- Agent evaluation and explainability reports.
- Mobile-friendly offline-first experience.

---

## 🏆 Hackathon Information

**Event:** AWS Builder Center – Strands SDK: Workshop to Ship

**Project:** FarmGuard AI

**Category:** Climate Resilience

**AI Framework:** AWS Strands Agents SDK

**Foundation Model Platform:** Amazon Bedrock

**Objective:** Build an original AI-agent solution addressing a real-world social challenge.

---

## 📚 References and Resources

- [AWS Strands Agents SDK](https://strandsagents.com/)
- [Strands Agents Documentation](https://strandsagents.com/latest/documentation/docs/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Open-Meteo Weather API](https://open-meteo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [India Meteorological Department](https://mausam.imd.gov.in/)

---

## 👨‍💻 Author

**Developed for the AWS Strands SDK: Workshop to Ship Hackathon 2026.**

GitHub Repository: https://github.com/prathamesh-1983/FarmGuard-AI

Demo Video: https://drive.google.com/file/d/1mucMnTsUcJ5XKUJ2kLmiCYjqyFTIKJ31/view?usp=sharing

---

### 🌾 FarmGuard AI

**Turning Climate Signals into Practical Farm Preparedness.**

*Building a more climate-resilient future through accessible and responsible AI.*
