# FarmGuard AI: Turning Climate Signals into Practical Farm Preparedness with Strands Agents

## The problem

Smallholder farmers face increasingly difficult decisions when heat and dry spells threaten crops, water availability and farm-worker safety. Forecasts are useful, but raw temperature and rainfall numbers do not always translate into understandable actions—especially when a farmer has limited access to personalized agricultural guidance.

I built **FarmGuard AI**, an agentic climate-preparedness prototype designed to help smallholder farmers interpret forecast signals and prepare practical next steps.

## What I built

FarmGuard AI combines a transparent climate-risk screening engine with a collaborative team of AI agents built using the **AWS Strands Agents SDK**.

A farmer enters a village or town, crop, growth stage, irrigation method and water-access constraints. The application retrieves a seven-day forecast, calculates explainable heat and dry-spell indicators, and then asks specialist agents to interpret the evidence and prepare a cautious action plan.

### The agent team

- **Climate specialist:** explains the supplied temperature and rainfall signals and their limitations.
- **Crop preparedness specialist:** suggests practical crop and worker-safety preparation options.
- **Water stewardship specialist:** suggests water-conservation and monitoring actions.
- **Coordinator:** delegates to the specialists and combines their findings into a clear advisory.

The project uses the Strands Agents SDK's agents-as-tools pattern. Each specialist has a focused role, while the coordinator is responsible for the final response.

## What makes it different

The core design principle is **Evidence-to-Action**. FarmGuard does not ask a language model to invent a forecast or generate unsupported risk claims. A deterministic Python risk engine calculates the indicators first. Specialist agents receive those observations and scores, explain the evidence, and create context-aware preparedness suggestions.

The application also includes a rule-based baseline so that a demo can compare deterministic threshold guidance with the richer multi-agent workflow.

## Technology

- Python
- AWS Strands Agents SDK
- Amazon Bedrock
- Streamlit
- Open-Meteo forecast and geocoding APIs
- SQLite
- Pandas and pytest

## Social impact and measurement

FarmGuard is intended to improve access to understandable climate-preparedness information for smallholder farmers. The prototype records the number of assessments, risk categories and advisory language selections in a local SQLite database.

These are usage and reach indicators, not proof of reduced crop losses or increased yields. A meaningful field evaluation would require farmer interviews, agronomist review, locally calibrated thresholds and a comparison over a growing season.

## Demo

[Insert public demo video link — under 3 minutes]

## Source code

[Insert public GitHub repository link]

## What I learned

This project helped me apply Strands Agents SDK beyond a single conversational agent. I used specialized agents as tools, designed a coordinator that delegates domain-specific work, and combined model-generated reasoning with deterministic code for evidence and safety.

## Limitations and responsible use

FarmGuard AI is a hackathon prototype. It is not an official weather alert, crop diagnosis system or replacement for local agricultural extension officers. The current risk thresholds are illustrative design assumptions and have not been validated for individual crops, soil types or districts. Farmers should verify weather information with official meteorological services and seek crop-specific guidance from their local Krishi Vigyan Kendra or agriculture department.

## Try it

[Insert repository link and setup instructions]

Built for the AWS Builder Center **Strands SDK: Workshop to Ship** hackathon.
