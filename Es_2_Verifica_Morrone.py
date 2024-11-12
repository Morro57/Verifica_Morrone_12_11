tupla_produzione_agricola = (
    ("Toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo",("grano",1500)),
        ("marzo",("mais",500))
       
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo",("grano",1350)),
        ("marzo",("mais",900))
       
    ]),
   
    ("Liguria", [
        ("gennaio", ("grano", 1400)),
        ("gennaio", ("mais", 950)),
        ("febbraio", ("grano", 1050)),
        ("febbraio", ("mais", 980)),
        ("marzo",("grano",1000)),
        ("marzo",("mais",700))
    ]),
)

def media_produzione(regioneInp,colturaInput):
    mediaProd=0
    cont=0
    for regione,rilevazioni in tupla_produzione_agricola:
        if(regioneInp==regione):
            for mese,raccolto in rilevazioni:
                coltura,prodMax=raccolto
                if(colturaInput==coltura):
                    mediaProd+=prodMax
                    cont+=1
                 
        
    mediaProd/=cont
    print(f"La media di produzione mensile di {colturaInput} è di: {mediaProd:.2f}")

def max_produzione(meseInp,colturaInput):
    max=0
    for regione,rilevazioni in tupla_produzione_agricola:
        for mese,raccolto in rilevazioni:
            coltura,prodMax=raccolto
            if(meseInp==mese and colturaInput==coltura):
                if(max<prodMax):
                    max=prodMax

    print(f"La produzione massima del mese di {meseInp} di {colturaInput} è di: {max}")

def mese_max_produzione(colturaInput):
    max=0
    meseMax=""
    for regione,rilevazioni in tupla_produzione_agricola:
        for mese,raccolto in rilevazioni:
            coltura,prodMax=raccolto
            if(colturaInput==coltura):
                if(max<prodMax):
                    max=prodMax
                    meseMax=mese
    print(f"Il mese in cui si è prodotto maggior {colturaInput} è il mese di {meseMax}.")
def analizza_produzione_agricola(regioneInp,colturaInput):
    for regione,rilevazioni in tupla_produzione_agricola:
        for mese,raccolto in rilevazioni:
            if(regioneInp==regione):
                coltura,prodMax=raccolto
                if(colturaInput==coltura):
                    media_produzione(regioneInp,colturaInput)
                    max_produzione("febbraio",colturaInput)
                    mese_max_produzione(colturaInput)
    tupla=(media_produzione,(max_produzione,mese_max_produzione))
    print(f"Risultato: {tupla}")
                

analizza_produzione_agricola("Lombardia","grano") 

