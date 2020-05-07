from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import sys

def def_environment():
   path_to_dir = os.path.dirname(os.path.realpath(__file__))
   #print("ścieszka do folderu:" + path_to_dir)
   os.environ["PATH"] += os.pathsep + path_to_dir

def def_romaji(sentence):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    basic_url = "http://romaji.me/"
    driver = webdriver.Firefox(options=options)
    driver.get(basic_url)
    textAreaInput = driver.find_element_by_xpath('//*[@id="REQUEST_TEXT"]')
    textAreaInput.send_keys(Keys.CONTROL + "a")
    textAreaInput.send_keys(Keys.DELETE)
    textAreaInput.send_keys(sentence)
    submitBtn = driver.find_element_by_xpath('//*[@id="BUTTON_SUBMIT"]')
    submitBtn.click()
    sleep(1)
    textAreaOutput = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/div[4]/div[3]/div[2]/div/p/ruby[2]/rt')
    textOutput = textAreaOutput.text
    print(textOutput)
    #do testow
    #driver.save_screenshot('Romaji.png')
    driver.quit()

def main():
    if len(sys.argv) > 1:
        sentence = str(sys.argv[1])
        def_romaji(sentence)
    else:
        print("Coś nie tak z liczba argumentów, sprawdź listę argumentów skryptu")

if __name__ == "__main__":
    def_environment()
    main()

