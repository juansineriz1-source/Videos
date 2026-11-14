# tf-27 Perderse los diez mejores días de la bolsa
Tipo: la cuenta. Duración objetivo: 60 s. Estado: borrador, espera revisión financiera (2026-11-14).
Cálculo: Yahoo Finance, SPY diario con dividendos reinvertidos (adjclose), US$ 10.000 invertidos al cierre del 2006-11-14 y valuados al cierre del 2026-11-13 (20 años, 5.030 ruedas). "Perderse un día" = ese día el rendimiento es cero (estabas afuera). Sin comisiones ni impuestos. Script: `calculos/tf-27.py`.
- Todos los días adentro: ~US$ 77.900 (x7,79; 10,8 % anual).
- Sin los 10 mejores días: ~US$ 33.800 (-57 %). Sin los 20 mejores: ~US$ 20.300. Sin los 40 mejores: ~US$ 9.400 (menos que lo invertido).
- Los 10 mejores días: 2008-10-13 (+14,5 %), 2008-10-28 (+11,7 %), 2025-04-09 (+10,5 %), 2020-03-24 (+9,1 %), 2020-03-13 (+8,6 %), 2009-03-23 (+7,2 %), 2008-11-24 (+6,9 %), 2020-04-06 (+6,7 %), 2008-11-13 (+6,2 %), 2008-10-20 (+6,0 %). Cinco en 2008, uno en 2009, tres en 2020, uno en 2025.
- 7 de los 10 mejores cayeron a 10 ruedas o menos de uno de los 10 peores días.
- La otra cara: sin los 10 PEORES días serían ~US$ 183.800. Peor caída del período: -55,2 % (2007-10-09 a 2009-03-09).

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Si en veinte años te perdiste solo los diez mejores días de la bolsa, te quedaste con menos de la mitad. | 10 DÍAS = -57 % | Gráfico: número grande "-57 %" con subtítulo "por perderte 10 días en 20 años" |
| 2 | Hagamos la cuenta: son diez días entre más de cinco mil ruedas. | 10 DE 5.030 | Pixabay: calendar pages flipping |
| 3 | Diez mil dólares en el SPY en noviembre de 2006, con dividendos reinvertidos. Hoy serían unos setenta y ocho mil. | US$ 78.000 | Gráfico: línea US$ 10.000 en SPY, valor anual en noviembre: 2006: 10.000, 2008: 6.454, 2010: 9.370, 2012: 11.038, 2014: 17.278, 2016: 19.096, 2018: 24.748, 2020: 34.097, 2022: 38.729, 2024: 59.874, 2026: 77.879 |
| 4 | Ahora sacá los diez mejores días. Quedan unos treinta y cuatro mil. Cincuenta y siete por ciento menos. | US$ 34.000 | Gráfico: línea "sin los 10 mejores" debajo de la anterior, valor anual: 2006: 10.000, 2008: 4.481, 2010: 5.676, 2012: 6.687, 2014: 10.466, 2016: 11.567, 2018: 14.991, 2020: 16.349, 2022: 18.570, 2024: 28.709, 2026: 33.793 |
| 5 | Sin los cuarenta mejores quedan nueve mil cuatrocientos: menos de lo que pusiste. | SIN 40 DÍAS: PERDÉS | Gráfico: barras "Todos los días: 77.900 / Sin 10: 33.800 / Sin 20: 20.300 / Sin 40: 9.400" |
| 6 | ¿Cuándo fueron? Cinco en 2008, uno en 2009, tres en 2020 y uno en 2025. | 2008 · 2009 · 2020 · 2025 | Gráfico: lista de los 10 mejores días con fecha y suba (13/10/2008 +14,5 % ... 20/10/2008 +6,0 %) |
| 7 | Todos en plena crisis. Siete de los diez, a menos de dos semanas de uno de los peores. | PEGADOS A LOS PEORES | Pixabay: worried trader looking at screen |
| 8 | O sea: el que sale por miedo suele perderse también el rebote. | SE PIERDE EL REBOTE | Pixabay: person leaving through door |
| 9 | La contra es real: para cobrar esos días hubo que aguantar una caída de cincuenta y cinco por ciento. | -55 % | Gráfico: línea con zoom 2007-2009, de 11.417 (9/10/2007) a 5.116 (9/3/2009) |
| 10 | Esquivando los diez peores tendrías mucho más. Pero nadie sabe cuáles son hasta que pasaron. | NADIE LOS ADIVINA | Pixabay: dice rolling on table |
| 11 | Ya sabés por qué entrar y salir puede costar caro. Y que lo que pasó no garantiza lo que viene. | 10 DÍAS, MEDIA GANANCIA | Gráfico: remate "Siempre adentro: US$ 77.900 / Sin los 10 mejores días: US$ 33.800" |
| 12 | Cuando la bolsa se derrumba, ¿qué te cuesta más: quedarte quieto o volver a entrar? Votá abajo. | QUEDARME QUIETO / VOLVER A ENTRAR | Placa de encuesta + cierre |

## Encuesta para poner
En una caída, ¿qué te cuesta más? / Quedarme quieto / Volver a entrar

## Caption
US$ 10.000 en el SPY del 14/11/2006 al 13/11/2026: unos US$ 77.900. Si te perdías solo los 10 mejores días (de más de 5.000 ruedas): unos US$ 33.800, un 57 % menos. Sin los 40 mejores, terminabas con menos de lo que pusiste. Esos días fueron en 2008, 2009, 2020 y 2025, casi todos pegados a los peores. La otra cara: esquivando los 10 peores días tendrías mucho más, pero nadie sabe de antemano cuáles son. Y quedarse adentro fue aguantar una caída de 55 %.
Cálculo con datos de Yahoo Finance al 13/11/2026, rendimientos diarios con dividendos reinvertidos, sin comisiones ni impuestos. Cuenta en dólares.
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#spy #bolsa #inversiones #largoplazo #markettiming #finanzas #argentina

## A revisar (agente financiero)
- El ejercicio "perderse los mejores días" es un clásico discutido: nadie se pierde justo esos diez. Por eso se muestra también la otra cara (fila 10). ¿Alcanza o sumamos el número (US$ 183.800 sin los 10 peores) en pantalla?
- "A menos de dos semanas" = 10 ruedas o menos (7 de 10); a 5 ruedas o menos son 5 de 10.
