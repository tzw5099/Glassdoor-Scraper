"""
Created on Sun Dec 24 09:00:27 2017

@author: lishuo
"""
from session import GlassdoorSession

if __name__=='__main__':
    with GlassdoorSession() as session:
        reviews = session.scrapeReviews()
        reviews.to_csv('reviews.csv', sep=',')