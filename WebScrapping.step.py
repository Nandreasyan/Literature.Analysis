import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime

# # ACM case
# acm = pd.read_csv("acm.12.20-10.23.no.dups.with.all.csv")

# print(len(acm['Abstract'][acm['Abstract'].isna()]))

# i = 0
# for i in range(len(acm['Abstract'])):
    
#     if isinstance(acm['Abstract'].loc[i], float):

#         obj = datetime.now()

#         url = acm['URL'].loc[i]
#         print('\x1b[6;30;42m' + url + '\x1b[0m')

#         driver = webdriver.Chrome()
#         driver.get(url)
#         # driver.maximize_window()
#         time.sleep(0.1)
#         page = driver.page_source
#         driver.quit()
#         soup = BeautifulSoup(page, 'html.parser')

#         main_content = soup.find('div', class_='main-content')

#         if main_content:

#             for element in main_content.select("p"):
#                 acm.loc[i, 'Abstract'] = element.get_text()
#                 acm.to_csv("acm.12.20-10.23.no.dups.with.all.csv")
        
#         abstracts_div = soup.find('div', id='abstracts')

#         if abstracts_div:

#             for element in abstracts_div.select("p"):
#                 acm.loc[i, 'Abstract'] = element.get_text()
#                 acm.to_csv("acm.12.20-10.23.no.dups.with.all.csv")

#         abstractSection = soup.find('div', class_='abstractSection')

#         if abstractSection:

#             for element in abstractSection.select("p"):
#                 acm.loc[i, 'Abstract'] = element.get_text()
#                 acm.to_csv("acm.12.20-10.23.no.dups.with.all.csv")
        
# print(len(acm['Abstract'][acm['Abstract'].isna()]))
# print(acm)

# # Save the updated DataFrame back to the CSV file
# acm.to_csv('acm.12.20-10.23.no.dups.with.all.csv', index=False)


## Springer case
springer = pd.read_csv("springer2123N.csv")

print(len(springer['Abstract'][springer['Abstract'].isna()]))

# i = 0
# for i in range(len(springer['Abstract'])):
    
#     if isinstance(springer['Abstract'].loc[i], float):

#         obj = datetime.now()

#         url = springer['URL'].loc[i]
#         print(i, ") ", '\x1b[6;30;42m' + url + '\x1b[0m')

#         driver = webdriver.Chrome()
#         driver.get(url)
#         # driver.maximize_window()
#         time.sleep(0.01)
#         page = driver.page_source
#         soup = BeautifulSoup(page, 'html.parser')

#         main_content = soup.find('div', class_='main-content')

#         if main_content:
#             springer.loc[i, 'Abstract'] = ""
#             for element in main_content.select("p"):
                
#                 springer.loc[i, 'Abstract'] += element.get_text()
#                 springer.to_csv('springer2123N.csv', index=False)
        
#         abstracts_div = soup.find('div', id='Abs1-content')

#         if abstracts_div:
#             springer.loc[i, 'Abstract'] = ""
#             for element in abstracts_div.select("p"):
                
#                 springer.loc[i, 'Abstract'] += element.get_text()
#                 springer.to_csv('springer2123N.csv', index=False)

#         bookSection = soup.find('div', class_='c-book-section')

#         if bookSection:
#             springer.loc[i, 'Abstract'] = ""
#             if bookSection.select("p"):
#                 for element in bookSection.select("p"):
#                     springer.loc[i, 'Abstract'] += element.get_text()
#                     springer.to_csv('springer2123N.csv', index=False)
#             else:
#                 springer.loc[i, "Abstract"] = element.get_text()
        
#         articleSection = soup.find('div', class_='c-article-section__content')

#         if articleSection:
#             for element in articleSection.select("p"):
                
#                 springer.loc[i, 'Abstract'] = element.get_text()
#                 springer.to_csv('springer2123N.csv', index=False)

        
#     if isinstance(springer['Abstract'].loc[i], float) and isinstance(springer['Keywords'], float):
#         print("book")
        

# driver.quit()
# print(len(springer['Abstract'][springer['Abstract'].isna()]))

# # Save the updated DataFrame back to the CSV file
# springer.to_csv('springer2123.csv', index=False)


# adjustment for springer errors.Handling possible errors
i = 0
for i in range(len(springer['Abstract'])):
    
    if springer['Type'].loc[i] == 'Book':

        obj = datetime.now()

        url = springer['URL'].loc[i]
        print(i, ") ", '\x1b[6;30;42m' + url + '\x1b[0m')

        driver = webdriver.Chrome()
        driver.get(url)
        # driver.maximize_window()
        time.sleep(0.01)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        # Find the section with data-title="About this book"
        about_book_section = soup.find('section', {'data-title': 'About this book'})

        if about_book_section:
            # Find the internal div with class="c-book-section"
            book_section = about_book_section.find('div', class_='c-book-section')

            if book_section:
                print(book_section.get_text())
                # Update the Abstract column
                springer.loc[i, 'Abstract'] = book_section.get_text()
                springer.to_csv('springer2123N.csv', index=False)

    if springer['Type'].loc[i] == 'ReferenceWork':

        obj = datetime.now()

        url = springer['URL'].loc[i]
        print(i, ") ", '\x1b[6;30;42m' + url + '\x1b[0m')

        driver = webdriver.Chrome()
        driver.get(url)
        # driver.maximize_window()
        time.sleep(0.01)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        # Find the section with data-title="About this book"
        about_book_section = soup.find('section', {'data-title': 'About this book'})

        if about_book_section:
            # Find the internal div with class="c-book-section"
            book_section = about_book_section.find('div', class_='c-book-section')

            if book_section:
                print(book_section.get_text())
                # Update the Abstract column
                springer.loc[i, 'Abstract'] = book_section.get_text()
                springer.to_csv('springer2123N.csv', index=False)
        

driver.quit()
print(len(springer['Abstract'][springer['Abstract'].isna()]))

# Save the updated DataFrame back to the CSV file
springer.to_csv('springer2123N.csv', index=False)





# Philpapers case
# philpapers = pd.read_csv("philpapers2123N.csv")

# print(len(philpapers['Abstract'][philpapers['Abstract'].isna()]))
# print(philpapers['Abstract'][philpapers['Abstract'].isna()])

# i = 0
# for i in range(len(philpapers['Abstract'])):
    
#     if isinstance(philpapers['Abstract'].loc[i], float):

#         print(philpapers.loc[i, 'URL'])
#         obj = datetime.now()

#         url = philpapers['URL'].loc[i]
#         print(i, ") ", '\x1b[6;30;42m' + url + '\x1b[0m')

#         driver = webdriver.Chrome()
#         driver.get(url)
#         # driver.maximize_window()
#         time.sleep(3)
#         page = driver.page_source
#         soup = BeautifulSoup(page, 'html.parser')

        # main_content = soup.find('div', class_='main-content')

        # if main_content:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in main_content.select("p"):
                
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)
        
        # abstracts_div = soup.find('div', id='Abs1-content')

        # if abstracts_div:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in abstracts_div.select("p"):
                
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # bookSection = soup.find('div', class_='c-book-section')

        # if bookSection:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     if bookSection.select("p"):
        #         for element in bookSection.select("p"):
        #             philpapers.loc[i, 'Abstract'] += element.get_text()
        #             philpapers.to_csv('philpapers2123N.csv', index=False)
        #     else:
        #         philpapers.loc[i, "Abstract"] = element.get_text()

        # abs001 = soup.find('div', class_='abstract author')

        # if abs001:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     print(abs001.get_text())
        #     philpapers.loc[i, 'Abstract'] = abs001.get_text()
        #     philpapers.to_csv('philpapers2123N.csv', index=False)
        
        # articleSection = soup.find('div', class_='c-article-section__content')

        # if articleSection:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in articleSection.select("p"):
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # hlFld = soup.find('div', class_='hlFld-Abstract')

        # if hlFld:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in hlFld.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # article = soup.find('div', class_='article fulltext-view')

        # if article:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in article.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # article = soup.find('div', class_='article extract-view')

        # if article:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in article.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # article = soup.find('div', id='sec001')

        # if article:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in article.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # article = soup.find('div', id='core-container')

        # if article:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in article.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)

        # article = soup.find('div', id='sec no-title')

        # if article:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in article.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)
        
        # article = soup.find('div', id='article_abstract')

        # if article:
        #     philpapers.loc[i, 'Abstract'] = ""
        #     for element in article.select("p"):
        #         print(element.get_text())
        #         philpapers.loc[i, 'Abstract'] += element.get_text()
        #         philpapers.to_csv('philpapers2123N.csv', index=False)


        
    # if isinstance(philpapers['Abstract'].loc[i], float) and isinstance(philpapers['Keywords'], float):
    #     print("book")
        

# driver.quit()
# print(len(philpapers['Abstract'][philpapers['Abstract'].isna()]))

