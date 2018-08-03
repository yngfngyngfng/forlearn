from urllib.request import Request, urlopen
import json
import pprint
import ssl


# https://api.etherscan.io/api?module=logs&action=getLogs
# &fromBlock=4051681
# &toBlock=4051681
# &address=0xb7cB1C96dB6B22b0D3d9536E0108d062BD488F74
# &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
# &apikey=C5DSQ17Y65WQ39JRYVEYHAV8WKSP1XMGJY


def get_event(blocknumber):

    urlpartern = """https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={}&toBlock=latest&address=0xb7cB1C96dB6B22b0D3d9536E0108d062BD488F74&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&apikey=C5DSQ17Y65WQ39JRYVEYHAV8WKSP1XMGJY"""
    url = urlpartern.format(blocknumber)
    print(url)
    context = ssl._create_unverified_context()

    req = Request(url, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"})
    rsp = urlopen(req, context=context)
    res = json.loads(rsp.read().decode('utf8'))
    events = res['result']
    if len(events) > 0:
        blocknumber = int(events[-1]['blockNumber'], 16)
    return events, blocknumber

def main():
    events_cnt = 0
    cur_blocknumber = 0
    # cur_blocknumber = 5944136

    for i in range(10000000):
        cur_events, cur_blocknumber = get_event(blocknumber=cur_blocknumber)
        if len(cur_events) == 0:
            break
        events_cnt += len(cur_events)
        print('cur_events ', 'all_events ', 'cur_blocknumber')
        print(len(cur_events), events_cnt, cur_blocknumber)

        dataout = json.dumps({'events': cur_events}, indent=4)
        filename = 'eslogs/log_{:06}_{}_0x{:x}.json'.format(i, cur_blocknumber, cur_blocknumber)

        with open(filename, mode='w') as dataout_file:
                dataout_file.write(dataout)



if __name__ == '__main__':
    main()



