# Pong
Prosta gra typu Pong napisana w Pythonie z użyciem biblioteki Pygame.

## Gameplay
Gra dla dwóch graczy:
- Gracz lewy: `W` / `S`
- Gracz prawy: `↑` / `↓`

## Mechaniki
- Ruch paletek (klawiatura)
- Ruch piłki z prędkością X/Y
- Kolizje oparte o `pygame.Rect`
- Odbicia od paletek i ścian
- System punktów
- Prosty system stanów gry:
  - menu
  - gra
  - ekran wygranej

## Technologie
- Python
- Pygame

## Struktura projektu
- main.py główna pętla gry, logika stanów
- objects.py klasy: Ball, Padle