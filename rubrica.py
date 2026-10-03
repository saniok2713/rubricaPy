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
        for dati_contatto in dati["contatti"]:
            contatto = Contatto(
                dati_contatto["codice"],
                dati_contatto["nome"],
                dati_contatto["cognome"],
                dati_contatto["data_nascita"],
                [],
                dati_contatto["nr_recapiti"],
            )
            for dati_recapito in dati_contatto["recapiti_telefonici"]:
                recapito = Recapito(
                    dati_recapito["numero"],
                    dati_recapito["descrizione"],
                )
                contatto.recapiti_telefonici.append(recapito)
            rubrica.append(contatto)
        return dati["codice"]


rubrica = []
codice = carica_dati()


def nuovo_contatto(codice):
    nome = input("Inserici il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci data nascita: ")
    lista_recapiti = []
    esito_contatto = controlla_contatto(nome, cognome)
    if esito_contatto is None:
        nr_recapiti_da_aggiungere = int(
            input("Quanti recapiti vuoi aggungere? (max 10) ")
        )
        if nr_recapiti_da_aggiungere <= 10:
            for i in range(nr_recapiti_da_aggiungere):
                nr_telefono = input("Inserisci il numero:")
                descrizione = input("Descrizione: ")
                recapito = Recapito(nr_telefono, descrizione)
                lista_recapiti.append(recapito)
        else:
            print("Numero max recapiti superato!")
        contatto = Contatto(
            codice,
            nome,
            cognome,
            data_nascita,
            lista_recapiti,
            nr_recapiti_da_aggiungere,
        )
        rubrica.append(contatto)
    else:
        numero_recapiti_attuale = esito_contatto.nr_recapiti
        numero_recapiti_disponibili = 10 - numero_recapiti_attuale
        print("Il contatto e gia presente nella rubrica!")
        risposta = input("Vuoi aggingere un'altro recapito? (si/no) ")
        if risposta == "no":
            return
        elif risposta == "si":
            print(f"Puoi aggiungere altri {numero_recapiti_disponibili} recapiti!")
            nr_recapiti_da_aggiungere = int(
                input(
                    f"Quanti recapiti vuoi aggiungere? (max {numero_recapiti_disponibili}) "
                )
            )
            if nr_recapiti_da_aggiungere > numero_recapiti_disponibili:
                print("Hai superato il limite disponibile!")
            else:
                for i in range(nr_recapiti_da_aggiungere):
                    nr_telefono = input("Inserisci il numero:")
                    descrizione = input("Descrizione: ")
                    recapito = Recapito(nr_telefono, descrizione)
                    lista_recapiti.append(recapito)
                    esito_contatto.nr_recapiti += 1
            esito_contatto.recapiti_telefonici.extend(lista_recapiti)


def controlla_contatto(nome, cognome):
    for contatto in rubrica:
        if contatto.nome == nome and contatto.cognome == cognome:
            return contatto
    return None


def cerca_numero(nr_telefono):
    for persona in rubrica:
        for numero in persona.recapiti_telefonici:
            if numero.numero == nr_telefono:
                return numero

    return None


def cerca_contatto(cognome):
    lista_contatti = []
    for persona in rubrica:
        if persona.cognome == cognome:
            lista_contatti.append(persona)
    return lista_contatti


def visualizza_rubrica():
    for contatto in rubrica:
        print(
            f"Nome: {contatto.nome} Cognome: {contatto.cognome} Data nascita: {contatto.data_nascita}"
        )
        for recapito in contatto.recapiti_telefonici:
            print(
                f"--------Nr.Telefono: {recapito.numero} Descrizione: {recapito.descrizione}"
            )


def nuovo_recapito(codice):
    for contatto in rubrica:
        if codice == contatto.codice:
            return contatto
    return None


run = True
while run:
    print("------RUBRICA------")
    print("1: Nuovo contatto")
    print("2: Nuovo recapito")
    print("3: Cerca numero")
    print("4: Visualizza rubrica")
    print("0: CHIUDI")

    scelta = int(input("Scelta: "))
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
            codice_contatto = int(input("Inserisci il codice del contatto: "))
            esito_contatto = nuovo_recapito(codice_contatto)
            if esito_contatto == None:
                print("Conatto non trovato!")
            else:
                print(f"Nome: {esito_contatto.nome} Cognome: {esito_contatto.cognome}")
                for recapito in esito_contatto.recapiti_telefonici:
                    print(
                        f"--------Nr.Telefono: {recapito.numero} Descrizione: {recapito.descrizione}"
                    )
                recapito_numero = input("Inserici il numero: ")
                recapito_desc = input("Inserici descrizione: ")
                recapito = Recapito(recapito_numero, recapito_desc)
                esito_contatto.recapiti_telefonici.append(recapito)
                esito_contatto.nr_recapiti += 1
        case 3:
            ##nr_telefono = input("Inserici il numero di telefono: ")
            ##esito_contatto = cerca_numero(nr_telefono)
            ##if esito_contatto == None:
            ##   print("Il numero non e trovato!")
            ##else:
            ##   print(esito_contatto)
            cognome = input("Inserisci il cognome: ")
            contatti_trovati = cerca_contatto(cognome)
            for contatto in contatti_trovati:
                print(f"Nome: {contatto.nome} Cognome: {contatto.cognome}")
                for recapito in contatto.recapiti_telefonici:
                    print(
                        f"--------Nr.Telefono: {recapito.numero} Descrizione: {recapito.descrizione}"
                    )
        case 4:
            visualizza_rubrica()
        case _:
            print("NON VALIO")
