REG_EXPR_TO_CALC_SENT = r"[.!?]+"
REG_EXPR_TO_CALC_NON_DEC_SENT = r"[!?]+"
REG_EXPR_TO_WORD = r"\b[a-zA-Z\d]+\b"

WORDS_CONTAIN_ONE_CHAR = [
    ' etc.', ' vs.', ' jr.', ' sr.', ' mr.', ' mrs.', ' smb.', ' smth.', ' adj.', ' pp.', ' par.', ' ex.',
    ' edu.', ' appx.', ' sec.', ' gm.', ' cm.', ' yr.', ' jan.', ' feb.', ' mar.',
    ' apr.', ' jun.', ' jul.', ' aug.', ' sep.', ' oct.', ' nov.', ' dec.', ' mon.', ' tue.', ' wed.', ' thu', ' fri.'
    , ' sat.'
]

WORDS_CONTAIN_TWO_CHAR = ['e.g.', 'i.e.', 'p.s.', 'p.m.', 'a.m.']

WORDS_CONTAIN_THREE_CHAR = ['v.i.p.', 'p.p.s.']

K = 4
N = 10
