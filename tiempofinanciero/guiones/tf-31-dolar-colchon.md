# tf-31 Cien dólares en el colchón durante 20 años
Tipo: la cuenta. Duración objetivo: 60 s. Estado: revisado OK (2026-11-14).
Cálculo: inflación de EE. UU. con el CPI-U del BLS (todos los rubros, promedio de ciudades, sin desestacionalizar, base 1982-84 = 100), de octubre de 2006 (201,8) a octubre de 2026 (337,511; último dato publicado, comunicado del 2026-11-10): 20 años. Comparación con Yahoo Finance, SPY con dividendos reinvertidos (adjclose), del 2006-11-14 al 2026-11-13. Sin comisiones ni impuestos. Script: `calculos/tf-31.py`.
- Inflación acumulada en dólares: 67,3 % (2,60 % anual).
- US$ 100 de 2006 compran hoy lo que entonces se compraba con ~US$ 59,8 (pérdida de poder de compra: 40,2 %). Para comprar lo mismo hacen falta ~US$ 167.
- Peor tramo: octubre de 2020 a octubre de 2022, +14,4 % en dos años (6,2 % y 7,7 %).
- US$ 100 en SPY en el mismo tramo: ~US$ 779 nominales, ~US$ 466 en dólares de 2006. Peor caída del SPY: -55,2 % (2007-10-09 a 2009-03-09).
- El dato de octubre de 2025 no fue publicado por el BLS (cierre del gobierno de EE. UU.); en la serie anual del gráfico se interpola entre septiembre y noviembre de 2025. No afecta el resultado de punta a punta.

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Si guardaste cien dólares en el colchón hace veinte años, hoy compran lo que antes comprabas con sesenta. | US$ 100 → COMPRAN COMO US$ 60 | Pixabay: hundred dollar bill close up |
| 2 | El mito: el dólar no pierde valor. Pierde, más despacio que el peso. Hagamos la cuenta. | EL DÓLAR TAMBIÉN PIERDE | Gráfico: número grande "-40 %" con subtítulo "poder de compra del dólar, 2006-2026" |
| 3 | Según el índice de precios de Estados Unidos, de octubre de 2006 a octubre de 2026 todo subió sesenta y siete por ciento. | +67 % (2,6 % POR AÑO) | Gráfico: barras "Precios oct-2006: 100" contra "Precios oct-2026: 167" |
| 4 | Pero acumulado, tu billete de cien perdió cuarenta por ciento de su poder de compra. | -40 % | Gráfico: línea poder de compra de US$ 100, valor cada octubre: 2006: 100, 2008: 93,2, 2010: 92,3, 2012: 87,2, 2014: 85,0, 2016: 83,5, 2018: 79,8, 2020: 77,5, 2021: 73,0, 2022: 67,7, 2024: 63,9, 2026: 59,8 |
| 5 | Para comprar lo mismo que en 2006, hoy necesitás ciento sesenta y siete dólares. | HOY HACEN FALTA US$ 167 | Pixabay: grocery bags receipt kitchen table |
| 6 | Y no fue parejo. Entre 2020 y 2022, los precios subieron catorce por ciento en dos años. | +14 % EN 2 AÑOS | Gráfico: barras inflación anual de octubre a octubre "2021: 6,2 % / 2022: 7,7 %" contra promedio 2,6 % |
| 7 | ¿Y si esos cien iban al SPY, con dividendos reinvertidos? Hoy serían unos setecientos ochenta dólares. | SPY: US$ 780 | Gráfico: barras "Colchón: US$ 100 (compran como 60)" contra "SPY: US$ 779 (compran como 466 de 2006)" |
| 8 | Pero ojo: el colchón nunca mostró un número en rojo. El SPY cayó cincuenta y cinco por ciento en la crisis de 2008. | SPY: -55 % | Pixabay: stock market crash red screen |
| 9 | Y en Argentina, el dólar guardado te cubrió de algo mucho peor: la inflación en pesos. | CONTRA EL PESO, SIRVIÓ | Pixabay: buenos aires city street |
| 10 | Ya sabés que el colchón también cuesta, aunque no se vea. Y que lo que pasó no garantiza lo que viene. | EL COLCHÓN TAMBIÉN CUESTA | Gráfico: remate "US$ 100 en 2006 → compran como US$ 60 en 2026" |
| 11 | ¿Qué te da más miedo: ver tu inversión caer cuarenta por ciento, o perderlo sin darte cuenta? Comentá 1 o 2. | VERLA CAER / PERDER SIN VERLO | Placa de encuesta + cierre |

## Pregunta de cierre (va dibujada en el video con 1 y 2, y al final del texto)
¿Qué te da más miedo? / 1: Verla caer 40 % / 2: Perder 40 % sin verlo

## Caption
US$ 100 guardados en el colchón en 2006 siguen siendo US$ 100. Pero entre octubre de 2006 y octubre de 2026 los precios en Estados Unidos subieron 67 % (2,6 % anual), así que hoy compran lo que antes comprabas con unos US$ 60. Para comprar lo mismo que entonces hacen falta US$ 167. Esos mismos US$ 100 en el SPY, con dividendos reinvertidos, serían unos US$ 779, pero con una caída de 55 % en el medio que el colchón no tuvo. Y contra la inflación en pesos, el dólar guardado sí cubrió.
Fuente de inflación: CPI-U del BLS (oct-2006: 201,8; oct-2026: 337,511). SPY: Yahoo Finance del 14/11/2006 al 13/11/2026, sin comisiones ni impuestos. Cuenta en dólares.
¿Qué te da más miedo? Comentá 1 (Verla caer 40 %) o 2 (Perder 40 % sin verlo) 👇
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#dolar #dolarcolchon #inflacion #ahorro #inversiones #finanzas #argentina

## A revisar (agente financiero)
- CPI tomado de la tabla histórica y del comunicado del BLS vía búsqueda web (FRED y la API del BLS no responden desde este entorno): confirmar 201,8 (oct-2006) y 337,511 (oct-2026).
- Octubre de 2025 interpolado (324,46) entre sep-2025 (324,800) y nov-2025 (324,122) solo para la serie del gráfico.
- El CPI llega a octubre y el SPY al 13 de noviembre: desfase de dos semanas entre las dos series.
- Fila 9 (el dólar cubrió de la inflación en pesos) va sin cifra. Si se quiere número, falta fuente de IPC argentino de 20 años (INDEC tiene el tramo 2007-2015 cuestionado).

## Revisión financiera (2026-11-14)
CPI-U de oct-2026 = 337,511, confirmado en el comunicado de BLS del 2026-11-10. +67,3% y −40,2% de poder de compra están bien. Ojo: BLS no publica la variación de 12 meses de oct-2026 porque no relevó oct-2025, así que el gráfico no tiene que mostrar 'inflación 2026 interanual'.
