def countTweets(dupdic, total):
    dickeys = dupdic.keys()
    number_of_keys = len(dickeys)
    dicvalues = dupdic.values()
    dupes = sum(dicvalues)
    dupes_number = dupes - number_of_keys
    final = total - dupes_number
    return(final)
    
    
    
