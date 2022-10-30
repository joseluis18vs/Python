import requests


class QueryClass:
    url = "https://www.bet365.com/#/HO/"

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'es-419,es;q=0.5',
        'Connection': 'keep-alive',
        'Cookie': 'pstk=83E9088659196988B0B579B0153877A5000003; rmbs=3; gstk=83E9088659196988B0B579B0153877A5000003; '
                  'swt=ASURMvNvdzsJov1obAopGEm5/mUGBxnGCZ4OZXCeaQltGUAQvNR2nxm8UeFoG7O'
                  '+MLPn0o32YK2T8xyWwrE9mjJBzUYwNWPAMEXhSRhYx7ac2DFQ; '
                  'aps03=cf=N&cg=1&cst=0&ct=139&hd=N&lng=3&oty=2&tt=5&tzi=13',
        'Host': 'www.bet365.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 '
    }

    def __int__(self):
        print("Constructor")

    def queryRun(self):
        return requests.get(self.url, headers=self.header)
