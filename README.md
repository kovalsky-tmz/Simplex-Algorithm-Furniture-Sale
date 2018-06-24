# Simplex-Algorithm-Furniture-Sale
Using Pulp Library for solve a linear problem

Zużycie surowca na produkcję 1 sztuki wyrobu
Surowce	        A	  B
Płyty wiórowe	  15	8
Płyty MDF	      25	5
Zużyta energia	1	  0,6
Cena	          500	180

Zmienne decyzyjne:
x1 – planowana ilość produkcji mebla rodzaju A
x2 - planowana ilość produkcji mebla rodzaju B

Funkcja celu 
Celem jest zmaksymalizowanie zysków sprzedaży zabawek.
F(x_1,x_2)=500x_1+180x_2 -> max

Warunki ograniczające 
15x_1+8x_2<=3240
25x_1+5x_2<=4300
1x_1+0,6x_2<=200
x_1,x_2>=0
x_1,x_2 \in C
