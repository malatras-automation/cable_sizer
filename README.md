# Cable Sizer

A Python tool that selects the smallest copper cable cross-section for a
single-phase 230 V circuit. The chosen cable must pass two checks:

1. **Current-carrying capacity:** Iz of the cable ≥ circuit current
2. **Voltage drop:** ≤ 3 %

## How it works

- Iz values are stored in a dictionary (copper, PVC, method B1, 30 °C).
- The program checks the sizes from smallest to largest and returns
  the first one that passes both checks.
- If no standard size is enough, it reports that no suitable cable was found.

## How to run

`````````````````````
python cable_sizer.py
`````````````````````

## Example output

```````````````````````````````````````````````````````````````````````````````
--- Cable selection (Iz + 3 % voltage drop) ---
✅ For current 16 A and length 30 m -> selected cross section: 2.5 mm²
✅ For current 30 A and length 10 m -> selected cross section: 4 mm²
✅ For current 50 A and length 30 m -> selected cross section: 10 mm²
✅ For current 16 A and length 60 m -> selected cross section: 6 mm²
⚠️  For current 16 A and length 1171 m ---> NOT SUITABLE cross section FOUND!
```````````````````````````````````````````````````````````````````````````````



## Notes

Iz values follow the international standard IEC 60364-5-52 (Table B.52.4).
Most European national wiring rules are based on IEC 60364, for example
NEN 1010 (Netherlands), BS 7671 (United Kingdom) and DIN VDE 0100 (Germany).
Always verify the values against the standard that applies to your project.
This tool is not intended for installations under the US NEC.

## Author

Michalis Malatras, Electrical engineer, learning Python for industrial automation.
