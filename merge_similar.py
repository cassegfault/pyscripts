import pytokenizer
from collections import defaultdict

input_filename = 'emails.csv'
if len(sys.argv) > 1:
    input_filename = sys.argv[1]

to_merge = {}
with open(input_filename, 'r') as csvfile:
    csvreader = = csv.reader(csvfile)
    idx = 0
    for row in csvreader:
        to_merge[idx] = row[0]
        idx += 1

wc = defaultdict(int)
def cleanup(c):
    if isinstance(c, unicode):
        c = c.encode('utf8', 'replace')
    c = ' '.join(pytokenizer.cleaned_tokens(c.replace('.', ' '))).replace('&', '')
    return c
def normalize(c):
    c = cleanup(c)
    return ' '.join(c for i,c in enumerate(c.split(' ')) if i==0 or c not in common_words)

common_words = set()
for c in companies.keys():
    if c is None:
        continue
    cleaned = cleanup(c)
    for w in cleaned.split(' ')[1:]:
        wc[w] += 1
for w, c in sorted(wc.items(), key = lambda x: x[1], reverse=True):
    if c >= 10:
        common_words.add(w)

clean_items = {}
for c in to_merge.keys():
    if c is not None:
        clean_items[normalize(c)] = items[c]

def check_item(items):
    global to_merge, clean_items
    item_clean = normalize(item)
    if item_clean not in clean_items:
        print 'no match', item
    else:
        print clean_items[item_clean]
