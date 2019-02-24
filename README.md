# Simplex-Algorithm-Furniture-Sale
Użycie biblioteki Pulp do rozwiązania problemu liniowego

Zużycie surowca na produkcję 1 sztuki wyrobu
<table>
<tr>
 <td>
Surowce	      
<td> A	 
<td> B
<tr>
<td>
Płyty wiórowe
<td>15
<td>8
<tr>
<td>Płyty MDF
<td>25
<td>5
<tr>
<td>Zużyta energia
<td>1	  
<td>0,6
<tr>
<td>Cena	          
<td>500
<td>180
</table>
Zmienne decyzyjne:

x1 – planowana ilość produkcji mebla rodzaju A

x2 - planowana ilość produkcji mebla rodzaju B


<h4>Funkcja celu</h4>

Celem jest zmaksymalizowanie zysków sprzedaży mebli.

F(x_1,x_2)=500x_1+180x_2 -> max


<h4>Warunki ograniczające </h4>

15x_1+8x_2<=3240

25x_1+5x_2<=4300

1x_1+0,6x_2<=200

x_1,x_2>=0

x_1,x_2 \in C
</ul>
