def view_reformatter(rows):
    all_freqs = {}
    for row in rows:
        freqs = []
        for (k, v) in row['value'].items():
            freqs.append({'text': k, 'value': v})
        all_freqs[row['key']] = freqs
    return all_freqs

def view_reformatterAU(rows):
    freqs = []
    for row in rows:
        freqs.append({'text': row['key'], 'value': row['value']})
    all_freqs = {'AU': freqs}
    return all_freqs