import sys, os

APP_NAME: str = "Gra paragrafowa"
APP_VERSION: str = "0.0.0"
DEBUG: bool = "--debug" in sys.argv
INFO: bool = "--quite" in sys.argv

def debug_print(tekst: str) -> None:
    if DEBUG:
        input( f"DEBUG: {tekst}. Naciśnij ENTER aby kontynuować !!!")
    return None

def info_print(tekst: str) -> None:
    if DEBUG or QUITE:
        input(f"INFO: {tekst}. Naciśnij ENTER aby kontynuować !!!")
    return None

def program() -> None:
    return None

if __name__ == "__main__":
    if "--help" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        To jest gra paragrafowa, której akcja dzieje się w niedalekiej przyszłości, w świecie cyberpunkowym.
        
        Dostępne flagi:
            --help - pomoc,
            --version - wersja programu,
            --history - historia wersji gry,
            --info - uruchomienie gry w trybie z komentarzami dla gracza,
            --debug - uruchomienie gry w trybie debug.
""")
        sys.exit()
    if "--version" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        Program {APP_NAME}, wersja: {APP_VERSION}
""")
        sys.exit()
    if "--history" in sys.argv:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        Historia wersji:
        
        0.0.0
        Rozpoczęcie pracy.
""")
        sys.exit()
    if "--info" in sys.argv:
        DEBUG = False
    debug_print("Program wita Michasia !!!")
    info_print("Gra rozpoczyna pracę")

    program()

    info_print("Koniec gry. DO zobaczenia !!!")
    sys.exit()