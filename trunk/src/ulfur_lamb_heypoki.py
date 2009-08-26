# encoding: utf-8
def logleg_stada(vandi):
    for bakki in vandi:
        if "u" in bakki and "l" in bakki:
            return False
        elif "b" in bakki and "u" in bakki and "l" in bakki:
            return True
        elif "l" in bakki and "h" in bakki:
            return False
        elif "l" in bakki and "h" in bakki and "u" in bakki:
            return False
        else:
            return True

        
def vinstri_hlid(v, adili):
    pass

def haegri_hlid(v, adili):
    vinstri, haegri = v
    if not adili in vinstri:
        return False
    if adili in haegri:
        return False
    vinstri = vinstri.replace(adili, "")
    haegri = haegri + adili
    return vinstri, haegri

vandi = ["bulh", ""]
print vandi
print logleg_stada(vandi)
vandi = haegri_hlid(vandi, "l")
print vandi
print logleg_stada(vandi)
vandi = haegri_hlid(vandi, "h")
print vandi
print logleg_stada(vandi)
vandi = haegri_hlid(vandi, "u")
print vandi
print logleg_stada(vandi)
