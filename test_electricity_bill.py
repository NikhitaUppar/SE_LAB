import pytest
from electricity_bill import energy_charge, late_fee, subsidy

def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200

def test_paid_on_time():
    assert late_fee(500, 0) == 0

def test_energy_charge_unknown_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")

def test_energy_charge_invalid_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")

def test_energy_charge_mid_usage_domestic():
    # units = 200: 300 + (200 - 100) * 5 = 800. domestic fixed = 50 -> 850
    assert energy_charge(200, "domestic") == 850

def test_energy_charge_high_usage_domestic():
    # units = 350: 1300 + (350 - 300) * 8 = 1700. domestic fixed = 50 -> 1750
    assert energy_charge(350, "domestic") == 1750

def test_energy_charge_commercial():
    # units = 50: 50 * 3 = 150. commercial = 150 * 2 = 300. fixed = 150 -> 450
    assert energy_charge(50, "commercial") == 450

def test_energy_charge_mid_usage_commercial():
    # units = 200: charge = 800. commercial = 1600 + 150 = 1750
    assert energy_charge(200, "commercial") == 1750

def test_energy_charge_high_usage_commercial():
    # units = 350: charge = 1700. commercial = 3400 + 150 = 3550
    assert energy_charge(350, "commercial") == 3550

def test_late_fee_short_delay():
    assert late_fee(500, 10) == 50

def test_late_fee_long_delay_low_bill():
    assert late_fee(1500, 20) == 100

def test_late_fee_long_delay_high_bill():
    # 100 + 2500 // 20 = 100 + 125 = 225
    assert late_fee(2500, 20) == 225

def test_subsidy_senior_low_usage():
    assert subsidy(50, True, False) == 50

def test_subsidy_non_senior_low_usage():
    assert subsidy(50, False, False) == 0

def test_subsidy_with_solar_normal_usage():
    assert subsidy(150, False, True) == 100

def test_subsidy_senior_with_solar_normal_usage():
    assert subsidy(50, True, True) == 150

def test_subsidy_with_solar_high_usage():
    assert subsidy(350, True, True) == 0