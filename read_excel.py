import pandas as pd
import sys

try:
    xls = pd.ExcelFile('Cash Flow for High Springs Mobil (Commission).xlsx')
    print('Sheet names:', xls.sheet_names)

    for sheet in xls.sheet_names:
        print(f'\n{"="*60}')
        print(f'SHEET: {sheet}')
        print(f'{"="*60}')
        df = pd.read_excel(xls, sheet_name=sheet)
        print(df.to_string())
        print()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
