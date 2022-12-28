import time


class MoveToResults:
    def __init__(self):
        self.gdpr_decline_xpath = "W0wltc"
        self.google_input_name = "q"
        self.search_results_link_xpath = "//a[contains(@href,'www.wakacje.pl')]"
        self.internal_holidays_gdpr_decline_xpath = "//button[text()='AKCEPTUJĘ I PRZECHODZĘ DO SERWISU']"
        self.place_input_xpath = "//input[@value='Dowolnie']"
        self.place_confirmation_xpath = "//input[@placeholder='Wpisz kierunek lub hotel']"
        self.results_confirmation_xpath = "//div[1]/div/div[1]/ul/li[2]/label"
        self.search_places_button_xpath = "/html/body/div[5]/div[1]/div/footer/button"
        self.inside_offer_price_tag = "//div[2]/div/div/div/h4"


scrollread = driver.execute_script('return document.body.scrollHeight')
scrolldown = driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
while True:
    scrolldown
    time.sleep(sleeptime)
    scrollread
    if scrollread==scrollread
        break