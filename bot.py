from selenium import webdriver
import time

PATH = "./chromedriver"
class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.log_in()

    def log_in(self):
        self.driver.get("https://instagram.com")
        # time.sleep(6)

    def do_by_hashtag(self, hashtag, how_many, action):
        if "#" in hashtag:
            hashtag = hashtag.replace("#", "")
        self.driver.get(f"https://instagram.com/explore/tags/{hashtag}")
        time.sleep(4)

        pic_path = "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]"
        pic = self.driver.find_element_by_xpath(pic_path)
        pic.click()
        time.sleep(2)

        for _ in range(how_many):
            action()
            self.go_right()

    def follow_by_hashtag(self, hashtag, how_many):
        action = self.follow
        self.do_by_hashtag(hashtag, how_many, action)

    def like_by_hashtag(self, hashtag, how_many):
        action = self.like
        self.do_by_hashtag(hashtag, how_many, action)

    def follow(self):
        xpath = "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button"
        follow_btn = self.driver.find_element_by_xpath(xpath)
        print(follow_btn.text)
        while follow_btn.text != "Obserwuj":
            self.go_right()
            follow_btn = self.driver.find_element_by_xpath(xpath)
        follow_btn.click()
        time.sleep(.5)

    def like(self):
        like_xpath = '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button'
        value_selector = 'button>div>span>svg'
        value = self.driver.find_element_by_css_selector(value_selector)
        while value.get_attribute("aria-label") != "Lubię to!":
            self.go_right()
            value = self.driver.find_element_by_css_selector(value_selector)
        like_btn = self.driver.find_element_by_xpath(like_xpath)
        like_btn.click()
        time.sleep(.5)

    def go_right(self):
        xpath="/html/body/div[4]/div[1]/div/div/a[2]"
        right_arrow = self.driver.find_element_by_xpath(xpath)
        right_arrow.click()
        time.sleep(2)
        

class Client:
    actions = """
What would you like me to do? Enter action's number.
1 - Follow chosen number of people who recently posted something with a given hashtag
2 - Like most recently added pictures with a given hashtag.
"""

    def __init__(self):
        print("\n\n ---INSTABOT v0.001---\n\n")
        print("Please log in to your account and close all windows, that popped up.\n")
        self.bot = InstaBot()
        while True:
            self.get_request()

    def get_request(self):
        pic = input(Client.actions)
        if pic in ['1', '2']:
            hashtag = input("Choose a hashtag: ")
            if pic == '1':
                how_many = int(input("Choose how many people should i follow: "))
                print("Please wait...")
                self.bot.follow_by_hashtag(hashtag, how_many)
            else:
                how_many = int(input("Choose how many photos should i like: "))
                print("Please wait...")
                self.bot.like_by_hashtag(hashtag, how_many)
                
Client()
