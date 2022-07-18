# Subtype 	 Type 	 Date 	 Date 	 Sequence 	 Cashier Name 	 Custom Data 	 USD Amount 
# END_OF_SHIFT = SUM by DATE( USD Amount , Type = "END_OF_SHIFT")+ SUM by DATE (USD AMOUNT, Type = "DEPOSIT", subtype is "" (blank))
import pandas as pd