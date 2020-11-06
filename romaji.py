from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import sys
import argparse
import logging


def def_params():
   parser = argparse.ArgumentParser(
             description="Script to create transcription from japana symbols to romaji i odwrotnie"
   )
   parser.add_argument('-l', "--loghami", action="store_true", help="set debug")
   parser.add_argument('-s', '--sentence', help="sentence to romajing", required=True)
   #parser.add_argument('', "", )
   args = parser.parse_args()
   if args.loghami:
       logging.basicConfig(level=logging.DEBUG)
       logging.debug("args:" + str(args))
   return args


def def_environment():
   path_to_dir = os.path.dirname(os.path.realpath(__file__))
   logging.debug("ścieszka do folderu:" + path_to_dir)
   os.environ["PATH"] += os.pathsep + path_to_dir


def def_romaji(sentence, loghami):
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
    logging.debug(textOutput)
    #do testow
    if loghami:
        driver.save_screenshot('Romaji.png')
    driver.quit()


def main():
    args=def_params()
    sentence = args.sentence
    loghami = args.loghami
    def_romaji(sentence, loghami)


if __name__ == "__main__":
    def_environment()
    main()

