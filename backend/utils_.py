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

def checkIfAscii(hashtag):
    '''This function checks if a hashtag is of ascii characters.'''
    try:
        code = hashtag.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False
