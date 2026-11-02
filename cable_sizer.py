"""
Cable sizer: selects the smallest copper cable cross-section
that passes both the current-carrying capacity (Iz) and the
3 % voltage drop limit for a single-phase 230 V circuit.
"""

# Constants
RHO_CU = 0.0175
VOLTAGE = 230
LIMIT_OK = 3

# Iz in A: copper, PVC, 2 loaded conductors, method B1, 30 °C
# Source: IEC 60364-5-52 Table B.52.4 (verify against NEN 1010)
IZ_TABLE = {
    1.5: 17.5,
    2.5: 24,
    4: 32,
    6: 41,
    10: 57,
    16: 76,
    25: 101,
    35: 125,
    50: 151,
    70: 192,
    95: 232
}

def drop_percent(current, length, cross_section):
    """Calculates and returns the voltage drop percentage."""
    return (2 * length * current * RHO_CU / cross_section) / VOLTAGE * 100

# Decision Function
def select_cable(current, length):
    """Smallest cable size that passes Iz and 3 % voltage drop."""
    for cross_section, iz in IZ_TABLE.items():
        if iz >= current:
            voltage_drop_percent = drop_percent(current, length, cross_section)
            if voltage_drop_percent <= LIMIT_OK:
                return cross_section
    return None

# Main program
print("--- Cable selection (Iz + 3 % voltage drop) ---")


test_cases = [(16, 30), (30, 10), (50, 30), (16, 60), (16, 1171)]

for current, length in test_cases:
    selected_cross_section = select_cable(current, length)
    if selected_cross_section is not None: 
        print(f"✅ For current {current} A and length {length} m -> selected cross section: {selected_cross_section} mm²")
    else: 
        print(f"⚠️  For current {current} A and length {length} m ---> NOT SUITABLE cross section FOUND!")
