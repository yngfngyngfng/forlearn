from urllib.request import Request, urlopen
import json
import ssl

# https://api.etherscan.io/api?module=logs&action=getLogs
# &fromBlock=4051681
# &toBlock=4051681
# &address=0xb7cB1C96dB6B22b0D3d9536E0108d062BD488F74
# &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
# &apikey=C5DSQ17Y65WQ39JRYVEYHAV8WKSP1XMGJY

urlpartern = """https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={}&toBlock=latest&address=0xb7cB1C96dB6B22b0D3d9536E0108d062BD488F74&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&apikey=C5DSQ17Y65WQ39JRYVEYHAV8WKSP1XMGJY"""
url = urlpartern.format(blocknumber)

req = Request(
    url, 
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"})

rsp = urlopen(
    req,
    context=ssl._create_unverified_context())

res = json.loads(rsp.read().decode('utf8'))
result = res['result']
