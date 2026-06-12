from langchain.tools import tool

# Conversion factors to base units
CONVERSIONS = {
    # Length (meter)
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
    "mile": 1609.344,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,

    # Weight (kg)
    "kg": 1,
    "g": 0.001,
    "mg": 0.000001,
    "lb": 0.45359237,
    "oz": 0.0283495,

    # Time (second)
    "sec": 1,
    "min": 60,
    "hour": 3600,
    "day": 86400,
    "week": 604800,

    # Area (m²)
    "sqm": 1,
    "sqkm": 1_000_000,
    "acre": 4046.8564224,
    "hectare": 10000,

    # Volume (liter)
    "liter": 1,
    "ml": 0.001,
    "gallon": 3.78541,
    "quart": 0.946353,

    # Speed (m/s)
    "mps": 1,
    "kmph": 0.277778,
    "mph": 0.44704,

    # Data (byte)
    "byte": 1,
    "kb": 1024,
    "mb": 1024**2,
    "gb": 1024**3,
    "tb": 1024**4,
}


CATEGORIES = {
    "length": ["m", "km", "cm", "mm", "mile", "yard", "foot", "inch"],
    "weight": ["kg", "g", "mg", "lb", "oz"],
    "time": ["sec", "min", "hour", "day", "week"],
    "area": ["sqm", "sqkm", "acre", "hectare"],
    "volume": ["liter", "ml", "gallon", "quart"],
    "speed": ["mps", "kmph", "mph"],
    "data": ["byte", "kb", "mb", "gb", "tb"],
}


def get_category(unit):
    for category, units in CATEGORIES.items():
        if unit in units:
            return category
    return None


@tool
def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """
    Convert values between different units.

    Supported Categories:
    Length: m, km, cm, mm, mile, yard, foot, inch

    Weight: kg, g, mg, lb, oz

    Time: sec, min, hour, day, week

    Area: sqm, sqkm, acre, hectare

    Volume: liter, ml, gallon, quart

    Speed: mps, kmph, mph

    Data: byte, kb, mb, gb, tb
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in CONVERSIONS:
        return f"Unsupported unit: {from_unit}"

    if to_unit not in CONVERSIONS:
        return f"Unsupported unit: {to_unit}"

    from_category = get_category(from_unit)
    to_category = get_category(to_unit)

    if from_category != to_category:
        return (
            f"Cannot convert {from_unit} ({from_category}) "
            f"to {to_unit} ({to_category})"
        )

    base_value = value * CONVERSIONS[from_unit]
    result = base_value / CONVERSIONS[to_unit]

    return (
        f"{value} {from_unit} = "
        f"{result:.6f} {to_unit}"
    )
    
@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.
    Supported Units: C, F, K
    
    input example: convert_temperature(100, "C", "F")
    output example: "100.0 C = 212.000000 F"
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Convert to Celsius
    if from_unit == "c":
        c = value
    elif from_unit == "f":
        c = (value - 32) * 5 / 9
    elif from_unit == "k":
        c = value - 273.15
    else:
        raise ValueError("Invalid temperature unit")

    # Celsius -> target
    if to_unit == "c":
        return f"{c} °C"
    elif to_unit == "f":
        return f"{(c * 9 / 5) + 32} °F"
    elif to_unit == "k":
        return f"{c + 273.15} K"
    else:
        raise ValueError("Invalid temperature unit")
