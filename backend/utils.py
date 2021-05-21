def view_reformatter(rows, URL):
    if URL[-2:] == 'AU':
        # mapreduce the whole country
        freqs = []
        for row in rows:
            freqs.append({'text': row['key'], 'value': row['value']})
        all_freqs = {'AU': freqs}
        return all_freqs
    else:
        # mapreduce by states
        all_freqs = {}
        for row in rows:
            freqs = []
            for (k, v) in row['value'].items():
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
