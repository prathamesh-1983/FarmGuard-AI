import json
import os
from datetime import datetime
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from farmguard.weather import geocode_location, fetch_forecast, demo_weather
from farmguard.risk_engine import score_climate_risk
from farmguard.agents import generate_advisory
from farmguard.baseline import baseline_advice
from farmguard.storage import save_assessment, get_metrics

load_dotenv()
st.set_page_config(page_title="FarmGuard AI", page_icon="🌾", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#071b18 0%,#102c24 55%,#14251f 100%); color:#f3f7ef;}
section[data-testid="stSidebar"] {background:#0b211b;}
div[data-testid="stMetric"] {background:#16372c;padding:16px;border-radius:14px;border:1px solid #315b45;}
.hero {padding:26px;border-radius:20px;background:linear-gradient(110deg,#174b35,#286343);border:1px solid #4d8b61;}
.small-muted {color:#c5d7c8;font-size:0.9rem;}
</style>
""", unsafe_allow_html=True)

if "assessment" not in st.session_state:
    st.session_state.assessment = None

with st.sidebar:
    st.title("🌾 FarmGuard AI")
    st.caption("Climate intelligence for smallholder farmers")
    st.divider()
    location_name = st.text_input("Village / town", "Nashik, Maharashtra")
    crop = st.selectbox("Primary crop", ["Grapes","Onion","Cotton","Soybean","Rice","Wheat","Vegetables","Other"])
    growth_stage = st.selectbox("Crop growth stage", ["Sowing / planting","Vegetative","Flowering","Fruiting / grain filling","Maturity / harvest"])
    water_access = st.selectbox("Water access", ["Reliable irrigation","Limited irrigation","Rain-fed","Community/shared source"])
    irrigation_type = st.selectbox("Irrigation method", ["Drip","Sprinkler","Flood / furrow","Manual","Not applicable"])
    language = st.selectbox("Preferred advisory language", ["English","Hindi","Marathi"])
    constraints = st.text_area("Farm constraints (optional)", "Small farm; limited budget")
    demo_mode = st.toggle("Use illustrative demo scenario (offline)", value=False)
    run_button = st.button("🌦️ Assess climate risk", type="primary", use_container_width=True)

st.markdown("""
<div class="hero">
  <h1>🌱 FarmGuard AI</h1>
  <h3>From climate signals to practical farm preparedness.</h3>
  <p class="small-muted">An agentic climate-resilience assistant designed for smallholder farmers.</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Risk assessment","Farm action plan","Impact dashboard","About & safety"])

if run_button:
    try:
        with st.spinner("Collecting weather signals and calculating transparent risk indicators..."):
            if demo_mode:
                location, weather = demo_weather()
            else:
                location = geocode_location(location_name)
                weather = fetch_forecast(location["latitude"], location["longitude"], location.get("timezone","auto"))
            risk = score_climate_risk(weather).to_dict()
            farmer = {"crop":crop,"growth_stage":growth_stage,"water_access":water_access,
                      "irrigation_type":irrigation_type,"language":language,"constraints":constraints}
        st.session_state.assessment = {"location":location,"weather":weather,"risk":risk,"farmer":farmer,"demo":demo_mode}
    except Exception as exc:
        st.error(f"Unable to complete weather assessment: {exc}")
        st.info("Try the illustrative demo scenario, or check your internet connection.")

assessment = st.session_state.assessment

with tab1:
    if assessment:
        risk = assessment["risk"]
        loc = assessment["location"]
        st.subheader(f"Assessment: {loc['name']}, {loc.get('admin1','')}")
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Overall screening score", f"{risk['overall_score']}/100")
        c2.metric("Risk level", risk["level"])
        c3.metric("Heat indicator", f"{risk['heat_score']}/100")
        c4.metric("Dry-spell indicator", f"{risk['dry_spell_score']}/100")
        if assessment["demo"]:
            st.warning("Illustrative demo data — not a live forecast.")
        daily = assessment["weather"]["daily"]
        frame = pd.DataFrame({
            "Date":daily["time"],
            "Max temperature (°C)":daily["temperature_2m_max"],
            "Rainfall (mm)":daily["precipitation_sum"],
            "Rain probability (%)":daily.get("precipitation_probability_max",[None]*len(daily["time"]))
        })
        st.markdown("#### Seven-day forecast signals")
        st.dataframe(frame, use_container_width=True, hide_index=True)
        st.markdown("#### Why this score?")
        for signal in risk["signals"]:
            st.write("• " + signal)
        with st.expander("Scoring method and limitations"):
            st.write("The score combines heat (40%), dry-day frequency (35%) and low forecast rainfall (25%) using transparent threshold-based indicators.")
            for item in risk["limitations"]:
                st.write("• " + item)
    else:
        st.info("Enter farm details in the sidebar and select Assess climate risk. You can start with the offline demo.")

with tab2:
    if assessment:
        st.subheader("Agentic farm preparedness")
        if st.button("🤖 Generate multi-agent advisory", type="primary"):
            try:
                with st.spinner("Climate, crop and water specialists are collaborating..."):
                    advisory = generate_advisory(assessment["location"], assessment["weather"],
                                                  assessment["risk"], assessment["farmer"],
                                                  demo=assessment["demo"])
                st.session_state.advisory = advisory
                st.session_state.baseline = baseline_advice(assessment["risk"], assessment["farmer"]["crop"])
                save_assessment(assessment["location"]["name"], assessment["farmer"]["crop"],
                                assessment["risk"]["level"], assessment["risk"]["overall_score"],
                                assessment["farmer"]["language"], st.session_state.baseline)
            except Exception as exc:
                st.error(f"Agent run failed: {exc}")
                st.info("Check AWS credentials, Bedrock model access, region and IAM permissions. You can still use the deterministic risk assessment.")
        if st.session_state.get("advisory"):
            if assessment["demo"]:
                st.warning("This is deterministic sample output. It does not invoke a live foundation model.")
            st.markdown(st.session_state.advisory)
        if st.session_state.get("baseline"):
            with st.expander("Compare with the transparent rule-based baseline"):
                st.write("The baseline uses only deterministic thresholds; the agentic advisory adds specialist interpretation and contextual planning.")
                for action in st.session_state.baseline:
                    st.write("• " + action)
    else:
        st.info("Run a risk assessment first.")

with tab3:
    st.subheader("Community impact evidence")
    metrics = get_metrics()
    a,b = st.columns(2)
    a.metric("Assessments recorded", metrics["assessments"])
    b.metric("High-risk assessments", metrics["high_risk"])
    st.caption("Local demo database only. These counts are usage indicators, not proof of reduced crop losses.")
    if metrics["rows"]:
        df = pd.DataFrame(metrics["rows"], columns=["Created (UTC)","Location","Crop","Risk","Score","Language"])
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No assessments saved yet. Generate an advisory to create the first local record.")

with tab4:
    st.subheader("What FarmGuard AI is — and is not")
    st.write("FarmGuard AI is a climate preparedness decision-support prototype. It interprets forecast indicators and generates cautious actions.")
    st.warning("It is not an official weather alert, a crop-disease diagnostic system, or a replacement for agricultural extension officers.")
    st.write("For real-world use, verify forecasts with India Meteorological Department (IMD), and crop-specific guidance with your local Krishi Vigyan Kendra (KVK) or agriculture department.")
    st.write("Weather data provider: Open-Meteo. Review its terms and attribution requirements before public deployment.")
    st.write("Emergency: follow local government and health-authority instructions. For heat illness, move to a cooler place and seek medical help for severe symptoms.")

st.caption("FarmGuard AI • Built with Python, Streamlit and AWS Strands Agents SDK • Hackathon prototype")
