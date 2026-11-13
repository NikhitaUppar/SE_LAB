from electricity_bill import units_consumed, daily_average, tariff_rate
import random
import string

def generate_random_inputs(n=50):
    """Generates a list of random/malformed strings and None for fuzzing."""
    inputs = [None, "", "1200", "1200:1350:1400", "abc:xyz", "1200:1350", "5,6,7", "5,,7", "DOM-A", "INVALID-Z", "-10:20"]
    for _ in range(n):
        # Generate random text inputs
        rand_str = ''.join(random.choices(string.ascii_letters + string.digits + ",:- ", k=random.randint(0, 15)))
        inputs.append(rand_str)
    return inputs

def test_units_consumed_no_crash():
    for val in generate_random_inputs():
        try:
            units_consumed(val)
        except (ValueError, AttributeError, IndexError, TypeError):
            pass

def test_daily_average_no_crash():
    for val in generate_random_inputs():
        try:
            daily_average(val)
        except (ValueError, AttributeError, ZeroDivisionError, TypeError):
            pass

def test_tariff_rate_no_crash():
    for val in generate_random_inputs():
        try:
            tariff_rate(val)
        except (ValueError, AttributeError, KeyError, TypeError):
            pass

if __name__ == "__main__":
    print("Running custom fuzz tests...")
    test_units_consumed_no_crash()
    test_daily_average_no_crash()
    test_tariff_rate_no_crash()
    print("All fuzz tests executed successfully!")