import random
import turtle
import time

# def start():
# return (Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1)

# def start_igre():
#     global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
#     screen.bgpic('backdrop5.png')
#     tezavnost=int(input("Izberi tezavnost igre."))
#     while 0<tezavnost<4:
#         tezavnost=int(input("Ta tezavnost ni na moznost."))
#     globals().update(locals())

def nastavitve_igre_in_start_2():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    stskatel=int(input("S koliko skatlami zelis igrati?"))
    while not (3<=stskatel):
        print("Nemores igrati z manj kot tremi skatljami.")
        stskatel=int(input("S koliko skatlami zelis igrati?"))
    stpalic=int(input("Do koliko palic zelis na skatlo?"))
    while not (6<=stpalic):
        print("Igranje s tako malo palicami je nesmiselno.")
        print("Igraj najmanj s sestimi.")
        stpalic=int(input("Do koliko palic zelis na skatlo?"))  
    while not (256>=stpalic):
        print("Igranje s tako veliko palicami je nesmiselno.")
        print("Izberi kvoto nizjo od 256.")
        stpalic=int(input("Do koliko palic zelis na skatlo?"))
    Ppalice=stpalic
    Mpalice=1
    t.goto(400,-400)# OOOOOOOOOOOOO
    globals().update(locals())
    
def risanje_palic():
    objavi_risanje_palic()
    globals().update(locals())
    
def generacija_stopenjskih_spremenljivk():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    x=0
    for i in range (len(skatle)):
        x+=1
        xREV=(len(vrednosti_stopenj))+1
        while not skatle_za_racunanje[(x)-1]==0:
            #print(skatle_za_racunanje)#koment
            #print(x,xREV,vrednosti_stopenj)#koment
            xREV-=1
            if skatle_za_racunanje[(x)-1]-vrednosti_stopenj[(xREV)-1]>=0:
                stopnje[(xREV)-1]+=1
                skatle_za_racunanje[(x)-1]=(skatle_za_racunanje[(x)-1]-vrednosti_stopenj[(xREV)-1])
                if signal==1:
                    if xREV==najvecja_liha_stopnja:
                        skatle_z_liho_stopnjo.append(skatle[(x)-1])
    globals().update(locals())
                        
def poteza_igralca():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    barva=0
    #t.goto(-200,-80)# OOOOOOOOOOOOO
    skatla_za_zmanjsevanje=int(input("Iz katere skatle zelis vzeti palice? (napisi le stevilko)"))
    if skatle[(skatla_za_zmanjsevanje)-1]==0:
        while not skatle[(skatla_za_zmanjsevanje)-1]>0:
            skatla_za_zmanjsevanje=int(input("Ta skatla je ze prazna izberi drugo."))
    if (len(skatle))<skatla_za_zmanjsevanje:
        while not (len(skatle))>=skatla_za_zmanjsevanje:
            skatla_za_zmanjsevanje=int(input("Mislim, da si se zatipkal, poizkusi ponovno."))
    stevilo_palic_za_brisanje=int(input("Koliko palic zelis vzeti?"))
    #print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"a")#koment
    if stevilo_palic_za_brisanje>skatle[(skatla_za_zmanjsevanje)-1]:
        while not stevilo_palic_za_brisanje<=skatle[(skatla_za_zmanjsevanje)-1]:
            stevilo_palic_za_brisanje=int(input("V tej skatli ni palic."))
    #t.goto(400,-400)# OOOOOOOOOOOOO
    objavi_brisanje()# OOOOOOOOOOOOO
    zmagovalec=1
    globals().update(locals())
    #print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"b")#koment


def vse_skatle_prazne():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    signal_5=0
    ciklicni_x_9=0
    for i in range (len(skatle)):
        ciklicni_x_9+=1
        if not skatle[(ciklicni_x_9)-1]==0:
            signal_5=1
    if signal_5==0:
        konec=1
    globals().update(locals())

def random_poteza():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    odstranitev_nic_skatel()
    barva=1
    signal_2=0
    #print("tle")#koment
    random_poteza_skatle=random.randint(1, (len(skatle)))
    if (len(prazne_skatle))>0:
        while not signal_2==1:
            random_poteza_skatle=random.randint(1, (len(skatle)))
            signal_4=0
            ciklicni_x_7=0
            for i in range (len(prazne_skatle)):
                ciklicni_x_7+=1
                if random_poteza_skatle==prazne_skatle[(ciklicni_x_7)-1]:
                    signal_4=1
            if signal_4==0:
                signal_2=1
                #print(random_poteza_skatle)#koment
    #print("tle2")#koment
    #print(random_poteza_skatle, skatle[(random_poteza_skatle)-1], (len(skatle)))#koment
    if skatle[(random_poteza_skatle)-1]==1:
        random_poteza_palce=1
    else:
        random_poteza_palce=random.randint(1, skatle[(random_poteza_skatle)-1])
    pomoc_3=0
    signal_6=0
    ciklicni_x_10=0
    for i in range (len(skatle)):
        ciklicni_x_10+=1
        if skatle[(ciklicni_x_10)-1]==0:
            signal_6+=1
        else:
            pomoc_3=skatle[(ciklicni_x_10)-1]
    if (len(skatle))-signal_6==1:
        random_poteza_palce=pomoc_3
    skatla_za_zmanjsevanje=random_poteza_skatle
    stevilo_palic_za_brisanje=random_poteza_palce
    #print(skatla_za_zmanjsevanje)#koment
    #print(stevilo_palic_za_brisanje)#koment
    objavi_brisanje()# OOOOOOOOOOOOO
    zmagovalec=0
    globals().update(locals())
    
def odstranitev_nic_skatel():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    ciklicni_x_6=0
    for i in range (len(skatle)):
        ciklicni_x_6+=1
        if skatle[(ciklicni_x_6)-1]==0:
            ciklicni_x_8=0
            signal_3=0
            for i in range (len(prazne_skatle)):
                ciklicni_x_8+=1
                if ciklicni_x_6==prazne_skatle[(ciklicni_x_8)-1]:
                    signal_3=1
            if signal_3==0:
                prazne_skatle.append(ciklicni_x_6)
            if (len(prazne_skatle))==0:
                prazne_skatle.append(ciklicni_x_6)
    #print(skatle,prazne_skatle)#koment
    globals().update(locals())
    
def racunalniska_poteza():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    barva=1
    signal=0
    refresh_stopnje_stopnje_za_zmanjsevanje()
    polnjenje_skatel_za_racunanje()
    generacija_stopenjskih_spremenljivk()
    h=0
    najvecja_liha_stopnja=0
    ciklicni_x=(len(stopnje))
    aREV=(len(stopnje))+1
    while not ciklicni_x==0:
        ciklicni_x-=1
        aREV-=1
        if stopnje[(aREV)-1]%2>0:
            najvecja_liha_stopnja=aREV
            ciklicni_x=0
            h=1
    if h==0:
        random_poteza()
    else:
        signal=1
        refresh_stopnje_stopnje_za_zmanjsevanje()
        polnjenje_skatel_za_racunanje()
        generacija_stopenjskih_spremenljivk()
        dolocanje_najvecjega_stevila_z_liho_stopnjo()
        dolocanje_skatle_za_zmanjsevanje()
        izracun_skatel_z_liho_stopnjo()
        izracunanje_stevila_ki_ga_zmanjsa_racunalnik()
        #print(skatla_za_zmanjsevanje)#koment
        objavi_brisanje()
    zmagovalec=0
    globals().update(locals())
    
def refresh_stopnje_stopnje_za_zmanjsevanje():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    ciklicni_x_4=(len(stopnje))
    for i in range (len(stopnje)):
        ciklicni_x_4-=1
        if not stopnje[(ciklicni_x_4)-1]==0:
            stopnje_skatle_za_zmanjsevanje[(ciklicni_x_4)-1]=0
            stopnje[(ciklicni_x_4)-1]=0
    globals().update(locals())
            
def polnjenje_skatel_za_racunanje():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    y=0
    for i in range (len(skatle)):
        y+=1
        skatle_za_racunanje[(y)-1]=skatle[(y)-1]
    globals().update(locals())
        
def dolocanje_najvecjega_stevila_z_liho_stopnjo():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    while not (len(skatle_z_liho_stopnjo))==1:
        c=0
        c+=1
        if skatle_z_liho_stopnjo[(c)-1]>skatle_z_liho_stopnjo[(c+1)-1]:
            del skatle_z_liho_stopnjo[(c+1)-1]
        else:
            del skatle_z_liho_stopnjo[(c)-1]
    globals().update(locals())

def dolocanje_skatle_za_zmanjsevanje():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    ciklicni_x_5=0
    if (len(skatle))==1:
        skatla_za_zmanjsevanje=1
    else:
        for i in range (len(skatle)):
            ciklicni_x_5+=1
            if skatle[(ciklicni_x_5)-1]==skatle_z_liho_stopnjo[(1)-1]:
                skatla_za_zmanjsevanje=ciklicni_x_5
    globals().update(locals())
    #print(skatla_za_zmanjsevanje)#koment

def izracun_skatel_z_liho_stopnjo():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    pomoc_2=skatle_z_liho_stopnjo[(1)-1]
    xREV=(len(vrednosti_stopenj))+1
    while not xREV==0:
        xREV-=1
        if (skatle_z_liho_stopnjo[(1)-1]-vrednosti_stopenj[(xREV)-1])>=0:
            stopnje_skatle_za_zmanjsevanje[(xREV)-1]+=1
            skatle_z_liho_stopnjo[(1)-1]=skatle_z_liho_stopnjo[(1)-1]-vrednosti_stopenj[(xREV)-1]
    globals().update(locals())

def izracunanje_stevila_ki_ga_zmanjsa_racunalnik():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    b=0
    if (len(skatle))==1:
        stevilo_palic_za_brisanje=skatle[(1)-1]
        skatla_za_zmanjsevanje=1
    else:
        while not b==(len(stopnje_skatle_za_zmanjsevanje)):
            b+=1
            if stopnje[(b)-1]>0:
                if stopnje[(b)-1]%2==0:
                    if stopnje_skatle_za_zmanjsevanje[(b)-1]==1:
                        skatle_z_liho_stopnjo[(1)-1]=skatle_z_liho_stopnjo[(1)-1]+vrednosti_stopenj[(b)-1]
                else:
                    if stopnje_skatle_za_zmanjsevanje[(b)-1]==0:
                        skatle_z_liho_stopnjo[(1)-1]=skatle_z_liho_stopnjo[(1)-1]+vrednosti_stopenj[(b)-1]
            stevilo_palic_za_brisanje=pomoc_2-skatle_z_liho_stopnjo[(1)-1]
    globals().update(locals())

def tezavnost_igre():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    screen.bgpic('backdrop5.png')
    screen.update()
    tezavnost=int(input("Izberi tezavnost igre."))
    while not 0<tezavnost<4:
        tezavnost=int(input("Ta tezavnost ni mogoca."))
    globals().update(locals())

def generiranje_vrednosti_stopenj():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    a_sen_pac=0
    #vrednosti_stopenj=[]#koment
    #stopnje=[]#koment
    #stopnje_skatle_za_zmanjsevanje=[]#koment
    for i in range (9):
        vrednosti_stopenj.append(2**a_sen_pac)
        a_sen_pac+=1
        stopnje.append(0)
        stopnje_skatle_za_zmanjsevanje.append(0)
        #print(vrednosti_stopenj)#koment
    globals().update(locals())
    
#OPOMNIK: zacasno izklojucen blok
def length_stopenj_brez_nic():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    nenicelna_dolzina_stopenj=0
    ciklicni_x_2=(len(stopnje))
    while not ciklicni_x_2==0:
        ciklicni_x_2-=1
        if stopnje[(ciklicni_x_2)-1]>0:
            nenicelna_dolzina_stopenj=ciklicni_x_2
            ciklicni_x_2=0
    globals().update(locals())
   
def objavi_start():
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    #t.goto(-300,300) #koment
    globals().update(locals())
    
def objavi_izbrisi_svincnik():
    t=turtle.Turtle()
    t.clear()
    globals().update(locals())

def zp():
    t.pendown()
    t.pensize(7)
    t.color("black")
    t.hideturtle()
    t.setheading(90)
    t.forward(20)
    t.penup()
    globals().update(locals())

def objavi_risanje_palic():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    n=0
    for i in range (stskatel):
        t.goto(-223,(165-(37*n)))
        n+=1
        nakljucno_stevilo_palic=0
        #Ppalice=8#koment
        #Mpalice=1#koment
        nakljucno_stevilo_palic=random.randint(Mpalice,Ppalice)
        for i in range (nakljucno_stevilo_palic):
            t.penup()
            t.setheading(0)
            t.forward(20)
            t.setheading(270)
            t.forward(20)
#             print("n je ",n)
#             print(t.xcor())#koment
#             print(t.ycor())#koment
            zp()
        skatle.append(nakljucno_stevilo_palic)
        skatle_za_racunanje.append(nakljucno_stevilo_palic)
    globals().update(locals())

def objavi_brisanje():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    if barva==1:
        #print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"c",barva)#koment
        t.goto((-203+(20*(skatle[(skatla_za_zmanjsevanje)-1]))),(156-(37*(skatla_za_zmanjsevanje-1))))
#         print(t.xcor())#koment
#         print(t.ycor())#koment
        for i in range (stevilo_palic_za_brisanje):
            t.setheading(180)
            t.forward(20)
            sprite1()
            #t.goto(-300,300)
        skatle[(skatla_za_zmanjsevanje)-1]=(skatle[(skatla_za_zmanjsevanje)-1]-stevilo_palic_za_brisanje)
    else:
        druga_figura()
    globals().update(locals())

def druga_figura():
    global stopnje_skatle_z_liho_stopnjo,barva,Mpalice,Ppalice,a,a_pomoc,stopnje,vrednosti_stopenj,aREV,b,c,ciklicni_x,ciklicni_x_2,ciklicni_x_3,ciklicni_x_4,ciklicni_x_5,ciklicni_x_6,ciklicni_x_7ciklicni_x_9,ciklicni_x_10,konec,n,najvecja_liha_stopnja,nakljucno_stevilo_palic,nenicelna_dolzina_stopenj,pomoc_2,pomoc_3,random_poteza_palce,random_poteza_skatle,signal,signal_2,signal_3,signal_4,signal_5,signal_6,skatla_za_zmanjsevanje,stevilo_palic_za_brisanje,stpalic,stskatel,tezavnost,x,xREV,y,zmagovalec,prazne_skatle,skatle,skatle_z_liho_stopnjo,skatle_za_racunanje,stopnje_skatle_za_zmanjsevanje,ciklicni_x_11,posebnost_1,posebnost_2,signal_7,lovro_1
    t.goto((-203+(20*(skatle[(skatla_za_zmanjsevanje)-1]))),(156-(37*(skatla_za_zmanjsevanje-1))))
#     print(skatle[(skatla_za_zmanjsevanje)-1],skatla_za_zmanjsevanje)#koment
    for i in range (stevilo_palic_za_brisanje):
#         print(t.xcor())#koment
#         print(t.ycor())#koment
#         print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"d")#koment
        t.setheading(180)
        t.forward(20)
        sprite2()
    skatle[(skatla_za_zmanjsevanje)-1]=(skatle[(skatla_za_zmanjsevanje)-1]-stevilo_palic_za_brisanje)
    globals().update(locals())

def sprite1():
    t.pendown()
    t.pensize(5)
    t.hideturtle()
    t.color("blue")
    t.setheading(135)
    t.forward(4)
    t.setheading(315)
    t.forward(8)
    t.setheading(135)
    t.forward(4)
    t.setheading(180)
    t.penup()
    globals().update(locals())
    
def sprite2():
    t.pendown()
    t.pensize(5)
    t.hideturtle()
    t.color("green")
    t.setheading(45)
    t.forward(4)
    t.setheading(225)
    t.forward(8)
    t.setheading(45)
    t.forward(4)
    t.setheading(180)
    t.penup()
    globals().update(locals())
    
Mpalice=0
Ppalice=0
a=0
a_pomoc=0
stopnje=[]
vrednosti_stopenj=[]
aREV=(len(stopnje))+1
b=0
c=0
ciklicni_x=0
ciklicni_x_2=0
ciklicni_x_3=0
ciklicni_x_4=0
ciklicni_x_5=0
ciklicni_x_6=0
ciklicni_x_7=0
ciklicni_x_8=0
ciklicni_x_9=0
ciklicni_x_10=0
konec=0
h=0    
n=0
najvecja_liha_stopnja=0
nakljucno_stevilo_palic=0
nenicelna_dolzina_stopenj=0
pomoc_2=0
pomoc_3=0
random_poteza_palce=0
random_poteza_skatle=0
signal=0
signal_2=0
signal_3=0
signal_4=0
signal_5=0
signal_6=0
skatla_za_zmanjsevanje=0
stevilo_palic_za_brisanje=0
stpalic=0
stskatel=0
tezavnost=0
x=0
xREV=(len(vrednosti_stopenj))+1
y=0
zmagovalec=0
prazne_skatle=[]
skatle=[]
skatle_z_liho_stopnjo=[]
skatle_za_racunanje=[]
stopnje_skatle_za_zmanjsevanje=[]
objavi_izbrisi_svincnik()# OOOOOOOOOOOOO
generiranje_vrednosti_stopenj()
ciklicni_x_11=0
posebnost_1=0
posebnost_2=0
signal_7=0
lovro_1=0
globals().update(locals())    

objavi_start()# OOOOOOOOOOOOO
# start()
t.hideturtle()
screen = turtle.Screen()
t.speed(10)
t.penup()
#t.goto(400,-400)# OOOOOOOOOOOOO #koment
screen.bgpic('backdrop1.png')
screen.update()
time.sleep(2)
screen.bgpic('backdrop8.png')
screen.update()
#t.goto(-200,-80)# OOOOOOOOOOOOO #koment
tezavnost_igre()
#t.goto(400,-400)# OOOOOOOOOOOOO #koment
screen.bgpic('backdrop4.png')
screen.update()
lovro_1=str(input("Napisi p ali pa pritisni enter."))
if lovro_1=="p":
    t.goto(-200,-80)# OOOOOOOOOOOOO
    screen.bgpic('backdrop9.png')
    screen.update()
    print("Dobro preberi navodila.")
    time.sleep(15)
screen.bgpic('backdrop8.png')
screen.update()
#t.goto(400,-400)# OOOOOOOOOOOOO #koment
nastavitve_igre_in_start_2()
risanje_palic()
#print(vrednosti_stopenj)#koment
generacija_stopenjskih_spremenljivk()
if tezavnost==1:
    while not konec==1:
        if konec==0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        if konec==0:
            random_poteza()
            time.sleep(1)
            vse_skatle_prazne()
if tezavnost==2:
    while not konec==1:
        if konec==0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        if konec==0:
            racunalniska_poteza()
            time.sleep(1)
            vse_skatle_prazne()
        if konec==0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        time.sleep(2)
        if konec==0:
            random_poteza()
            time.sleep(1)
            vse_skatle_prazne()
if tezavnost==3:
    while not konec==1:
        if konec==0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        if konec==0:
            racunalniska_poteza()
            time.sleep(1)
            vse_skatle_prazne()
objavi_izbrisi_svincnik()# OOOOOOOOOOOOO
objavi_start()
t.goto(400,-400)# OOOOOOOOOOOOO
if zmagovalec==1:
    if tezavnost==1:
        screen.bgpic('backdrop2.png')
        screen.update()
    if tezavnost==2:
        screen.bgpic('backdrop7.png')
        screen.update()
    if tezavnost==3:
        screen.bgpic('backdrop6.png')
        screen.update()
else:
    screen.bgpic('backdrop3.png')
    screen.update()
    

#Opomnik: (naredi še)
#preden karkoli unicujes naredi backup!!!!!!!!!
#novo verzijo shrani in uporabi kot template
#1. nakoncu igre ko se zamenja ozadje na konco, se palice se vidijo, pa se nebi smele
#2. turtle se sevedno vidi nasredi polja na zacetku
#3. dobro stesteraj vse tri moznosti igre (tezavnosti)
#4. v vseh treh nacinih preizkusi konec igre
#5. DODATNO: ce ostane cas lahko naredis nova ozadja, tako da bodo lepsa in da bpdp ZP res zlate
#6. dodaj sound efekte
#pametno, bi bilo redizajnirati, ker se da veliko lepse narediti celo igrico (tudi bol user friendly (med drugim na delu s "p" in "enter" za razumevanje navodil))
#razmisli o debelinah pisal za vse tri like (zp, sprite1 in 2)
#prilagodi hitrost turtla (sedaj je prehiter, namrec ne vidi se da se palice dejansko narisejo), (dodaj vrstico penup in pendown tako, da se bosta narisala tudi sprita 1 in 2 v eni potezi)
    
#napisati je se potrebno vsebino splstr (ce se ni) - zahvale cot in inf prof, o ZP igri nasplosno, avtorja, okvir in izgled zavihka z igro ZP, prvo stran, kontakt (da promoutava igja (: )

#ideja:
    #multiplejer!!!!!!!!!

    
    
        
        
        
            
            
            
