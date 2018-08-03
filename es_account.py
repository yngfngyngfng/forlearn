from urllib.request import Request, urlopen
import json
import pprint
import ssl
import pandas as pd

# Get a list of 'Normal' Transactions By Address
# http://api.etherscan.io/api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken

# [BETA] Get a list of 'Internal' Transactions by Address
# http://api.etherscan.io/api?module=account&action=txlistinternal&address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3&startblock=0&endblock=2702578&sort=asc&apikey=YourApiKeyToken

# [BETA] Get a list of "ERC20 - Token Transfer Events" by Address
# http://api.etherscan.io/api?module=account&action=tokentx&address=0x4e83362442b8d1bec281594cea3050c8eb01311c&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken

# address_internal_eth
# address_external_eth
# address_token

class ScanEvents:
    def __init__(self, urlpattern, **kwargs):
        apiKey = 'C5DSQ17Y65WQ39JRYVEYHAV8WKSP1XMGJY'
        url = urlpattern.format(**kwargs, apiKey=apiKey)
        print(url)

        context = ssl._create_unverified_context()
        req = Request(url, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"})

        rsp = urlopen(req, context=context)

        res = json.loads(rsp.read().decode('utf8'))
        self.events = res['result']


class Account:
    def __init__(self, address):

        scaner = ScanEvents(urlpattern="""http://api.etherscan.io/api?module=account&action=txlistinternal&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={apiKey}""",
                             address=address)
        self.save_events(scaner.events, '{}_eth_internal.json'.format(address))

        scaner = ScanEvents(urlpattern="""http://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={apiKey}""",
                             address=address)
        self.save_events(scaner.events, '{}_eth_external.json'.format(address))

        scaner = ScanEvents(urlpattern="""http://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=999999999&sort=asc&apikey={apiKey}""",
                             address=address)
        self.save_events(scaner.events, '{}_token.json'.format(address))



    def save_events(self, events, filename):
        outdir = 'esaccounts/'
        dataout = json.dumps(events, indent=4)
        with open(outdir+filename, mode='w') as dataout_file:
            dataout_file.write(dataout)


def main():
    addresses = [
        '0x44b6051f5831cab34fdd3599d4711849d21d59bc',
        '0x44b6051f5831cab34fdd3599d4711849d21d59bc',
        '0x4599c5389fdb7582cfd716dc99430a224829d147',
        '0x4c8882be61adbba0bfc8c321f0a48a200844d111',
        '0xaa41973dd147aa5d9d1c7c4b696f7a2924117765',
    ]
    for address in addresses:
        account = Account(address)

    #df = pd.read_json(filename)
    # print(df)




if __name__ == '__main__':
    main()


