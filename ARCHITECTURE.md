# Architecture notes

```text
Farmer
  |
  v
Streamlit UI
  |
  +--> Geocoding + 7-day forecast (Open-Meteo)
  |
  +--> Deterministic climate risk engine (Python)
  |       heat / dry-day / low-rain indicators
  |
  v
Strands Coordinator Agent (Amazon Bedrock)
  |
  +--> Climate Specialist Agent (as_tool)
  |       evidence interpretation
  |
  +--> Crop Preparedness Agent (as_tool)
  |       crop-stage-aware cautious actions
  |
  +--> Water Stewardship Agent (as_tool)
  |       conservation and monitoring options
  |
  v
Synthesized advisory + evidence + limitations
  |
  +--> Rule-based baseline comparison
  +--> SQLite local assessment metrics
  +--> Streamlit impact dashboard
```

## Trust boundaries
- Weather provider response is external input and must be treated as untrusted data.
- Risk score is deterministic, transparent, and separate from LLM-generated advice.
- Agent output is advisory text and must not be presented as an official warning.
- Database is local demo storage; do not store sensitive farmer data.
- Bedrock credentials are supplied through AWS configuration / environment, never source control.
