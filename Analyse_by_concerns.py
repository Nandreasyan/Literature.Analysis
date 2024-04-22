from gc import get_count
import pandas as pd
import re


acm = pd.read_csv("inclusionStep/acm_inclusion_final.csv")
ieee = pd.read_csv("inclusionStep/ieee_inclusion_final.csv")
philpapers = pd.read_csv("inclusionStep/philpapers_inclusion_final.csv")
springer = pd.read_csv("inclusionStep/springer_inclusion_final.csv")


def remove_special_characters_lower(input_string):

    pattern = re.compile('[^A-Za-z0-9 ]+')
    result_string = pattern.sub('', input_string).lower()
    return result_string


def get_score(cleaned_string, keywords):
    
    count = 0
    total_count = 0
    word_list = cleaned_string.split(" ")
    for word in word_list:
        if word in keywords:
            count += keywords[word]
            total_count += 1
        else:
            total_count += 1
    score = count/total_count
    return score

def get_count_library(library, keywords):
    count = 0
    for i in library.index:
        
        score = 0
        
        string_1 = library.loc[i, "Title"]
        string_2 = library.loc[i, "Abstract"]

        cleaned_string_1 = remove_special_characters_lower(string_1)
        cleaned_string_2 = remove_special_characters_lower(string_2)

        score += get_score(cleaned_string_1, keywords)
        score += get_score(cleaned_string_2, keywords)

        if score > 0:
            count += 1

    return count


# keywords

autonomy_keywords = {
    'autonomy': 1,
    'autonomous': 1,
    'self-governance': 1,
    'independence': 1,
    'self-determination': 1,
    'freedom': 1,
    'self-rule': 1,
    'agency': 1,
    'self-sufficiency': 1,
    'liberty': 1,
    'sovereignty': 1,
    'empowerment': 1,
    'individualism': 1,
    'self-direction': 1,
    'self-reliance': 1,
    'personal choice': 1,
    'self-regulation': 1,
    'self-control': 1,
    'decentralization': 1,
}

discrimination_keywords = {
    'discrimination': 1,
    'bias': 1,
    'prejudice': 1,
    'inequality': 1,
    'racism': 1,
    'sexism': 1,
    'ageism': 1,
    'homophobia': 1,
    'xenophobia': 1,
    'intolerance': 1,
    'stereotyping': 1,
    'bigotry': 1,
    'unfairness': 1,
    'inequity': 1,
    'marginalization': 1,
    'exclusion': 1,
    'oppression': 1,
    'victimization': 1,
    'classism': 1,
    'ableism': 1,
}

domination_keywords = {
    'domination': 1,
    'control': 1,
    'power': 1,
    'authority': 1,
    'supremacy': 1,
    'hegemony': 1,
    'subjugation': 1,
    'oppression': 1,
    'tyranny': 1,
    'dictatorship': 1,
    'autocracy': 1,
    'imperialism': 1,
    'colonialism': 1,
    'exploitation': 1,
    'manipulation': 1,
    'coercion': 1,
    'authoritarianism': 1,
    'monopoly': 1,
    'overpowering': 1,
    'subordination': 1,
    'rulership': 1,
    'dominance': 1,
    'totalitarianism': 1,
    'sovereignty': 1,
}

exclusion_keywords = {
    'exclusion': 1,
    'isolation': 1,
    'marginalization': 1,
    'segregation': 1,
    'discrimination': 1,
    'ostracism': 1,
    'alienation': 1,
    'disenfranchisement': 1,
    'rejection': 1,
    'outsider': 1,
    'ghettoization': 1,
    'apartheid': 1,
    'inequality': 1,
    'neglect': 1,
    'ignoring': 1,
    'sidelining': 1,
    'barring': 1,
    'elitism': 1,
    'non-inclusion': 1,
    'casteism': 1,
    'divisiveness': 1,
    'disconnection': 1,
    'isolationism': 1,
    'xenophobia': 1,
}

exploitation_keywords = {
    'exploitation': 1,
    'abuse': 1,
    'manipulation': 1,
    'oppression': 1,
    'misuse': 1,
    'overuse': 1,
    'enslavement': 1,
    'usurpation': 1,
    'profiteering': 1,
    'subjugation': 1,
    'victimization': 1,
    'extraction': 1,
    'overexploitation': 1,
    'embezzlement': 1,
    'fraud': 1,
    'depletion': 1,
    'colonialism': 1,
    'imperialism': 1,
}

inequality_keywords = {
    'inequality': 1,
    'disparity': 1,
    'imbalance': 1,
    'unevenness': 1,
    'discrimination': 1,
    'unfairness': 1,
    'inequity': 1,
    'bias': 1,
    'prejudice': 1,
    'disadvantage': 1,
    'exclusion': 1,
    'marginalization': 1,
}

justice_keywords = {
    'justice': 1,
    'fairness': 1,
    'equality': 1,
    'rights': 1,
    'law': 1,
    'legal': 1,
    'judicial': 1,
    'retribution': 1,
    'redress': 1,
    'reparation': 1,
    'compensation': 1,
    'impartiality': 1,
    'accountability': 1,
    'morality': 1,
    'judgement': 1,
    'adjudication': 1,
    'jurisprudence': 1,
}

privacy_keywords = {
    'privacy': 1,
    'confidentiality': 1,
    'anonymity': 1,
    'secrecy': 1,
    'discretion': 1,
    'solitude': 1,
    'intimacy': 1,
    'non-disclosure': 1,
    'encryption': 1,
    'cybersecurity': 1,
    'consent': 1,
    'hipaa': 1,
    'gdpr': 1,
    'surveillance': 1,
}

responsibility_keywords = {
    'responsibility': 1,
    'accountability': 1,
    'duty': 1,
    'obligation': 1,
    'liability': 1,
    'answerability': 1,
    'stewardship': 1,
    'commitment': 1,
    'trustworthiness': 1,
    'integrity': 1,
    'conscientiousness': 1,
    'dependability': 1,
    'sustainability': 1,
    'custodianship': 1,
    'ownership': 1,
    'professionalism': 1,
}

trust_keywords = {
    'trust': 1,
    'reliability': 1,
    'confidence': 1,
    'faith': 1,
    'credibility': 1,
    'assurance': 1,
    'dependability': 1,
    'honesty': 1,
    'integrity': 1,
    'loyalty': 1,
    'trustworthiness': 1,
    'belief': 1,
    'fidelity': 1,
    'authenticity': 1,
    'transparency': 1,
    'security': 1,
    'commitment': 1,
    'consistency': 1,
    'expectation': 1,
    'respect': 1,
    'mutual trust': 1,
    'good faith': 1,
    'bond': 1,
    'accountability': 1,
    'sincerity': 1,
}

dignity_keywords = {
    'dignity': 1,
    'respect': 1,
    'self-respect': 1,
    'self-worth': 1,
    'honor': 1,
    'esteem': 1,
    'integrity': 1,
    'pride': 1,
    'value': 1,
    'worthiness': 1,
    'nobility': 1,
    'decency': 1,
    'humanity': 1,
    'morality': 1,
    'righteousness': 1,
    'self-esteem': 1,
    'self-dignity': 1,
    'reputation': 1,
    'prestige': 1,
    'self-regard': 1,
    'individualism': 1,
}

truth_keywords = {
    'truth': 1,
    'fact': 1,
    'reality': 1,
    'honesty': 1,
    'accuracy': 1,
    'authenticity': 1,
    'veracity': 1,
    'transparency': 1,
    'sincerity': 1,
    'genuineness': 1,
    'candor': 1,
    'integrity': 1,
    'factualness': 1,
    'objectivity': 1,
    'trustworthiness': 1,
    'evidence': 1,
    'proof': 1,
    'verifiable': 1,
    'undeniable': 1,
    'certainty': 1,
    'clarity': 1,
    'frankness': 1,
    'openness': 1,
    'straightforwardness': 1,
    'reliability': 1,
}

# ACM 
    
print(f"\nACM - autonomy count: {get_count_library(acm, autonomy_keywords)}")
print(f"ACM - discrimination count: {get_count_library(acm, discrimination_keywords)}")
print(f"ACM - domination count: {get_count_library(acm, domination_keywords)}")
print(f"ACM - exclusion count: {get_count_library(acm, exclusion_keywords)}")
print(f"ACM - exploitation count: {get_count_library(acm, exploitation_keywords)}")
print(f"ACM - inequality count: {get_count_library(acm, inequality_keywords)}")
print(f"ACM - justice count: {get_count_library(acm, justice_keywords)}")
print(f"ACM - privacy count: {get_count_library(acm, privacy_keywords)}")
print(f"ACM - responsibility count: {get_count_library(acm, responsibility_keywords)}")
print(f"ACM - trust count: {get_count_library(acm, trust_keywords)}")
print(f"ACM - dignity count: {get_count_library(acm, dignity_keywords)}")
print(f"ACM - truth count: {get_count_library(acm, truth_keywords)}")


# IEEE

print(f"\nIEEE - autonomy count: {get_count_library(ieee, autonomy_keywords)}")
print(f"IEEE - discrimination count: {get_count_library(ieee, discrimination_keywords)}")
print(f"IEEE - domination count: {get_count_library(ieee, domination_keywords)}")
print(f"IEEE - exclusion count: {get_count_library(ieee, exclusion_keywords)}")
print(f"IEEE - exploitation count: {get_count_library(ieee, exploitation_keywords)}")
print(f"IEEE - inequality count: {get_count_library(ieee, inequality_keywords)}")
print(f"IEEE - justice count: {get_count_library(ieee, justice_keywords)}")
print(f"IEEE - privacy count: {get_count_library(ieee, privacy_keywords)}")
print(f"IEEE - responsibility count: {get_count_library(ieee, responsibility_keywords)}")
print(f"IEEE - trust count: {get_count_library(ieee, trust_keywords)}")
print(f"IEEE - dignity count: {get_count_library(ieee, dignity_keywords)}")
print(f"IEEE - truth count: {get_count_library(ieee, truth_keywords)}")


# Philpapers

print(f"\nPhilpapers - autonomy count: {get_count_library(philpapers, autonomy_keywords)}")
print(f"Philpapers - discrimination count: {get_count_library(philpapers, discrimination_keywords)}")
print(f"Philpapers - domination count: {get_count_library(philpapers, domination_keywords)}")
print(f"Philpapers - exclusion count: {get_count_library(philpapers, exclusion_keywords)}")
print(f"Philpapers - exploitation count: {get_count_library(philpapers, exploitation_keywords)}")
print(f"Philpapers - inequality count: {get_count_library(philpapers, inequality_keywords)}")
print(f"Philpapers - justice count: {get_count_library(philpapers, justice_keywords)}")
print(f"Philpapers - privacy count: {get_count_library(philpapers, privacy_keywords)}")
print(f"Philpapers - responsibility count: {get_count_library(philpapers, responsibility_keywords)}")
print(f"Philpapers - trust count: {get_count_library(philpapers, trust_keywords)}")
print(f"Philpapers - dignity count: {get_count_library(philpapers, dignity_keywords)}")
print(f"Philpapers - truth count: {get_count_library(philpapers, truth_keywords)}")


# Springer

print(f"\nSpringer - autonomy count: {get_count_library(springer, autonomy_keywords)}")
print(f"Springer - discrimination count: {get_count_library(springer, discrimination_keywords)}")
print(f"Springer - domination count: {get_count_library(springer, domination_keywords)}")
print(f"Springer - exclusion count: {get_count_library(springer, exclusion_keywords)}")
print(f"Springer - exploitation count: {get_count_library(springer, exploitation_keywords)}")
print(f"Springer - inequality count: {get_count_library(springer, inequality_keywords)}")
print(f"Springer - justice count: {get_count_library(springer, justice_keywords)}")
print(f"Springer - privacy count: {get_count_library(springer, privacy_keywords)}")
print(f"Springer - responsibility count: {get_count_library(springer, responsibility_keywords)}")
print(f"Springer - trust count: {get_count_library(springer, trust_keywords)}")
print(f"Springer - dignity count: {get_count_library(springer, dignity_keywords)}")
print(f"Springer - truth count: {get_count_library(springer, truth_keywords)}")