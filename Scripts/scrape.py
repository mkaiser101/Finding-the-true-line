from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

path_to_script = os.path.dirname(os.path.abspath(__file__))

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

path = 'https://sports.va.betmgm.com/en/sports/football-11'
driver.get(path)

element = driver.find_element(By.XPATH, '/html/body')
# print(type)
pp.pprint(element.text)

page_text = element.text
page_text_list = list(page_text.split("\n"))
pp.pprint(page_text_list)

my_filename = os.path.join(path_to_script, "sample_football_lines_051322.txt")

with open(my_filename, 'w') as fp:
    for item in page_text_list:
        fp.write("%s\n" % item)
    print('Done')



'''
next steps:

split on lines and phrase all wagers


'''
