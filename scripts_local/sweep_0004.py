#!/usr/bin/env python3
"""Sweeps 1 to 5 for Batch 0004. Basis named in the printout for each sweep."""
import re, os, glob, itertools
from collections import Counter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
NEW = [os.path.join(ROOT, 'chapters/volume-08', 'chapter-%04d.md' % n) for n in range(381, 391)]
ALL = sorted(glob.glob(os.path.join(ROOT, 'chapters/volume-*', 'chapter-*.md')))
PRIOR = [p for p in ALL if p not in NEW]
print('new files: %d   prior files: %d   total: %d' % (len(NEW), len(PRIOR), len(ALL)))


def read(p):
    return open(p, encoding='utf-8').read()


def paras(p):
    out = []
    for b in read(p).split('\n'):
        b = b.strip()
        if not b or b == '---' or b.startswith('#'):
            continue
        out.append(b)
    return out


# ---------- SWEEP 1: clause level at 0.60, Jaccard on distinct lower-cased words of 4+ letters, paragraphs of 25+ words
def sweep1():
    print()
    print('=== SWEEP 1 BASIS: Jaccard on sets of distinct lower-cased words of four letters or more, over paragraphs of 25 words or more, the ten new files against all %d prior chapters. Threshold 0.60 both directions reported. ===' % len(PRIOR))
    def vec(text):
        ws = re.findall(r'[a-z]{4,}', text.lower())
        return set(ws)
    newp = []
    for p in NEW:
        for i, t in enumerate(paras(p)):
            if len(t.split()) >= 25:
                newp.append((os.path.basename(p), i, t, vec(t)))
    hits = []
    for pn, i, t, v in newp:
        for q in PRIOR:
            for j, u in enumerate(paras(q)):
                if len(u.split()) < 25:
                    continue
                w = vec(u)
                if not v or not w:
                    continue
                inter = len(v & w)
                if inter == 0:
                    continue
                jac = inter / len(v | w)
                small = min(len(v), len(w))
                con = inter / small
                if jac >= 0.60:
                    hits.append((round(jac, 3), round(con, 3), pn, i, os.path.basename(q), j, t[:90]))
    hits.sort(reverse=True)
    print('paragraph pairs examined: %d new paragraphs' % len(newp))
    print('hits at 0.60 Jaccard: %d   (containment is reported beside each hit and is NOT a trigger)')
    for h in hits:
        print('  jac=%s con=%s  %s p%s vs %s p%s :: %s' % h)


# ---------- SWEEP 2: shingle containment 0.40, 12 and 8 word, paragraphs with 20+ shingles
def sweep2():
    print()
    print('=== SWEEP 2 BASIS: 12-word and 8-word contiguous shingles, containment over the smaller set, restricted to paragraphs with 20 or more shingles, threshold 0.40, the ten new against all prior. ===')
    for n in (12, 8):
        newsh = {}
        for p in NEW:
            for i, t in enumerate(paras(p)):
                toks = re.findall(r"[a-z0-9']+", t.lower())
                sh = set(tuple(toks[j:j + n]) for j in range(len(toks) - n + 1))
                if len(sh) >= 20:
                    newsh[(os.path.basename(p), i)] = sh
        priorsh = {}
        for q in PRIOR:
            for i, t in enumerate(paras(q)):
                toks = re.findall(r"[a-z0-9']+", t.lower())
                sh = set(tuple(toks[j:j + n]) for j in range(len(toks) - n + 1))
                if len(sh) >= 20:
                    priorsh[(os.path.basename(q), i)] = sh
        npairs = 0
        detail = []
        for k, a in newsh.items():
            for k2, b in priorsh.items():
                inter = len(a & b)
                if not inter:
                    continue
                c = inter / min(len(a), len(b))
                if c >= 0.40:
                    npairs += 1
                    detail.append((round(c, 3), k, k2))
        detail.sort(reverse=True)
        print('  %d-word shingles: new paragraphs qualifying %d, prior paragraphs qualifying %d, pairs at 0.40 containment: %d' %
              (n, len(newsh), len(priorsh), npairs))
        for d in detail[:12]:
            print('    ', d)


# ---------- SWEEP 3: raw token, headings stripped, 15-word maximal shared runs
def norm_tokens(p, bold=True):
    t = read(p)
    t = re.sub(r'^#.*$', ' ', t, flags=re.M)
    t = t.replace('**', ' ')
    t = t.replace('---', ' ')
    t = t.lower()
    return re.findall(r"[a-z0-9']+", t)


def longest_run(a, b):
    # a, b token lists; return longest maximal shared contiguous run length
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1)
    best = 0
    bi = 0
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
                    bi = j
        prev = cur
    run = b[bi - best:bi]
    return best, ' '.join(run)


def sweep3():
    print()
    print('=== SWEEP 3 BASIS: raw tokens, headings stripped, asterisks and rules removed, lower-cased, no paragraph boundary respected, bold datelines kept in, 15-word seeds, [a-z0-9] runs. Reported as the longest maximal shared run per new file. ===')
    newt = {os.path.basename(p): norm_tokens(p) for p in NEW}
    priort = {os.path.basename(p): norm_tokens(p) for p in PRIOR}
    col = []
    for k, a in newt.items():
        best = 0
        bestrun = ''
        bestsrc = ''
        for k2, b in priort.items():
            L, r = longest_run(a, b)
            if L > best:
                best, bestrun, bestsrc = L, r, k2
        col.append(best)
        print('  %-20s longest run against prior: %3d  <- %s' % (k, best, bestsrc))
        if best >= 15:
            print('      run: %s' % bestrun)
    print('  column: %s' % ' / '.join(str(x) for x in col))
    print('  new against new:')
    keys = list(newt)
    col2 = []
    for i in range(len(keys)):
        best = 0
        bestrun = ''
        for j in range(len(keys)):
            if i == j:
                continue
            L, r = longest_run(newt[keys[i]], newt[keys[j]])
            if L > best:
                best, bestrun = L, r
        col2.append(best)
        print('    %-20s longest internal run: %3d  <- %s' % (keys[i], best, bestrun[:160]))
    print('  internal column: %s' % ' / '.join(str(x) for x in col2))


# ---------- SWEEP 4: exact duplicate paragraphs, 12+ words, whitespace normalised
def sweep4():
    print()
    print('=== SWEEP 4 BASIS: exact duplicate paragraphs, whitespace-normalised, 12 words or more, the ten new against the whole manuscript and against themselves. ===')
    def blocks(files):
        d = {}
        for p in files:
            for i, t in enumerate(paras(p)):
                k = ' '.join(t.split()).lower()
                if len(k.split()) >= 12:
                    d.setdefault(k, []).append('%s p%s' % (os.path.basename(p), i))
        return d
    newd = blocks(NEW)
    alld = blocks(ALL)
    dup = {k: v for k, v in alld.items() if len(v) > 1}
    newinvolved = []
    for k, v in dup.items():
        if any(re.match(r'chapter-03(8[1-9]|90)', x) for x in v):
            newinvolved.append(v)
    print('  duplicate paragraph keys in the whole manuscript: %d' % len(dup))
    print('  of which a new-file paragraph is one of the copies: %d' % len(newinvolved))
    for v in newinvolved[:20]:
        print('    ', v)
    print('  scope: all %d chapter files in chapters/volume-01 to chapters/volume-08' % len(ALL))


# ---------- SWEEP 5: bold parity, doubled rules, double blank lines, missing full stop
def sweep5():
    print()
    print('=== SWEEP 5 BASIS: bold marker count per file and per line, doubled --- check, double blank line check, and a missing-full-stop sweep on the pattern a lowercase word, a space, a comma, a space, a capitalised common word. ===')
    pat = re.compile(r'\b[a-z]{3,} , [A-Z][a-z]{3,}\b')
    for p in NEW:
        t = read(p)
        lines = t.split('\n')
        bad = [i + 1 for i, l in enumerate(lines) if l.count('**') % 2]
        dr = len(re.findall(r'\n---\n---\n', t)) + len(re.findall(r'^---\s*\n---\s*$', t, flags=re.M))
        db = len(re.findall(r'\n\n\n', t))
        ms = pat.findall(t)
        print('  %-20s boldodd=%s doubledrule=%d doubleblank=%d trailnl=%s curly=%d/%d rules=%d missingfullstop=%s' %
              (os.path.basename(p), bad if bad else 'none', dr, db, t.endswith('\n'), t.count('“'), t.count('”'),
               t.count('\n---\n'), ms if ms else 'none'))


if __name__ == '__main__':
    sweep1()
    sweep2()
    sweep3()
    sweep4()
    sweep5()
