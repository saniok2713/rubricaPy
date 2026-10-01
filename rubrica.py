class Contatto:
    def __init__(
        self, codice, nome, cognome, data_nascita, recapiti_telefonici, nr_recapiti
    ):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.recapiti_telefonici = recapiti_telefonici
        self.nr_recapiti = nr_recapiti


class Recapito:
    def __init__(self, numero, descrizione):
        self.numero = numero
        self.descrizione = descrizione


codice = 1
rubrica = []


def nuovo_contatto(codice):
    nome = input("Inserici il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci data nascita: ")
    nr_recapiti_da_aggiungere = int(input("Quanti recapiti vuoi aggungere? (max 10)"))
    if nr_recapiti_da_aggiungere <= 10:
        lista_recapiti = []
        for i in range(nr_recapiti_da_aggiungere):
            nr_telefono = input("Inserisci il numero:")
            descrizione = input("Descrizione: ")
            recapito = Recapito(nr_telefono, descrizione)
            lista_recapiti.append(recapito)
    else:
        print("Numero max recapiti superato!")
    contatto = Contatto(
        codice, nome, cognome, data_nascita, lista_recapiti, nr_recapiti_da_aggiungere
    )
    rubrica.append(contatto)


def cerca_numero(nr_telefono):
    for persona in rubrica:
        for numero in persona.recapiti_telefonici:
            if numero.numero == nr_telefono:
                return numero

    return None


def cerca_contatto(cognome):
    for persona in rubrica:
        if persona.cognome == cognome:
            print(f"Cognome: {persona.cognome}")

run = True
while run:
    print("------RUBRICA------")
    print("1: Nuovo contatto")
    print("2: Nuovo recapito")
    print("3: Cerca numero")
    print("4: Visualizza rubrica")
    print("0: CHIUDI")

    scelta = int(input("Scelta:"))
    match scelta:
        case 0:
            run = False
            print("------A PRESTO------")
        case 1:
            nuovo_contatto(codice)
            codice += 1
        case 2:
            print("2")
        case 3:
            ##nr_telefono = input("Inserici il numero di telefono: ")
            ##esito_contatto = cerca_numero(nr_telefono)
            ##if esito_contatto == None:
            ##   print("Il numero non e trovato!")
            ##else:
            ##   print(esito_contatto)
            cognome = input("Inserisci il cognome: ")
            cerca_contatto(cognome)
        case 4:
            print("4")
        case _:
            print("NON VALIO")
