import pandas as pd


def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

def getTop3VulgarWords(rows):
    '''This function returns the word-frequency dict of top 3 most used vulgar word in each state.
    If ties exist, rank alphabetically.'''
    newrows = []
    for row in rows:
        newfreq = {}
        freq = row['value']
        freq = {k: freq[k] for k in sorted(freq)}  # rank alphabetically
        top3Freq = {k: freq[k] for k in sorted(freq, key = lambda x: freq[x], reverse = True)[:3]}
        newfreq['key'] = row['key']
        newfreq['value'] = top3Freq
        newrows.append(newfreq)
    return newrows


def top3VulgarWordsJson_to_CSV(vulgarWordFreq_top3, vulgar_countTweetByStates):
    '''This function converts and combines lists of json to a csv file
    so that it can be used in Tableau more conveniently.
    e.g. vulgarWordFreq_top3:list = [{'key': 'NSW', 'value': {'fuck': 77, 'fucking': 49,
    'bullshit': 17}}],
    vulgar_countTweetByStates:list = [{"key":"new south wales","value":286}]'''
    
    csvToBe = 'top3VulgarWordsByState.csv'  # csv file name
    
    # define columns in the csv
    col_state = []
    col_category = []  # total, top1, top2, top3
    col_vword = []  # name of each vulgar word
    col_freq = []  # frequencies
    categories = ["top1", "top2", "top3"]
    
    # the conversion begins
    for row in vulgar_countTweetByStates:
        col_state.append(row['key'])
        col_category.append('total')
        col_vword.append('TOTAL')
        col_freq.append(row['value'])  # total number of vulgar tweets in this state
    
    for row in vulgarWordFreq_top3:
        state = row['key']
        dict_vwords = row[
            'value']  # dict of popular vulgar words (top 3) in each state and their frequencies
        for i in range(len(dict_vwords)):
            vword = list(dict_vwords.keys())[i]
            freq = list(dict_vwords.values())[i]
            category = categories[i]
            
            col_state.append(state)
            col_category.append(category)
            col_vword.append(vword)
            col_freq.append(freq)
    
    toDF = {'state': col_state, 'category': col_category, 'frequency': col_freq,
            'vulgar_word': col_vword}
    df = pd.DataFrame(toDF)
    try:
        df.to_csv(csvToBe)
        print('***\ntop3VulgarWordsJson_to_CSV: Saved to CSV!\n***\n')
    except:
        print('***\ntop3VulgarWordsJson_to_CSV: Error when saving to CSV\n***\n')


def countTweetsByStateJson_to_CSV2(clean_countTweetByStates, vulgar_countTweetByStates):
    '''This function converts and combines countTweetsByState (lists of json) to a csv file
    so that it can be used in Tableau more conveniently.'''
    
    csvToBe = 'countTweetsByState2.csv'  # csv file name
    state_abbrevsAndNames = {'ACT': 'ACT', 'VIC': 'Victoria', 'NSW': 'New South Wales',
                             'NT': 'Northern Territory', 'QLD': 'Queensland', 'TAS': 'Tasmania',
                             'WA': 'Western Australia', 'SA': 'South Australia'}
    
    # define columns in the csv
    col_state = []
    col_state_abbrevs = []  # abbreviations of state names
    col_label = []  # clean or explicit
    col_freq = []  # count of tweets
    
    # the conversion begins
    for row in clean_countTweetByStates:
        state_abbrev = row['key']
        col_state_abbrevs.append(state_abbrev)
        col_state.append(state_abbrevsAndNames[state_abbrev])
        col_label.append('clean')
        col_freq.append(row['value'])  # count of clean tweets
    
    for row in vulgar_countTweetByStates:
        state_abbrev = row['key']
        col_state_abbrevs.append(state_abbrev)
        col_state.append(state_abbrevsAndNames[state_abbrev])
        col_label.append('explicit')
        col_freq.append(row['value'])  # count of explicit tweets
    
    toDF = {'state': col_state, 'state_abbrevs': col_state_abbrevs, 'label': col_label,
            'frequency': col_freq}
    df = pd.DataFrame(toDF)
    try:
        df.to_csv(csvToBe)
        print('***\ncountTweetsByStateJson_to_CSV2: Saved to CSV!\n***\n')
    except:
        print('***\ncountTweetsByStateJson_to_CSV2: Error when saving to CSV\n***\n')


def countTweetsByStateJson_to_CSV(clean_countTweetByStates, vulgar_countTweetByStates):
    '''This function converts and combines countTweetsByState (lists of json) to a csv file
    so that it can be used in Tableau more conveniently.'''
    
    csvToBe = 'countTweetsByState.csv'  # csv file name
    state_abbrevsAndNames = {'ACT': 'ACT', 'VIC': 'Victoria', 'NSW': 'New South Wales',
                             'NT': 'Northern Territory', 'QLD': 'Queensland', 'TAS': 'Tasmania',
                             'WA': 'Western Australia', 'SA': 'South Australia'}
    
    dict_freq_total = {key: 0 for key in state_abbrevsAndNames.keys()}  # store tweet counts
    
    # define columns in the csv
    col_state = []
    col_state_abbrevs = []  # abbreviations of state names
    col_freq_explicit = []  # count of explicit tweets
    col_freq_total = []  # count of tweets
    
    # the conversion begins
    for row in vulgar_countTweetByStates:
        state_abbrev = row['key']
        freq = row['value']
        col_state_abbrevs.append(state_abbrev)
        col_state.append(state_abbrevsAndNames[state_abbrev])
        col_freq_explicit.append(freq)  # count of explicit tweets
        dict_freq_total[state_abbrev] += freq
    
    for row in clean_countTweetByStates:
        state_abbrev = row['key']
        freq = row['value']
        dict_freq_total[state_abbrev] += freq
    
    for abbrev in col_state_abbrevs:
        freq_total = dict_freq_total[abbrev]
        col_freq_total.append(freq_total)
    
    toDF = {'state': col_state, 'state_abbrevs': col_state_abbrevs, 'n_explicit': col_freq_explicit,
            'n_total': col_freq_total}
    
    df = pd.DataFrame(toDF)
    try:
        df.to_csv(csvToBe)
        print('***\ncountTweetsByStateJson_to_CSV: Saved to CSV!\n***\n')
    except:
        print('***\ncountTweetsByStateJson_to_CSV: Error when saving to CSV\n***\n')
