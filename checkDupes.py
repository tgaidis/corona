def checkDupes(filepath):
    tidl = []
    tiddic = dict()
    f = open(filepath, "r")
    for cat in f:
        cat_strip = cat.strip("\n")
        cat_split = cat_strip.split(",")
        tid = cat_split[1]
        tidl.append(tid)
    number_of_tweets = len(tidl)
    for item in tidl:
        if item in tiddic:
            tiddic[item] += 1
        else:
            tiddic[item] = 1
    tiddic = {key:value for key, value in tiddic.items() if value > 1}
    return tiddic, number_of_tweets    
    
