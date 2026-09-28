#!/usr/bin/env python3
"""Sweep 6: derive the whole chain from the single anchor and audit every dated row of outline/volume-08.md section 17,
then audit the ten chapter datelines against the derivation. Nothing is read off a chapter and then believed."""
import re, os

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MONTHS = ['Longlight', 'Rainmonth', 'Harvestmonth', 'Fallowmonth', 'Embermonth', 'Wolfmonth',
          'Frostmonth', 'Hearthmonth', 'Goatmonth', 'Thawmonth', 'Mudmonth']
WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
NUMWORDS = {'first':1,'second':2,'third':3,'fourth':4,'fifth':5,'sixth':6,'seventh':7,'eighth':8,'ninth':9,'tenth':10,
 'eleventh':11,'twelfth':12,'thirteenth':13,'fourteenth':14,'fifteenth':15,'sixteenth':16,'seventeenth':17,'eighteenth':18,
 'nineteenth':19,'twentieth':20,'twenty-first':21,'twenty-second':22,'twenty-third':23,'twenty-fourth':24,'twenty-fifth':25,
 'twenty-sixth':26,'twenty-seventh':27,'twenty-eighth':28,'twenty-ninth':29,'thirtieth':30}
L1 = 606  # Longlight 1 = day 606, from day 630 = Longlight 25

def date(d):
    off = d - L1
    m = off // 30
    day = off % 30 + 1
    if m >= len(MONTHS):
        return None, None, None
    return MONTHS[m], day, (317 if d <= 875 else 318)

def wd(d):
    return WEEK[(d - 630) % 7]

def market(d):
    return wd(d) in ('Sat', 'Thu')

print('=== SWEEP 6 BASIS: chain built forward from day 630 = Longlight 25, YR 317, a Monday, on the carried thirty-day month (Longlight 1 = day 606), weekday by (day - 630) mod 7, market days the Saturdays and the Thursdays, year YR 317 to day 875 and YR 318 from day 876. Run twice; the second run is the one reported. ===')
for d in (630, 811, 840, 870, 875, 876, 900, 930):
    print('  anchor check  day %3d -> %s %d, YR %d, a %s, %s' % (d, date(d)[0], date(d)[1], date(d)[2], wd(d), 'market' if market(d) else 'not a market day'))

txt = open(os.path.join(ROOT, 'outline/volume-08.md'), encoding='utf-8').read()
grab = False
tbl = []
for line in txt.split('\n'):
    if line.startswith('| Day | Date | Weekday |'):
        grab = True
        continue
    if grab:
        if not line.startswith('|'):
            break
        tbl.append(line)
data = [l for l in tbl if not set(l.replace('|', '').replace(' ', '')) <= set('-:')]
print()
print('section 17 table: %d lines, of which the head is one and the rule is one, so dated rows = %d' % (len(tbl), len(data)))
bad = wbad = cabad = 0
print()
print('audit of every dated row, on month, day of month, year and weekday, and on the chapter-attribution column:')
for line in data:
    m = re.match(r'^\|\s*\*{0,2}(\d{3})\*{0,2}\s*\|\s*\*{0,2}([A-Za-z]+)\s*(\d+)(?:,\s*YR\s*(\d+))?\*{0,2}\s*\|\s*\*{0,2}(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\*{0,2}\s*\|\s*([^|]*)\|', line)
    if not m:
        print('  UNPARSED ROW: %s' % line[:90])
        bad += 1
        continue
    d = int(m.group(1)); mon = m.group(2); dd = int(m.group(3))
    yr = int(m.group(4)) if m.group(4) else 317
    w = m.group(5); rest = m.group(6)
    em, ed, ey = date(d); ew = wd(d)
    notes = []
    if (em, ed, ey) != (mon, dd, yr):
        bad += 1
        notes.append('DATE MISMATCH, derived %s %d YR %d' % (em, ed, ey))
    if ew != w:
        wbad += 1
        notes.append('WEEKDAY MISMATCH, derived %s' % ew)
    for ch in re.findall(r'Chapter (\d{4})', rest):
        n = int(ch)
        if not (351 <= n <= 400):
            continue
        dt = open(os.path.join(ROOT, 'chapters/volume-08', 'chapter-%04d.md' % n), encoding='utf-8').read().split('\n')[2]
        m2 = re.search(r'\*\*The ([a-z-]+) day of ([A-Za-z]+), YR (\d+), a ([A-Za-z]+)', dt)
        if not m2:
            cabad += 1
            notes.append('Chapter %s DATELINE NOT PARSED' % ch)
            continue
        num, cmon, cyr, cw = int(m2.group(1)), m2.group(2), int(m2.group(3)), m2.group(4)
        found = None
        for cand in range(1, 1000):
            pass
        found = next((c for c in range(1, 1000)
                      if date(c) == (cmon, num, cyr) and wd(c) == cw[:3].title() and c >= 600), None)
        # weekday word match
        found = None
        for c in range(600, 1000):
            em2, ed2, ey2 = date(c)
            if (em2, ed2, ey2) == (cmon, num, cyr):
                if WEEK[wd(c) == 0 and 0 or (c - 630) % 7] == cw[:3].title():
                    found = c
                    break
        if found is None:
            cabad += 1
            notes.append('Chapter %s DATELINE DATE NOT LOCATED' % ch)
        elif found != d:
            cabad += 1
            notes.append('CHAPTER COLUMN MISMATCH: row day %s, Chapter %s dateline is day %d' % (d, ch, found))
        else:
            notes.append('Chapter %s OK' % ch)
    print('  day %3s %-14s %2d YR %d %-3s  %s' % (d, mon, dd, yr, w, '; '.join(notes) if notes else 'clean'))
print()
print('dated rows audited: %d   date-field mismatches: %d   weekday mismatches: %d   chapter-column findings: %d' % (len(data), bad, wbad, cabad))

print()
print('the ten chapter datelines, each located in the chain by deriving, not by reading:')
for n in range(381, 391):
    dt = '\n'.join(open(os.path.join(ROOT, 'chapters/volume-08', 'chapter-%04d.md' % n), encoding='utf-8').read().split('\n')[:8])
    m2 = re.search(r'\*\*The ([a-z-]+) day of ([A-Za-z]+), YR (\d+), a ([A-Za-z]+)', dt)
    word, mon, yr, w = m2.group(1), m2.group(2), int(m2.group(3)), m2.group(4)
    num = NUMWORDS[word] if not word.isdigit() else int(word)
    cands = [c for c in range(600, 1000) if date(c) == (mon, num, yr)]
    flag = 'and a market day' in dt
    notflag = 'not a market day' in dt
    okweek = bool(cands) and wd(cands[0]) == w[:3].title()
    print('  Chapter %d: "The %s day of %s, YR %d, a %s" -> derived day %s, derived weekday %s, page weekday matches: %s; page market flag: %s, derived market: %s' %
          (n, word, mon, yr, w, cands[0] if cands else 'NOT FOUND', wd(cands[0]) if cands else '-', okweek, ('market' if flag else 'not a market') if not notflag else 'not a market', 'market' if (cands and market(cands[0])) else 'not a market'))

print()
mk = [d for d in range(811, 871) if market(d)]
sats = [d for d in range(811, 871) if wd(d) == 'Sat']
print('Block 4 frame: day 811 = %s %d, %s, and day 870 = %s %d, %s; 60 days inclusive, 59 elapsed; the year does not turn in this block.'
      % (date(811)[0], date(811)[1], wd(811), date(870)[0], date(870)[1], wd(870)))
print('Block 4 market days derived from the anchor: %d  %s' % (len(mk), mk))
print('Block 4 Saturdays derived: %d  %s' % (len(sats), sats))
pmk = [816, 818, 823, 825, 830, 832, 837, 839, 844, 846, 851, 853, 858, 860, 865, 867]
print('The block prompt printed this market-day list: %s' % pmk)
print('  of the printed sixteen, derived to be market days: %s' % [d for d in pmk if market(d)])
print('  their derived weekdays: %s' % [wd(d) for d in pmk])
print('  derived list minus printed list: %s' % sorted(set(mk) - set(pmk)))
print('  printed list minus derived list: %s' % sorted(set(pmk) - set(mk)))
print('The block prompt printed the Saturday list 817, 824, 831, 838, 845, 852, 859, 866; derived Saturdays: %s' % sats)
