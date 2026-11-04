# FarmGuard AI — 2 minute 40 second demo script

**Important:** Record a real run. Do not show fabricated terminal output, fake model traces or unverified impact claims. If using offline demo mode, say that it is sample data and not a live model invocation.

## 0:00–0:20 — The problem
"Smallholder farmers receive weather forecasts, but raw weather numbers do not always explain what actions to take. FarmGuard AI turns climate signals into understandable preparedness guidance."

## 0:20–0:40 — Introduce the app
Show the Streamlit dashboard and sidebar. Explain the farmer inputs: location, crop, growth stage, water access, irrigation and language.

## 0:40–1:05 — Show the evidence
Run the assessment. Show the seven-day forecast, temperature, rainfall, heat indicator, dry-spell indicator and transparent risk score. Point out that the score is a screening prototype, not an official alert.

## 1:05–1:45 — Show Strands multi-agent workflow
Click "Generate multi-agent advisory" with demo mode OFF and a working Bedrock connection. Explain:
- Climate specialist interprets the evidence.
- Crop specialist suggests preparedness options.
- Water specialist proposes conservation actions.
- Coordinator synthesizes the response.

Show the real result and, if possible, the Strands tool-call trace from the terminal or logs.

## 1:45–2:10 — Originality
Explain Evidence-to-Action: each recommendation is grounded in supplied forecast indicators, with deterministic scoring separated from LLM interpretation. Show the baseline comparison.

## 2:10–2:30 — Social impact
Show the impact dashboard. Explain that assessment counts are usage indicators; field studies are needed to prove changes in crop outcomes.

## 2:30–2:40 — Close
"FarmGuard AI is a prototype for more accessible climate preparedness. Built with Python, Streamlit, Amazon Bedrock and AWS Strands Agents SDK."

## Recording checklist
- Public video link works in an incognito window.
- Total runtime is below 3 minutes.
- Text is readable and audio is clear.
- Show the real working application.
- Show at least one real Strands agent invocation.
- Do not expose AWS keys, tokens, personal data or account IDs.
- Do not claim field validation or reduced crop loss unless independently measured.
