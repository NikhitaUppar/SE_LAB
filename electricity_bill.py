RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}

def units_consumed(reading):
    if not isinstance(reading, str) or ':' not in reading:
        raise ValueError("Invalid reading format")
    parts = reading.split(':')
    if len(parts) != 2:
        raise ValueError("Invalid reading format")
    try:
        previous, current = parts
        return int(current) - int(previous)
    except ValueError:
        raise ValueError("Readings must be integers")

def daily_average(units_csv):
    if not isinstance(units_csv, str) or not units_csv.strip():
        raise ValueError("Invalid CSV input")
    try:
        units = [int(u.strip()) for u in units_csv.split(',') if u.strip()]
        if not units:
            raise ValueError("Empty units list")
        return round(sum(units) / len(units), 2)
    except ValueError:
        raise ValueError("Invalid integer in CSV")

def tariff_rate(code):
    if not isinstance(code, str) or '-' not in code:
        raise ValueError("Invalid tariff code format")
    parts = code.split('-')
    if len(parts) != 2:
        raise ValueError("Invalid tariff code format")
    category, slab = parts
    cat_key = category.strip().upper()
    slab_key = slab.strip().upper()
    if cat_key not in RATES or slab_key not in SLAB:
        raise KeyError("Unknown category or slab")
    return RATES[cat_key] * SLAB[slab_key]

def main():
    print("==== Running units_consumed ====")
    try:
        user_input = input("Enter meter readings as previous:current (e.g. 1200:1350): ")
        result = units_consumed(user_input)
        print("Units Consumed:", result)
    except Exception as e:
        print("Error:", e)

    print("\n==== Running daily_average ====")
    try:
        user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
        result = daily_average(user_input)
        print("Daily Average:", result)
    except Exception as e:
        print("Error:", e)

    print("\n==== Running tariff_rate ====")
    try:
        user_input = input("Enter a tariff code (e.g. DOM-A): ")
        result = tariff_rate(user_input)
        print("Rate per Unit:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()