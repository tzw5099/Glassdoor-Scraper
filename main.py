from session import GlassdoorSession

if __name__=='__main__':
    with GlassdoorSession() as session:
        reviews = session.scrapeReviews()
        reviews.to_csv('reviews.csv', sep=',')