"""
Created on Sun Dec 24 09:00:27 2017

@author: lishuo
"""
from selenium import webdriver
from credentials import username, password
from selenium.common.exceptions import TimeoutException
from scraper import GlassdoorReviewScraper

class Session:
    def login(self):
        pass
    
    def logout(self):
        pass
        
class GlassdoorSession(Session):
    browser          = None
    driver_path      = None
    login_page_url   = None
    username_ctl_id  = None
    password_ctl_id  = None
    login_btn_ctl_id = None
    review_scraper   = None
    config           = None
    
    def __init__(self, config):
        self.driver_path      = './driver/chromedriver'
        self.login_page_url   = 'http://www.glassdoor.com/profile/login_input.htm'
        self.username_ctl_name  = 'username'
        self.password_ctl_name  = 'password'
        self.login_btn_ctl_class = 'gd-btn-1'
        self.config = config
        
    def login(self):
        try:
            self.browser = webdriver.Chrome(self.driver_path)
            self.browser.get(self.login_page_url)
            
            username_ctl = self.browser.find_element_by_name(self.username_ctl_name)
            password_ctl = self.browser.find_element_by_name(self.password_ctl_name)
            username_ctl.send_keys(username)
            password_ctl.send_keys(password)
            
            login_btn = self.browser.find_element_by_class_name(self.login_btn_ctl_class)
            login_btn.click()    
            
            self.review_scraper   = GlassdoorReviewScraper(self.browser, self.config)
        except TimeoutException:
            print('login timeout')
            
    def __enter__(self):
        self.login()
        return self
        
    def __exit__(self, *args):
        self.logout()
        
    def scrapeReviews(self):
        return self.review_scraper.scrape()