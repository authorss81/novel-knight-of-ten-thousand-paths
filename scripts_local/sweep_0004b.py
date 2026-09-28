#!/usr/bin/env python3
"""Sweeps 7 to 10 for Batch 0004."""
import re, os, glob
from collections import Counter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
NEW = [os.path.join(ROOT, 'chapters/volume-08', 'chapter-%04d.md' % n) for n in range(381, 391)]
def read(p):
    return open(p, encoding='utf-8').read()
RAW = ''.join(read(p) for p in NEW)
TOKS = re.findall(r'[A-Za-z0-9]+', RAW.lower())

# ---------- SWEEP 7: name sweep
print('=== SWEEP 7 BASIS: capitalised two-word sequences, [A-Z][a-z]+ [A-Z][a-z]+, on the raw text of the ten new files, every hit read. ===')
hits = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', RAW)
for k, v in Counter(hits).most_common():
    where = [os.path.basename(p) for p in NEW if k in read(p)]
    print('  %-28s %d  %s' % (k, v, ','.join(where)))
print('  distinct: %d   total occurrences: %d' % (len(set(hits)), len(hits)))

# ---------- SWEEP 8: barred tokens, month names, weekday names, bell
print()
print('=== SWEEP 8 BASIS: whole word on [A-Za-z0-9]+ runs of the lower-cased raw text of the ten new files, hyphen a delimiter, every hit read. ===')
barred = ['failed', 'seam', 'roof', 'coping', 'gatehouse', 'custodian', 'melody', 'culling', 'culling order',
          'eastern', 'hemp', 'brother', 'brothers', 'charter', 'bell', 'thirty-six', 'fifty-two',
          'sixty-one', 'sixty-six', 'heroic', 'refugee', 'anchor', 'anchors']
c = Counter(TOKS)
for b in barred:
    n = c.get(b, 0)
    if n:
        ctx = []
        for m in re.finditer(r'.{0,55}\b%s\b.{0,55}' % re.escape(b), RAW):
            ctx.append(m.group(0).replace('\n', ' '))
        print('  HIT  %-14s %d' % (b, n))
        for x in ctx[:6]:
            print('        ...%s...' % x)
    else:
        print('  0    %-14s' % b)
print()
mw = ['Longlight', 'Rainmonth', 'Harvestmonth', 'Fallowmonth', 'Embermonth', 'Wolfmonth', 'Frostmonth',
      'Hearthmonth', 'Goatmonth', 'Thawmonth', 'Mudmonth']
rw = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
      'November', 'December']
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('  main-world month tokens: ' + ' · '.join('%s %d' % (m, len(re.findall(r'\b%s\b' % m, RAW))) for m in mw))
print('  real-world month tokens: ' + ' · '.join('%s %d' % (m, len(re.findall(r'\b%s\b' % m, RAW))) for m in rw))
print('  weekday tokens: ' + ' · '.join('%s %d' % (w, len(re.findall(r'\b%s\b' % w, RAW))) for w in wd))

# ---------- SWEEP 9: self-reference sweep
print()
print('=== SWEEP 9 BASIS: at least sixteen patterns on the ten new files, testing the bare noun as well as the prepositional phrase, and the four phrases in this chapter in a self-referential construction. Every hit read. ===')
pats = [r'in this volume', r'in this book', r'in this chapter', r'in this block', r'in this section',
        r'this volume', r'this book', r'this chapter', r'this block', r'this story', r'this project',
        r'the volume', r'the book', r'the chapter', r'the block', r'the manuscript', r'the page',
        r'the pages', r'on the page', r'this page', r'this paragraph', r'the paragraph',
        r'the narrator', r'the reader', r'the author', r'the text', r'the prose', r'the device',
        r'the devices', r'the manuscript is', r'in this manuscript', r'the state file', r'a chapter',
        r'the chapter', r'the outline', r'this volume', r'a volume', r'the novel', r'this novel']
total = 0
seen = set()
for pat in pats:
    for m in re.finditer(pat, RAW, flags=re.I):
        key = (pat, m.group(0).lower(), RAW[max(0, m.start()-45):m.end()+45].replace('\n', ' '))
        total += 1
        seen.add(key)
        print('  HIT  /%s/  ...%s...' % (pat, key[2]))
print('  total hits: %d  (a sweep that counts one occurrence under two patterns is reporting its own patterns)' % total)

# ---------- SWEEP 10: doubled word and spacing
print()
print('=== SWEEP 10 BASIS: a word of three letters or more immediately repeated, a space before a comma, a space before a full stop, and a lowercase word running straight into a capitalised one, on the ten new files. ===')
pat_dw = re.compile(r'\b(\w{3,})\s+\1\b', re.I)
pat_sc = re.compile(r'\s+[,.]')
pat_lc = re.compile(r'\b[a-z]{3,}[A-Z][a-z]{2,}\b')
tot = 0
for p in NEW:
    t = read(p)
    d = pat_dw.findall(t); s = pat_sc.findall(t); l = pat_lc.findall(t)
    tot += len(d) + len(s) + len(l)
    print('  %-20s doubledword=%s spacecomma=%s spacedot=%s lowerintoCap=%s' % (os.path.basename(p), d or '-', s or '-', s or '-', l or '-'))
print('  total: %d' % tot)
