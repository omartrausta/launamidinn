# encoding: utf-8
def logleg_stada(v):
    for bakki in v:
        if "b" in bakki:
            return True
        else:
            if "u" in bakki and "l" in bakki:
                return False
            elif "l" in bakki and "b" in bakki:
                return False
            else:
                return True
        
def vinstri(v, adili):
    pass

def haegri(v, adili):
    vi, ha=v
    if not adili in vi:
        return False
    if adili in ha:
        return False
    vi = vi.replace(adili,"")
    ha = ha + adili
    return vi, ha