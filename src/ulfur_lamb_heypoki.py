# encoding: utf-8

upphafsstada = ["bulh", ""]
profadar_stodur = ()
lokastada = ["", "bulh"]
keyrir_bat = "b"
faersla = ()


def logleg_stada(stada):
    for bakki in stada:
        if "u" in bakki and "l" in bakki and "b" not in bakki:
            return False
        elif "l" in bakki and "h" in bakki and "b" not in bakki:
            return False
    return True
 
 
def faera(stada,faersla):
    global profadar_stodur
    vinstri = stada[0]
    haegri = stada[1]
    for i in faersla:
        print "i: ", i
        vinstri = vinstri.replace(i,"")
    ny_haegri = haegri + faersla
    ny_stada = [vinstri, ny_haegri]
    ny_stada = "".join(sorted(ny_stada[0])),"".join(sorted(ny_stada[1]))  
    if logleg_stada(ny_stada):
        if ny_stada in profadar_stodur:
            print "stada fannst í prófaðar stöður"
            return stada
        profadar_stodur = profadar_stodur +ny_stada
        print profadar_stodur
        print "ný staða fundin : ", ny_stada
    else:
        print "ólögleg staða", ny_stada
        return stada
    print "return"
    return ny_stada 

 
def keyra(stada):
    stada = "".join(sorted(stada[0])),"".join(sorted(stada[1])) 
    global lokastada
    lokastada = "".join(sorted(lokastada[0])),"".join(sorted(lokastada[1]))
    if stada == lokastada:
        print "lokastöðu náð"
        return
    else:
        for s in stada:
            if keyrir_bat in s:
                uppfaerd_stada = faera(stada,keyrir_bat)
                if uppfaerd_stada == lokastada:
                    print "lokastöðu náð"
                    return
                farthegar = s.replace(keyrir_bat,"")
                for farthegi in farthegar:
                    uppfaerd_stada = faera(stada,keyrir_bat+farthegi)
                    if uppfaerd_stada == lokastada:
                        print "lokastöðu náð"
                        return
                


 
 
                      

        
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
  
  
        
keyra(upphafsstada)

