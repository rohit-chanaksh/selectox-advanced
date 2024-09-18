from utils.extractHTML import getHtml

def extractNews(nUrl):
    newsPage = getHtml(url=nUrl)

    newsData = newsPage.css("div.o-teaser__heading > a[data-trackable='heading-link']")

    newsHeadings = [nw.text() for nw in newsData]
    print('newsHeadings',newsHeadings)

    # return newsHeadings