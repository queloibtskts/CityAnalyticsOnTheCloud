import pandas as pd

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

def view_reformatter(rows, URL, isRemovingNonAscii=False):
    if URL[-2:] == 'AU':
        # mapreduce the whole country
        freqs = []
        for row in rows:
            if (not isRemovingNonAscii):
                freqs.append({'text': row['key'], 'value': row['value']})
            elif isRemovingNonAscii and checkIfAscii(row['key']):
                freqs.append({'text': row['key'], 'value': row['value']})

        all_freqs = {'AU': freqs}
        return all_freqs
    else:
        # mapreduce by states
        all_freqs = {}
        for row in rows:
            freqs = []
            for (k, v) in row['value'].items():
                if (not isRemovingNonAscii):
                    freqs.append({'text': k, 'value': v})
                elif isRemovingNonAscii and checkIfAscii(k):
                    freqs.append({'text': k, 'value': v})
            all_freqs[row['key']] = freqs
        return all_freqs

def getTop3VulgarWords(rows):
    newrows = []
    for row in rows:
        newfreq = {}
        freq = row['value']
        top3Freq = {k: freq[k] for k in sorted(freq, key=lambda x: freq[x], reverse=True)[:3]}
        newfreq['key'] = row['key']
        newfreq['value'] = top3Freq
        newrows.append(newfreq)
    return newrows

def top3VulgarWordsJson_to_CSV(vulgarWordFreq_top3, vulgar_countTweetByStates):
    '''This function converts and combines lists of json to a csv file
    so that it can be used in Tableau more conveniently.
    e.g. vulgarWordFreq_top3:list = [{'key': 'NSW', 'value': {'fuck': 77, 'fucking': 49, 'bullshit': 17}}],
    vulgar_countTweetByStates:list = [{"key":"new south wales","value":286}]'''

    csvToBe = 'top3VulgarWordsByState.csv' # csv file name

    # define columns in the csv
    col_state = []
    col_category = [] # name of each vulgar word
    col_freq = [] # frequencies

    # the conversion begins
    for row in vulgar_countTweetByStates:
        col_state.append(row['key'])
        col_category.append('total')
        col_freq.append(row['value']) # total number of vulgar tweets in this state

    for row in vulgarWordFreq_top3:
        state = row['key']
        dict_vwords = row['value'] # dict of popular vulgar words (top 3) in each state and their frequencies
        for (vword, freq) in dict_vwords.items():
            col_state.append(state)
            col_category.append(vword)
            col_freq.append(freq)

    toDF = {'state': col_state, 'category': col_category, 'frequency': col_freq}
    df = pd.DataFrame(toDF)
    try:
        df.to_csv(csvToBe)
        print('***\ntop3VulgarWordsJson_to_CSV: Saved to CSV!\n***\n')
    except:
        print('***\ntop3VulgarWordsJson_to_CSV: Error when saving to CSV\n***\n')

def checkIfAscii(hashtag):
    '''This function checks if a hashtag is of ascii characters.'''
    try:
        code = hashtag.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False
