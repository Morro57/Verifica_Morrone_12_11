tupla_competizioni = (
    ("ChefA", "Piatto1", 8.5, 5),
    ("ChefB", "Piatto2", 7.2, 4),
    ("ChefC", "Piatto3", 9.0, 6),
    ("ChefA", "Piatto4", 7.8, 5),
    ("ChefB", "Piatto5", 8.1, 4),
)

def media_punteggio_competizione(tupla_compmetizioni):
    media = 0
    cont = 0
    for chef,piatto,puntiPiatto,numGiudici in tupla_competizioni:
        media+=puntiPiatto
        cont += 1
    media/=cont
    print(f"La media generale di tutte le competizioni e di: {media:.2f}")

def media_punteggio_chef(tupla_competizioni, chefInp):
    mediaChef = 0
    cont = 0
    for chef,piatto,puntiPiatto,numGiudici in tupla_competizioni:
        if(chefInp==chef):
            mediaChef+=puntiPiatto
            cont+=1
    mediaChef/=cont
    print(f"La media del punteggio dello {chefInp} e di {mediaChef:.2f}.")

def competizione_con_piu_giudici(tupla_competizioni):
    giudiciMax=0
    chefMax=""
    piattoMax=""
    puntiMax=0
    
    #lista_Max=[]

    for chef,piatto,puntiPiatto,numGiudici in tupla_competizioni:
        if(giudiciMax<numGiudici):
            giudiciMax=numGiudici
            chefMax=chef
            piattoMax=piatto
            puntiMax=puntiPiatto
            """"
            lista_Max.clear()
            lista_Max.append(tupla_Max)
        elif(giudiciMax==numGiudici):
            lista_Max.append(tupla_Max)
            """
    tupla_Max=(chefMax,piattoMax,puntiMax,giudiciMax)
    print (f"Numero di giudici maggiore: {tupla_Max}")   

def competizione_con_meno_giudici(tupla_competizioni):
    giudiciMin=100
    chefMin=""
    piattoMin=""
    puntiMin=100
    #lista_Min=[]

    for chef,piatto,puntiPiatto,numGiudici in tupla_competizioni:
        if(giudiciMin>numGiudici):
            giudiciMin=numGiudici
            chefMin=chef
            piattoMin=piatto
            puntiMin=puntiPiatto
            """"
            lista_Min.clear()
            lista_Min.append(tupla_Min)
        elif(giudiciMin==numGiudici):
            lista_Min.append(tupla_Min)
            """
    tupla_Min=(chefMin,piattoMin,puntiMin,giudiciMin)
    print (f"Numero di giudici minore: {tupla_Min}")
     
media_punteggio_competizione(tupla_competizioni)
media_punteggio_chef(tupla_competizioni, "ChefB")
competizione_con_piu_giudici(tupla_competizioni)
competizione_con_meno_giudici(tupla_competizioni)