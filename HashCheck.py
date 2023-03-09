import re

with open("BlockHash.txt", encoding='utf-8') as f:
    content = f.read()
    print(content)

    '''
    parentHash
    sha3Uncle
    miner
    stateRoot
    transactionsRoot
    receiptsRoot
    logsBloom
    difficulty
    number
    gasLimit
    gasUsed
    timestamp
    extraData
    mixHash
    nonce
    '''

    a = "parentHash"
    pattern = f"\"{a}\":\"([a-f|0-9|x]+)\","
    result = re.findall(pattern, content)
    print(result)