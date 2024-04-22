import pandas as pd

acm = pd.read_csv("acm.12.20-10.23.no.dups.with.all.csv")

print("\nACM number of missing abstarct: \n", len(acm['Abstract'][acm['Abstract'].isna()]))
print(acm['URL'][acm['Abstract'].isna()])

ieee = pd.read_csv("IEEE.21-23.no.dups.with.all.csv")

print("\nIEEE number of missing abstarct: \n", len(ieee['Abstract'][ieee['Abstract'].isna()]))
print(ieee['URL'][ieee['Abstract'].isna()])

philpapers = pd.read_csv("philpapers2123N.csv")

print("\nPhilpapers number of missing abstarct: \n",len(philpapers['Abstract'][philpapers['Abstract'].isna()]))
print(philpapers['URL'][philpapers['Abstract'].isna()])

springer = pd.read_csv("springer2123N.csv")

print("\nSpringer number of missing abstarct: \n",len(springer['Abstract'][springer['Abstract'].isna()]))
print(springer['URL'][springer['Abstract'].isna()])

print(list(acm.columns))

import re

# function to remove special characters and clean the Abstracts
def remove_special_characters_lower(input_string):
    # Define a regular expression pattern to match non-alphanumeric characters excluding spaces
    pattern = re.compile('[^A-Za-z0-9 ]+')
    
    # Use the pattern to replace special characters with an empty string
    result_string = pattern.sub('', input_string).lower()
    
    return result_string

def get_eligibility_score(cleaned_string, keywords):
    
    count = 0
    total_count = 0
    word_list = cleaned_string.split(" ")

    for word in word_list:
        if word in keywords:
            count += keywords[word]
            total_count += 1
        else:
            total_count += 1

    eligibility_score = count/total_count
    return eligibility_score

def copy_values_into_df_pd(columns_list, df1, df2, i):
    for column in columns_list:
        df1.loc[i, column] = df2[column].loc[i]

def get_avg_3(element1, element2, element3, string1, string2, string3):
    len_1 = len(string1)
    len_2 = len(string2)
    len_3 = len(string3)
    total_len = len_1 + len_2 + len_3
    avg_value = element1 * (len_1/total_len) + element2 * (len_2/total_len) + element3 * (len_3/total_len)
    return avg_value

def get_avg_2(element1, element2, string1, string2):
    len_1 = len(string1)
    len_2 = len(string2)
    total_len = len_1 + len_2
    avg_value = element1 * (len_1/total_len) + element2 * (len_2/total_len)
    return avg_value

keywords = {
    'ai': 1,
    'ethical': 3,
    'digital': 2,
    'ethics': 2,
    'data': 1, 
    'autonomy': 1,
    'discrimination': 1,
    'domination': 1,
    'exclusion': 1,
    'exploitation': 1,
    'inequality': 1,
    'justice': 1,
    'privacy': 1,
    'responsibility': 1,
    'trust': 1,
    'dignity': 1,
    'truth': 1,
}

# ACM
acm_eligibility = pd.DataFrame()

i = 0
for i in range(len(acm['Abstract'])):

    if isinstance(acm['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(acm.loc[i, "Abstract"])
        eligibility_abstract_score = get_eligibility_score(cleaned_string, keywords)

        keywords_are_there = False
        keywords_length = ""
        if isinstance(acm['Keywords'].loc[i], str):
            keywords_are_there = True
            keywords_length = acm.loc[i, 'Keywords']
            cleaned_string = remove_special_characters_lower(acm.loc[i, "Keywords"])
            eligibility_keywords_score = get_eligibility_score(cleaned_string, keywords)
        
        cleaned_string = remove_special_characters_lower(acm.loc[i, "Title"])
        eligibility_title_score = get_eligibility_score(cleaned_string, keywords)

        copy_values_into_df_pd(list(acm.columns), acm_eligibility, acm, i)
        
        acm_eligibility.loc[i, "Eligibility_Abstract_Score"] = eligibility_abstract_score
        if keywords_are_there:
            acm_eligibility.loc[i, "Eligibility_Keywords_Score"] = eligibility_keywords_score
        else:
            acm_eligibility.loc[i, "Eligibility_Keywords_Score"] = 0
        acm_eligibility.loc[i, "Eligibility_Title_Score"] = eligibility_title_score

        acm_eligibility.loc[i, "Eligibility_Score"] = get_avg_3(acm_eligibility.loc[i, "Eligibility_Abstract_Score"],
                                                                acm_eligibility.loc[i, "Eligibility_Keywords_Score"],
                                                                acm_eligibility.loc[i, "Eligibility_Title_Score"],
                                                                acm_eligibility.loc[i, "Abstract"],
                                                                keywords_length,
                                                                acm_eligibility.loc[i, "Title"])


acm_eligibility = acm_eligibility.sort_values(by='Eligibility_Score', ascending=False)
acm_eligibility = acm_eligibility.reset_index(drop=True)
acm_eligibility.to_csv("eligibilityStep/acm_eligibility2123.csv")

# IEEE
ieee_eligibility = pd.DataFrame()

i = 0
for i in range(len(ieee['Abstract'])):

    if isinstance(ieee['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(ieee.loc[i, "Abstract"])
        eligibility_abstract_score = get_eligibility_score(cleaned_string, keywords)

        keywords_are_there = False
        keywords_length = ""
        if isinstance(ieee['Keywords'].loc[i], str):
            keywords_are_there = True
            keywords_length = ieee.loc[i, 'Keywords']
            cleaned_string = remove_special_characters_lower(ieee.loc[i, "Keywords"])
            eligibility_keywords_score = get_eligibility_score(cleaned_string, keywords)
        
        cleaned_string = remove_special_characters_lower(ieee.loc[i, "Title"])
        eligibility_title_score = get_eligibility_score(cleaned_string, keywords)

        copy_values_into_df_pd(list(ieee.columns), ieee_eligibility, ieee, i)
        
        ieee_eligibility.loc[i, "Eligibility_Abstract_Score"] = eligibility_abstract_score
        if keywords_are_there:
            ieee_eligibility.loc[i, "Eligibility_Keywords_Score"] = eligibility_keywords_score
        else:
            ieee_eligibility.loc[i, "Eligibility_Keywords_Score"] = 0
        ieee_eligibility.loc[i, "Eligibility_Title_Score"] = eligibility_title_score

        ieee_eligibility.loc[i, "Eligibility_Score"] = get_avg_3(ieee_eligibility.loc[i, "Eligibility_Abstract_Score"],
                                                                ieee_eligibility.loc[i, "Eligibility_Keywords_Score"],
                                                                ieee_eligibility.loc[i, "Eligibility_Title_Score"],
                                                                ieee_eligibility.loc[i, "Abstract"],
                                                                keywords_length,
                                                                ieee_eligibility.loc[i, "Title"])

ieee_eligibility = ieee_eligibility.sort_values(by='Eligibility_Score', ascending=False)
ieee_eligibility = ieee_eligibility.reset_index(drop=True)
ieee_eligibility.to_csv("eligibilityStep/ieee_eligibility2123.csv")

# Philpapers
philpapers_eligibility = pd.DataFrame()

i = 0
for i in range(len(philpapers['Abstract'])):

    if isinstance(philpapers['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(philpapers.loc[i, "Abstract"])
        eligibility_abstract_score = get_eligibility_score(cleaned_string, keywords)
        
        cleaned_string = remove_special_characters_lower(philpapers.loc[i, "Title"])
        eligibility_title_score = get_eligibility_score(cleaned_string, keywords)

        copy_values_into_df_pd(list(philpapers.columns), philpapers_eligibility, philpapers, i)
        
        philpapers_eligibility.loc[i, "Eligibility_Abstract_Score"] = eligibility_abstract_score
        philpapers_eligibility.loc[i, "Eligibility_Title_Score"] = eligibility_title_score

        philpapers_eligibility.loc[i, "Eligibility_Score"] = get_avg_2(philpapers_eligibility.loc[i, "Eligibility_Abstract_Score"],
                                                                philpapers_eligibility.loc[i, "Eligibility_Title_Score"],
                                                                philpapers_eligibility.loc[i, "Abstract"],
                                                                philpapers_eligibility.loc[i, "Title"])

philpapers_eligibility = philpapers_eligibility.sort_values(by='Eligibility_Score', ascending=False)
philpapers_eligibility = philpapers_eligibility.reset_index(drop=True)
philpapers_eligibility.to_csv("eligibilityStep/philpapers_eligibility2123.csv")

# Springer
springer_eligibility = pd.DataFrame()

i = 0
for i in range(len(springer['Abstract'])):

    if isinstance(springer['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(springer.loc[i, "Abstract"])
        eligibility_abstract_score = get_eligibility_score(cleaned_string, keywords)
        
        cleaned_string = remove_special_characters_lower(springer.loc[i, "Title"])
        eligibility_title_score = get_eligibility_score(cleaned_string, keywords)

        copy_values_into_df_pd(list(springer.columns), springer_eligibility, springer, i)
        
        springer_eligibility.loc[i, "Eligibility_Abstract_Score"] = eligibility_abstract_score
        springer_eligibility.loc[i, "Eligibility_Title_Score"] = eligibility_title_score

        springer_eligibility.loc[i, "Eligibility_Score"] = get_avg_2(springer_eligibility.loc[i, "Eligibility_Abstract_Score"],
                                                                springer_eligibility.loc[i, "Eligibility_Title_Score"],
                                                                springer_eligibility.loc[i, "Abstract"],
                                                                springer_eligibility.loc[i, "Title"])

springer_eligibility = springer_eligibility.sort_values(by='Eligibility_Score', ascending=False)
springer_eligibility = springer_eligibility.reset_index(drop=True)
springer_eligibility.to_csv("eligibilityStep/springer_eligibility2123.csv")

