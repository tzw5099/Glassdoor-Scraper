"""
Created on Sun Dec 24 09:00:27 2017

@author: lishuo
"""
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    
    browser   = None
    
    def scrape(self):
        raise ValueError('interface scrape need implemented with return value as a dataframe')
        
class GlassdoorReviewScraper(Scraper):
    
    config    = None
    columns   = None
    
    def __init__(self, browser, config):
        self.browser = browser
        self.config = config
        self.columns = ['company', 'stars', 'date']
        
    def scrape(self):
        dfs = []
        
        for company, (start_url, pages) in self.config.items():
            for i in range(1, pages+1):
                reviews = self.get_reviews(start_url, i)
                dfs.append(self.parse_reviews(company, reviews))
            
        sum_df = pd.concat(dfs)
        sum_df.index = [i for i in range(len(sum_df))]
        return sum_df
    
    def get_reviews(self, start_url, page_numer=1):
        url = start_url[:start_url.find('.htm')] + '_P' + str(page_numer) + '.htm'
        self.browser.get(url)
        
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        reviews = soup.find_all("li", { "class" : ["empReview", "padVert"] })
        
        return reviews
        
    def parse_reviews(self, company, reviews):
        df = pd.DataFrame(columns=self.columns)
        
        for index, review in enumerate(reviews):
            rating = review.find('span', {'class':'value-title'}).attrs['title']
            date = review.find('time').attrs['datetime']
            df.loc[index] = [company, rating, date]
            
        return df