import pandas as pd

# ACM
acm_el = pd.read_csv("eligibilityStep/acm_eligibility2123.csv")
print("ACM number of records for eligibility: ", len(acm_el['Eligibility_Score']))

acm_el =acm_el[(acm_el['Eligibility_Abstract_Score'] != 0) & (acm_el['Eligibility_Score'] != 0)]
acm_el.to_csv("eligibility_final_datasets/acm_eligibility_final.csv")
print("ACM number of records for eligibility: ", len(acm_el['Eligibility_Score']))

# IEEE
ieee_el = pd.read_csv("eligibilityStep/ieee_eligibility2123.csv")
print("IEEE number of records for eligibility: ", len(ieee_el['Eligibility_Score']))

ieee_el =ieee_el[(ieee_el['Eligibility_Abstract_Score'] != 0) & (ieee_el['Eligibility_Score'] != 0)]
ieee_el.to_csv("eligibility_final_datasets/ieee_eligibility_final.csv")
print("IEEE number of records for eligibility: ", len(ieee_el['Eligibility_Score']))

# Philpapers
philpapers_el = pd.read_csv("eligibilityStep/philpapers_eligibility2123.csv")
print("Philpapers number of records for eligibility: ", len(philpapers_el['Eligibility_Score']))

philpapers_el =philpapers_el[(philpapers_el['Eligibility_Abstract_Score'] != 0) & (philpapers_el['Eligibility_Score'] != 0)]
philpapers_el.to_csv("eligibility_final_datasets/philpapers_eligibility_final.csv")
print("Philpapers number of records for eligibility: ", len(philpapers_el['Eligibility_Score']))

# Springer
springer_el = pd.read_csv("eligibilityStep/springer_eligibility2123.csv")
print("Springer number of records for eligibility: ", len(springer_el['Eligibility_Score']))

springer_el =springer_el[(springer_el['Eligibility_Abstract_Score'] != 0) & (springer_el['Eligibility_Score'] != 0)]
springer_el.to_csv("eligibility_final_datasets/springer_eligibility_final.csv")
print("Springer number of records for eligibility: ", len(springer_el['Eligibility_Score']))
