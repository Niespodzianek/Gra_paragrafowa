import sys, os
from paragrafy import lista_paragrafow

APP_NAME: str = "Gra paragrafowa"
APP_VERSION: str = "0.0.1"
DEBUG: bool = "--debug" in sys.argv
INFO: bool = "--info" in sys.argv


def debug_print(tekst: str) -> None:
    if DEBUG:
        input(f"DEBUG: {tekst}. Naciśnij ENTER aby kontynuować !!!")
    return None


def info_print(tekst: str) -> None:
    if DEBUG or INFO:
        input(f"INFO: {tekst}. Naciśnij ENTER aby kontynuować !!!")
    return None


def tura_gry(
    status_gry: bool, obecny_paragraf: dict[str, str]
) -> tuple[bool, dict[str, str]]:
    nastepna_lokacja: dict[str, str]
    petla_tury: bool = True
    wybor: str
    while petla_tury:
        os.system("cls" if os.name == "nt" else "clear")
        info_print("Za chwilę wyświetlisz opis paragrafu, w którym się znajdujesz")
        print(f"{obecny_paragraf['opis']}")
        info_print(
            "Za chwilę wyświetlisz dostępne kierunki, do których się możesz poruszyć"
        )
        print(f"Możliwe kierunki ruchu z {obecny_paragraf['nazwa']}:")
        for indeks, lokacja in enumerate(obecny_paragraf["destynacje"]):
            print(lokacja)
        wybor = input("Wpisz numer wybranego paragrafu: ")
        if wybor in obecny_paragraf["destynacje"]:
            nastepny_paragraf = lista_paragrafow[int(wybor)]
            petla_tury = False
        elif wybor == "0":
            return False, lista_paragrafow[0]
        else:
            info_print("Dokonano nieprawidłowego wyboru. Wybierz ponownie !!!")
    return status_gry, nastepny_paragraf


def program() -> None:
    debug_print("Rozpoczynam grać w grę. Uruchamiam pętle gry")
    paragraf: dict[str, str]
    status: bool = True
    program_pracuje: bool = True
    paragraf = lista_paragrafow[1]
    while program_pracuje:
        os.system("cls" if os.name == "nt" else "clear")
        debug_print("Rozpoczęcie tury gry")
        debug_print(f"Pełny słownik lokacji, w której jesteś: {paragraf}")
        status, paragraf = tura_gry(status_gry=status, obecny_paragraf=paragraf)
        debug_print("Koniec tury gry")
        program_pracuje = status
    return None


if __name__ == "__main__":
    if "--help" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""
        To jest gra paragrafowa, której akcja dzieje się w niedalekiej przyszłości, w świecie cyberpunkowym.
        
        TIP !!!
        Żeby zakończyć grę wystarczy wpisać 0 zamiast numeru paragrafu, w momencie podejmowania decyzji.
        
        Dostępne flagi:
            --help - pomoc,
            --version - wersja programu,
            --history - historia wersji gry,
            --info - uruchomienie gry w trybie z komentarzami ułatwiającymi grę,
            --debug - uruchomienie gry w trybie debug.
"""
        )
        sys.exit()
    if "--version" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""
        Program {APP_NAME}, wersja: {APP_VERSION}
"""
        )
        sys.exit()
    if "--history" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""
        Historia wersji:
        
        0.0.1
        Działający silnik gry w wersji tekstowej z flagami CLI.
        
        0.0.0
        Rozpoczęcie pracy.
"""
        )
        sys.exit()
    os.system("cls" if os.name == "nt" else "clear")
    debug_print("Program wita Michasia !!!")
    info_print("Gra rozpoczyna pracę")
    os.system("cls" if os.name == "nt" else "clear")
    program()
    os.system("cls" if os.name == "nt" else "clear")
    info_print("Koniec gry. Do zobaczenia !!!")
    sys.exit()
