# Subtype 	 Type 	 Date 	 Date 	 Sequence 	 Cashier Name 	 Custom Data 	 USD Amount 
# END_OF_SHIFT = SUM by DATE( USD Amount , Type = "END_OF_SHIFT")+ SUM by DATE (USD AMOUNT, Type = "DEPOSIT", subtype is "" (blank))

# Tills Pulled = SUM by DATE( all BLANK "" subtype, type = DISPENSE) - SUBTRACT (DISPENSE with no custom data (Need User Input))

# Total Cash Sales = End of Shift + Tills



import pandas as pd
import numpy as np
import openpyxl