"""
Created on Sun Dec 24 09:00:27 2017

@author: lishuo
"""
from session import GlassdoorSession

config = {
    'Microsoft':'https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651.htm',
    'Google':'https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm'
}

if __name__=='__main__':
    with GlassdoorSession(config) as session:
        reviews = session.scrapeReviews()
        reviews.to_csv('reviews.csv', sep=',')