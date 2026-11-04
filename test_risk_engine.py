from farmguard.risk_engine import score_climate_risk

def test_hot_dry_scenario_scores_high():
    weather = {"daily": {
        "temperature_2m_max": [38,39,40,38,37,39,38],
        "precipitation_sum": [0,0,0,0,0,0,0],
        "relative_humidity_2m_mean": [30,29,28,30,31,29,30]
    }}
    result = score_climate_risk(weather)
    assert result.level == "High"
    assert result.overall_score >= 65
    assert result.heat_score > 0
    assert result.dry_spell_score == 100

def test_mild_wet_scenario_is_lower_than_hot_dry():
    weather = {"daily": {
        "temperature_2m_max": [28,29,29,28,27,28,29],
        "precipitation_sum": [4,5,2,3,6,2,4],
        "relative_humidity_2m_mean": [60,62,65,61,63,60,64]
    }}
    result = score_climate_risk(weather)
    assert result.level == "Low"
