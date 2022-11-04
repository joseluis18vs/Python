import requests


class QueryClass:
    url = "https://www.bet365.com/#/HO/"
    # url = "http://localhost:8080/api/books_list"

    # header = {
    #     # 'host': 'http://localhost:8080',
    #     'connection': 'keep-alive',
    #     'cache-control': 'max-age=0',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    #     'sec-gpc': '1',
    #     'accept-language': 'es-419,es',
    #     'sec-fetch-site': 'none',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-user': '?1',
    #     'sec-fetch-dest': 'document',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'cookie': 'OptanonConsent=isGpcEnabled=1&datestamp=Mon+Oct+10+2022+02%3A12%3A19+GMT%2B0200+(hora+de+verano+de+Europa+central)&version=6.26.0&isIABGlobal=false&hosts=&consentId=f18fe246-3dbb-48ef-9631-6cec92b048f4&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A0%2CC0007%3A1&AwaitingReconsent=false; JSESSIONID=0D6FC14DDC79A244D062E1BE1792E026'
    # }

    UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
           "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
           )

    header = {
        'connection': 'keep-alive',
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        'Content-Type': 'application/json'
    }

    def __int__(self):
        print("Constructor")

    def queryRun(self):
        return requests.get(self.url, headers=self.header)
