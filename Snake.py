
class Snake:
    def __init__(self):
        self.kierunek = Kierunek.PRAWO
        self.dlugosc = 1
        self.cialo = [punkt(1, 1)]
        self.koniec_gry = False

    def ruch(self):
        if self.kierunek == Kierunek.GORA:
            nowa_glowa = punkt(self.cialo[0].x, self.cialo[0].y - 1)
        elif self.kierunek == Kierunek.DOL:
            nowa_glowa = punkt(self.cialo[0].x, self.cialo[0].y + 1)
        elif self.kierunek == Kierunek.LEWO:
            nowa_glowa = punkt(self.cialo[0].x - 1, self.cialo[0].y)
        elif self.kierunek == Kierunek.PRAWO:
            nowa_glowa = punkt(self.cialo[0].x + 1, self.cialo[0].y)
        if nowa_glowa in self.cialo or nowa_glowa.x < 0 or nowa_glowa.x >= Plansza.szerokosc or nowa_glowa.y < 0 or nowa_glowa.y >= Plansza.wysokosc:
            self.koniec_gry = True
        else:
            self.cialo.insert(0, nowa_glowa)
            if len(self.cialo) > self.dlugosc:
                self.cialo.pop()

    def rysuj(self, plansza):
        for segment in self.cialo:
            pg.draw.rect(plansza, (0, 255, 0),
                         pg.Rect(segment.x * plansza.rozmiar, segment.y * plansza.rozmiar, plansza.rozmiar,
                                 plansza.rozmiar))

    def kolizja_jedzenia(self, jedzenie):
        if self.cialo[0] == jedzenie.pozycja:
            self.dlugosc += 1
            jedzenie.losuj_pozycje()
