import random


def dadoLancio():
    min=1
    max=6
    dado = random.randint(min, max)
    return dado

def EventOp():
    operazioneJ = ""
    feedback1 = input("Evento J o Non Assoociato giocabile ? (y/n) ")
    if feedback1 == "y":
       feedback2 = input("Recluta o colloca cellule ? (y/n) ")
       if feedback2 == "y":
          feedback3 = input("Indicatore contiene cellule ? (y/n) ")
          if feedback3 == "n":
             operazioneJ = "RADICALIZZAZIONE"
             return operazioneJ
    if feedback1 == "n":
       feedback4 = input("Evento U giocabile ? (y/n) ")
       if feedback4 == "y":
          operazioneJ = "COMPLOTTO"
          return operazioneJ
       if feedback4 == "n":
          feedback5 = input("Successo di J Maggiore possibile ? (y/n) ")
          if feedback5 == "y":
             operazioneJ = "J MAGGIORE"
             return operazioneJ
          if feedback5 == "n":
             feedback6 = input("J possibile in paese Forte/Equo ? (y/n) ")
             if feedback6 == "y":
                operazioneJ = "J MINORE"
                return operazioneJ
             if feedback6 == "n":
                feedback7 = input("Cellule disponibili ? (y/n) ")
                if feedback7 == "y":
                   operazioneJ = "RECLUTAMENTO"
                   return operazioneJ
                if feedback7 == "n":
                   operazioneJ = "VIAGGIARE"
                   return operazioneJ

    if (feedback2 =="n" or feedback3 =="y"):
       print("GIOCA EVENTO")
       feedback8 = input("Evento non associato ? (y/n) ")
       if feedback8 =="n":
           print("FINE")
           return operazioneJ
       if feedback8 =="y":
          feedback5 = input("Successo di J Maggiore possibile ? (y/n) ")
          if feedback5 == "y":
             operazioneJ = "J MAGGIORE"
          if feedback5 == "n":
             feedback6 = input("J possibile in paese Forte/Equo ? (y/n) ")
             if feedback6 == "y":
                operazioneJ = "J MINORE"
             if feedback6 == "n":
                feedback7 = input("Cellule disponibili ? (y/n) ")
                if feedback7 == "y":
                   operazioneJ = "RECLUTAMENTO"
                if feedback7 == "n":
                   operazioneJ = "VIAGGIARE"

    return operazioneJ


def PaeseCasuale():
    dado1 = dadoLancio()
    dado2 = dadoLancio()
    dado3 = dadoLancio()
    somma3 = dado1 + dado2 + dado3
    print("Somma di 3 dadi: ", somma3)

    dadoNero = dadoLancio()
    dadoMarrone = dadoLancio()
    Schengen = dadoLancio()
    print("Globale: Nero  ",dadoNero," Marrone ",dadoMarrone,"--- Schengen: ",Schengen)

def main():
    menu = 1
    while menu != 9:
        print("")
        print("MENU :")
        print("  0 - Scenario")
        print("  1 - Eventi o Operazioni")
        print("  2 - Dove ?")
        print("  3 - Paese Casuale")
        print("  4 - Nuovo Turno")
        print("  5 - Stato MOndo")
        print("  9 - Esci")
        menu = input("Scelta : ")
        menu = int(menu)
        print("")

        if menu== 0:
           prestigio = float(input("Prestigio: "))
           GGAT_USA = float(input("GGTA USA - 1 Rigido / 2 Moderato :"))
           GGAT_MONDO = float(input("GGTA MONDO:"))
           finanziamenti = float(input("Finanziamenti: "))
           risorse_forti = float(input("Risorse Forti: "))
           risorse_i = float(input("Risorse I: "))
        if menu== 4:
           nuovo_prestigio = float(input("Prestigio: "))
           prestigio = prestigio + nuovo_prestigio
           nuovo_GGAT_USA = float(input("GGTA USA - 1 Rigido / 2 Moderato :"))
           GGAT_USA = GGAT_USA + nuovo_GGAT_USA
           nuovo_GGAT_MONDO = float(input("GGTA MONDO:"))
           GGAT_MONDO = GGAT_MONDO + nuovo_GGAT_MONDO 
           nuovo_finanziamenti = float(input("Finanziamenti: "))
           finanziamenti = finanziamenti + nuovo_finanziamenti
           nuovo_risorse_forti = float(input("Risorse Forti: "))
           risorse_forti = risorse_forti + nuovo_risorse_forti 
           nuovo_risorse_i = float(input("Risorse I: "))
           risorse_i = risorse_i + nuovo_risorse_i
        if menu== 5:
           print("Prestigio: ",prestigio)
           print("GGTA USA: ",GGAT_USA )
           print("GGAT_MONDO: ",GGAT_MONDO)
           print("Finanziamenti; ",finanziamenti)
           print("Risorse Forti: ",risorse_forti)
           print("Risorse_i: ",risorse_i)

        if menu == 1:
           risultato = EventOp()
           print(risultato)
        if menu == 3:
           PaeseCasuale()
        if menu == 9:
           break
main()

