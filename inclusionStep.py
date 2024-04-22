import pandas as pd

# ACM
acm_el = pd.read_csv("eligibility_final_datasets//acm_eligibility_final.csv")
print("ACM number of records for eligibility: ", len(acm_el['Eligibility_Score']))

acm_in = acm_el[(acm_el['Abstract'].str.len() > 120) & 
        (acm_el['Eligibility_Score'] > 0.15) & 
        (acm_el['Eligibility_Abstract_Score'] > 0.12)]
acm_in.to_csv('inclusionStep/acm_inclusion_final.csv')
print("ACM number of records for inclusion: ", len(acm_in['Eligibility_Score']))

# IEEE
ieee_el = pd.read_csv("eligibility_final_datasets//ieee_eligibility_final.csv")
print("IEEE number of records for eligibility: ", len(ieee_el['Eligibility_Score']))

ieee_in = ieee_el[(ieee_el['Abstract'].str.len() > 120) & 
        (ieee_el['Eligibility_Score'] > 0.14) & 
        (ieee_el['Eligibility_Abstract_Score'] > 0.12)]
ieee_in.to_csv('inclusionStep/ieee_inclusion_final.csv')
print("IEEE number of records for inclusion: ", len(ieee_in['Eligibility_Score']))

# Philpapers
philpapers_el = pd.read_csv("eligibility_final_datasets//philpapers_eligibility_final.csv")
print("Philpapers number of records for eligibility: ", len(philpapers_el['Eligibility_Score']))

philpapers_in = philpapers_el[(philpapers_el['Abstract'].str.len() > 120) & 
        (philpapers_el['Eligibility_Score'] > 0.12) & 
        (philpapers_el['Eligibility_Abstract_Score'] > 0.12)]
philpapers_in.to_csv('inclusionStep/philpapers_inclusion_final.csv')
print("Philpapers number of records for inclusion: ", len(philpapers_in['Eligibility_Score']))

# Springer
springer_el = pd.read_csv("eligibility_final_datasets//springer_eligibility_final.csv")
print("Springer number of records for eligibility: ", len(springer_el['Eligibility_Score']))

springer_in = springer_el[(springer_el['Abstract'].str.len() > 120) & 
        (springer_el['Eligibility_Score'] > 0.15) & 
        (springer_el['Eligibility_Abstract_Score'] > 0.16)]
springer_in.to_csv('inclusionStep/springer_inclusion_final.csv')
print("Springer number of records for inclusion: ", len(springer_in['Eligibility_Score']))