import pandas as pd

df = pd.read_csv("cleandups/all.together.21-23.without.dups.csv")

df_nodups = df.dropna(subset=["DOI"])

all_doi_acm = df_nodups[df_nodups["Library"] == "ACM" ]["DOI"]
acm_df = pd.read_csv("cleandups/acm.12.20-10.23.no.dups.csv")
print(acm_df.shape[0])
filtered_acm = acm_df[acm_df['DOI'].isin(all_doi_acm)]
print(filtered_acm.shape[0])
filtered_acm.to_csv("cleandups/acm.12.20-10.23.no.dups.with.all.csv")


all_doi_philpapers = df_nodups[df_nodups["Library"] == "Philpapers" ]["DOI"]
philpapers_df = pd.read_csv("cleandups/Philpapers.21-23.no-dups.csv")
print(philpapers_df.shape[0])
filtered_philpapers = philpapers_df[philpapers_df['DOI'].isin(all_doi_philpapers)]
print(filtered_philpapers.shape[0])
filtered_philpapers.to_csv("cleandups/Philpapers.21-23.no-dups.with.all.csv")


all_doi_springer = df_nodups[df_nodups["Library"] == "Springer" ]["DOI"]
springer_df = pd.read_csv("cleandups/Springer.21-23.appended.no.dups.last.csv")
print(springer_df.shape[0])
filtered_springer = springer_df[springer_df['Item DOI'].isin(all_doi_springer)]
print(filtered_springer.shape[0])
filtered_springer.to_csv("cleandups/Springer.21-23.appended.no.dups.with.all.csv")


all_doi_ieee = df_nodups[df_nodups["Library"] == "IEEE" ]["DOI"]
ieee_df = pd.read_csv("cleandups/IEEE.21-23.no.dups.csv")
print(ieee_df.shape[0])
filtered_ieee = ieee_df[ieee_df['DOI'].isin(all_doi_ieee)]
print(filtered_ieee.shape[0])
filtered_ieee.to_csv("cleandups/IEEE.21-23.no.dups.with.all.csv")