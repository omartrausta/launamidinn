# encoding: utf-8
def logleg_stada(v):
    for bakki in v:
        print bakki
        if "b" in bakki:
            return True
        else:
            if "u" in bakki and "l" in bakki:
                return False
            elif "l" in bakki and "h" in bakki:
                return False
            else:
                return True

        
def vinstri_hlid(v, adili):
    vinstri, haegri = v
    if not adili in vinstri:
        return False
    if adili in haegri:
        return False
    haegri = haegri.replace("",adili)
    vinsri = vinstri + adili
    return vinstri, haegri

def haegri_hlid(v, adili):
    vinstri, haegri = v
    if not adili in vinstri:
        return False
    if adili in haegri:
        return False
    vinstri = vinstri.replace(adili, "")
    haegri = haegri + adili
    return vinstri, haegri

def keyra_forrit(stodur):
    pass       
        
vandi = ["bulh", ""]
vandi = vinstri_hlid(vandi, "l")
print vandi

#stodur = ["bulh","bul", "bu"]
#vandi = ["bulh", ""]
#vandi = haegri_hlid(vandi, "b")
#vandi = haegri_hlid(vandi, "l")
#print logleg_stada(vandi)

