# encoding: utf-8

upphafsstada = ["bulh", ""]
profadar_stodur = []
lokastada = ["", "bulh"]
keyrir_bat = "b"


def logleg_stada(stada):
    for bakki in stada:
        if "u" in bakki and "l" in bakki and "b" not in bakki:
            return False
        elif "l" in bakki and "h" in bakki and "b" not in bakki:
            return False
    return True
 
 
def faera(a,b,stada,faersla):
    global profadar_stodur
    vinstri = stada[a]
    haegri = stada[b]
    for i in faersla:
        print "i: ", i
        vinstri = vinstri.replace(i,"")
    ny_haegri = haegri + faersla
    ny_stada = [vinstri, ny_haegri]
    ny_stada = "".join(sorted(ny_stada[a])),"".join(sorted(ny_stada[b]))  
    if logleg_stada(ny_stada):
        if ny_stada in profadar_stodur:
            print "stada fannst í prófaðar stöður"
            return []
        profadar_stodur.append(ny_stada)
        print "profadar stodur: ", profadar_stodur
        print "ný staða fundin : ", ny_stada
    else:
        print "ólögleg staða", ny_stada
        return []
    print "return"
    return ny_stada 

 
def keyra(stada):
    stada = "".join(sorted(stada[0])),"".join(sorted(stada[1])) 
    global lokastada
    lokastada = "".join(sorted(lokastada[0])),"".join(sorted(lokastada[1]))
    if stada == lokastada:
        print "lokastöðu náð"
        return stada
    else:
        for i in range(0,2):
            if keyrir_bat in stada[i]:
                uppfaerd_stada = faera(i,1-i,stada, keyrir_bat)
                if uppfaerd_stada != []:
                    keyra(uppfaerd_stada)
                    break
                farthegar = stada[i].replace(keyrir_bat,"")
                for farthegi in farthegar:
                    uppfaerd_stada = faera(i,1-i,stada, keyrir_bat+farthegi)
                    if uppfaerd_stada != []:
                        keyra(uppfaerd_stada)
                        break
                    
                    

  
        
keyra(upphafsstada)

