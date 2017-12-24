from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    
    browser   = None
    
    def scrape(self):
        raise ValueError('interface scrape need implemented with return value as a dataframe')
        
class GlassdoorReviewScraper(Scraper):
    
    company   = None
    start_url = None
    pages     = None
    columns   = None
    
    def __init__(self, browser, company='Microsoft', \
                 start_url='https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651.htm', pages=10):
        self.browser = browser
        self.company = company
        self.start_url = start_url
        self.pages = pages
        self.columns = ['stars', 'date']
        
    def scrape(self):
        dfs = []
        
        for i in range(1, self.pages+1):
            reviews = self.get_reviews(i)
            dfs.append(self.parse_reviews(reviews))
            
        sum_df = pd.concat(dfs)
        sum_df.index = [i for i in range(len(sum_df))]
        return sum_df
    
    def get_reviews(self, page_numer=1):
        url = self.start_url[:self.start_url.find('.htm')] + '_P' + str(page_numer) + '.htm'
        self.browser.get(url)
        
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        reviews = soup.find_all("li", { "class" : ["empReview", "padVert"] })
        return reviews
        
    def parse_reviews(self, reviews):
        df = pd.DataFrame(columns=self.columns)
        
        for index, review in enumerate(reviews):
            rating = review.find('span', {'class':'value-title'}).attrs['title']
            date = review.find('time').attrs['datetime']
            df.loc[index] = [rating, date]
            
        return df