from utils.extractHTML import getHtml
from component.news import extractNews

import pandas as pd
if __name__ == '__main__': 
    fUrl = 'https://www.ft.com'
    tree = getHtml(url=fUrl)

    header = tree.css_first('a.o-header__top-logo > svg > title').text() 
    # print(header)

    divLink = tree.css_first('nav#o-header-nav-desktop > div.o-header__container')

    aTag = divLink.css('ul.o-header__nav-list > li.o-header__nav-item > a')

    # for a in aTag :
    #     print(f'{fUrl}{a.attributes['href']}')

    links = [f'{fUrl}{hr.attributes['href']}'  for hr in aTag]

    allNews = []

    for nLink in links[1:]:
        print(nLink)
        newHeading = extractNews(nUrl=nLink)
        allNews.append(
            {
                'link': nLink,
                'newHeading': newHeading
            }
        )

        newsPd = pd.DataFrame(allNews)

        newsPd.to_csv('news.csv')


    

