import json
import os


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


FILE_DATI = "rubrica.json"


def salva_dati(codice):
    dati = {
        "codice": codice,
        "contatti": [],
    }
    for contatto in rubrica:
        dati_contatto = {
            "codice": contatto.codice,
            "nome": contatto.nome,
            "cognome": contatto.cognome,
            "data_nascita": contatto.data_nascita,
            "recapiti_telefonici": [],
            "nr_recapiti": contatto.nr_recapiti,
        }
        for recapito in contatto.recapiti_telefonici:
            dati_recapito = {
                "numero": recapito.numero,
                "descrizione": recapito.descrizione,
            }
            dati_contatto["recapiti_telefonici"].append(dati_recapito)

        dati["contatti"].append(dati_contatto)

    with open(FILE_DATI, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)


def carica_dati():
    if not os.path.exists(FILE_DATI):
        return 1
    with open(FILE_DATI, "r", encoding="utf-8") as f:
        try:
            dati = json.load(f)
        except json.JSONDecodeError:
            return 1
        for contatto in dati["contatti"]:
            lista_recapiti = []

            for recapito in contatto["recapiti_telefonici"]:
                r = Recapito(
                    recapito["numero"],
                    recapito["descrizione"],
                )
                lista_recapiti.append(r)

            contatto = Contatto(
                contatto["codice"],
                contatto["nome"],
                contatto["cognome"],
                contatto["data_nascita"],
                lista_recapiti,
                contatto["nr_recapiti"],
            )
            rubrica.append(contatto)
        return dati["codice"]


rubrica = []
codice = carica_dati()


def nuovo_contatto(codice):
    nome = input("Inserici il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci data nascita: ")
    nr_recapiti_da_aggiungere = int(input("Quanti recapiti vuoi aggungere? (max 10) "))
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


def visualizza_rubrica():
    for contatto in rubrica:
        print(
            f"Nome: {contatto.nome} Cognome: {contatto.cognome} Data nascita: {contatto.data_nascita}"
        )
        for recapito in contatto.recapiti_telefonici:
            print(
                f"--------Nr.Telefono: {recapito.numero} Descrizione: {recapito.descrizione}"
            )


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
            salva_dati(codice)
            print("------A PRESTO------")
        case 1:
            nuovo_contatto(codice)
            codice += 1
            salva_dati(codice)
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
            visualizza_rubrica()
        case _:
            print("NON VALIO")
