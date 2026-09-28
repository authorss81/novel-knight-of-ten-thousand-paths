#!/usr/bin/env python3
"""Block 0004 device counter. Bases named before the run, per workspace prompt section 4."""
import re, sys, glob, os
from collections import Counter

BLOCK = ['chapter-%04d.md' % n for n in range(381, 391)]
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'chapters', 'volume-08')
DIR = os.path.normpath(DIR)

def read(f):
    return open(os.path.join(DIR, f), encoding='utf-8').read()

def words(f):
    return len(read(f).split())

def toks(f):
    return re.findall(r'[A-Za-z0-9]+', read(f).lower())

BLOCK_0003_TOTALS = {4,6,7,8,9,10,11,13,14,15,18,19,20,21,23,24,25,27,35,55,67,96,160,12}

def main():
    total = 0
    per_about = []
    print('=== word counts (whitespace split, title line included, each file on its own) ===')
    for f in BLOCK:
        w = words(f)
        total += w
        a = toks(f).count('about')
        per_about.append(a)
        print('%-20s %5d   about %3d  rate %5.2f' % (f, w, a, a / w * 1000))
    print('BLOCK TOTAL: %d' % total)
    print('about total: %d  rate %.2f per 1,000' % (sum(per_about), sum(per_about) / total * 1000))
    print('about per chapter:', ' / '.join('%.2f' % (a / words(f) * 1000) for f, a in zip(BLOCK, per_about)))

    raw = ''.join(read(f) for f in BLOCK)
    tk = re.findall(r'[A-Za-z0-9]+', raw.lower())
    c = Counter(tk)
    print()
    print('=== barred tokens (whole word, hyphen a delimiter) ===')
    barred = ['failed','seam','roof','coping','gatehouse','custodian','melody','culling',
              'culling order','eastern','hemp','brother','charter','bell',
              'thirty-six','fifty-two','sixty-one','sixty-six','failed','heroic']
    for b in barred:
        print('  %-14s %d' % (b, c.get(b, 0)))
    print()
    print('=== filler ===')
    for w in ['nodded','held','wrote','stood','plain','counted','breathed','steady']:
        print('  %-10s %d' % (w, c.get(w, 0)))
    print()
    print('=== phrases ===')
    for ph in ['the whole of','about four people','in that book','on the page','the book','the page',
               'in this volume','in this book','in this chapter','this volume','this book','this chapter',
               'in the book','the chapter','the block','Block 0001','Block 0002','Block 0003',
               'about nine hundred sheets','the office has read','a mark on']:
        print('  %-28s %d' % (ph, raw.count(ph)))
    print('  cut                            %d' % c.get('cut', 0))
    print('  schedule                       %d' % c.get('schedule', 0))
    print('  crossing                       %d' % c.get('crossing', 0))
    print('  toll                           %d' % c.get('toll', 0))
    print('  keeper                         %d' % c.get('keeper', 0))
    print('  steward                        %d' % c.get('steward', 0))
    print('  about four people (token run)  computed below')
    print()
    print('=== punctuation and rules ===')
    print('  --- rules                      %d' % raw.count('\n---\n'))
    for name, ch in [('semicolon',';'),('em dash','—'),('en dash','–'),
                     ('straight dquote','"'),('curly apostrophe','’'),
                     ('curly open single','‘'),('exclamation','!'),('question','?')]:
        print('  %-20s %d' % (name, raw.count(ch)))
    print('  curly open dquote            %d' % raw.count('“'))
    print('  curly close dquote           %d' % raw.count('”'))
    print('  straight apostrophe            %d' % raw.count("'"))
    print()
    print('=== narrator reporting clause ===')
    forms = [('have said since that', r'have said since that'),
             ('have worked out since that', r'have worked out since that'),
             ('have been saying since that', r'have been saying since that'),
             ('could not tell you', r'could not tell you'),
             ('do not know that', r'do not know that'),
             ('do not know how many', r'do not know how many'),
             ('has never once told', r'has never once told'),
             ('are not in a book', r'are not in a book'),
             ('not in a book and', r'not in a book and'),
             ('is not in a book', r'is not in a book'),
             ('is not on a roll', r'is not on a roll')]
    tot_r = 0
    for name, pat in forms:
        n = len(re.findall(pat, raw))
        print('  %-30s %d' % (name, n))
    single = len(re.findall(r'have (?:said|worked out|been saying) since that', raw))
    print('  SINGLE FORM (said/worked out/been saying since that): %d' % single)
    print('  reporting rate per 1,000: %.2f' % (single / total * 1000))
    print()
    print('=== per-file mechanics ===')
    for f in BLOCK:
        t = read(f)
        lines = t.split('\n')
        bad = [i + 1 for i, l in enumerate(lines) if l.count('**') % 2]
        dblrule = len(re.findall(r'\n---\n---\n', t))
        dblblank = len(re.findall(r'\n\n\n', t))
        trail = t.endswith('\n')
        print('  %-20s boldodd=%s doubledrule=%d doubleblank=%d trailnl=%s curly=%d/%d rules=%d' %
              (f, bad if bad else '-', dblrule, dblblank, trail, t.count('“'), t.count('”'), t.count('\n---\n')))
    print()
    print('=== money totals check ===')
    print('  (recurring totals that may not be reused:', sorted(BLOCK_0003_TOTALS), ')')
    money = re.findall(r'((?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|one hundred|one hundred and \w+)[- ]?(?:pence|shillings?))', raw)
    print('  money phrases found:', Counter(money))


if __name__ == '__main__':
    main()
