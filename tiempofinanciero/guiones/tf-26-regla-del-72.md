# tf-26 La regla del 72
Tipo: la cuenta. Duración objetivo: 60 s. Estado: borrador, espera revisión financiera (2026-11-14).
Cálculo: regla del 72 (años para duplicar ≈ 72 / tasa anual en %). Contraste con Yahoo Finance, SPY diario con dividendos reinvertidos (adjclose), del 1996-11-14 al 2026-11-13 (30 años). Inflación de EE. UU.: CPI-U del BLS, octubre de 2006 (201,8) a octubre de 2026 (337,511). Sin comisiones ni impuestos. Script: `calculos/tf-26.py`.
- Regla contra cuenta exacta: 6 % → 12,0 años (exacto 11,9); 10 % → 7,2 (exacto 7,3). La regla es una aproximación; se aleja con tasas muy altas.
- SPY 30 años: x17,05, o sea 9,92 % anual. 72 / 9,92 = 7,3 años por duplicación; 30 años ≈ 4 duplicaciones (x16). US$ 1.000 → ~US$ 17.050.
- El camino real: llegó a x2 el 1999-11-18 (3 años), pero volvió a estar debajo de x2 hasta el 2011-10-05 (casi 15 años después del inicio). Peor caída: -55,2 % (2007-10-09 a 2009-03-09).
- Inflación EE. UU.: 2,60 % anual en 20 años → los precios se duplican cada ~28 años. Comisión de 2 % anual → 36 años para llevarse la mitad.

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Al diez por ciento anual, tu plata se duplica en unos siete años. Y lo podés calcular de memoria, con una sola división. | x2 EN 7 AÑOS | Gráfico: número grande "x2 en 7 años" con subtítulo "al 10 % anual" |
| 2 | Hagamos la cuenta. Se llama la regla del setenta y dos. | REGLA DEL 72 | Pixabay: calculator hand close up |
| 3 | Dividís setenta y dos por la tasa anual. El resultado son los años que tarda en duplicarse. | 72 ÷ TASA = AÑOS | Gráfico: flujo "72 ÷ tasa anual (%) = años para duplicar" |
| 4 | Al seis por ciento, doce años. Al diez por ciento, siete años y pico. | 6 % → 12 AÑOS | Gráfico: lista "3 % → 24 años / 6 % → 12 años / 10 % → 7,2 años / 12 % → 6 años" |
| 5 | Probémosla con datos reales. El SPY, con dividendos reinvertidos, rindió casi diez por ciento anual en los últimos treinta años. | SPY: 9,9 % ANUAL | Pixabay: wall street sign new york |
| 6 | Setenta y dos dividido diez da unos siete años. En treinta años son cuatro duplicaciones: multiplicar por dieciséis. | x2 x2 x2 x2 = x16 | Gráfico: flujo "1.000 → 2.000 → 4.000 → 8.000 → 16.000" |
| 7 | La cuenta real: mil dólares de noviembre de 1996 hoy son unos diecisiete mil. La regla anduvo. | US$ 17.000 | Gráfico: línea US$ 1.000 en SPY, valor anual en noviembre: 1996: 1.000, 1998: 1.578, 2000: 1.981, 2002: 1.326, 2004: 1.794, 2006: 2.190, 2008: 1.413, 2010: 2.052, 2012: 2.417, 2014: 3.784, 2016: 4.182, 2018: 5.419, 2020: 7.467, 2022: 8.481, 2024: 13.112, 2026: 17.054 |
| 8 | Pero ojo, es un promedio. La primera duplicación tardó tres años, y después vinieron dos crisis. | NO ES PAREJO | Pixabay: roller coaster ride |
| 9 | Con una caída de cincuenta y cinco por ciento en el medio, recién en 2011 quedó para siempre arriba del doble. | -55 % | Gráfico: línea con zoom 1996-2011 y la raya de "x2" marcada: cruza en 1999, vuelve a caer en 2002 y 2008, la pasa definitivamente en 2011 |
| 10 | La regla también sirve al revés. Con la inflación de Estados Unidos, los precios en dólares se duplican cada veintiocho años. | INFLACIÓN: x2 EN 28 AÑOS | Pixabay: supermarket shopping cart prices |
| 11 | Y una comisión de dos por ciento anual se lleva la mitad de tu plata en treinta y seis años. | 72 ÷ 2 = 36 | Gráfico: barras "Sin comisión 100 %" contra "Con 2 % anual, a los 36 años: 50 %" |
| 12 | Ya sabés cómo estimar una duplicación sin calculadora. Y que lo que pasó no garantiza lo que viene. | 72 ÷ TASA | Gráfico: remate "72 ÷ tasa = años para duplicar" |
| 13 | ¿Qué te parece más difícil: conseguir una buena tasa o aguantar los años que hacen falta? Votá abajo. | CONSEGUIR LA TASA / AGUANTAR LOS AÑOS | Placa de encuesta + cierre |

## Encuesta para poner
¿Qué es más difícil? / Conseguir la tasa / Aguantar los años

## Caption
Regla del 72: dividís 72 por la tasa anual y te da, más o menos, los años que tarda en duplicarse la plata. Al 6 %, 12 años; al 10 %, unos 7. La probamos con el SPY: del 14/11/1996 al 13/11/2026 rindió 9,9 % anual con dividendos reinvertidos, y mil dólares se hicieron unos 17 mil (cuatro duplicaciones). Pero el camino no fue parejo: hubo una caída de 55 % y recién en 2011 quedó definitivamente arriba del doble. También sirve al revés: con la inflación de EE. UU. de los últimos 20 años (2,6 % anual, CPI del BLS), los precios se duplican cada 28 años.
Es una aproximación, no una fórmula exacta. Cálculo con datos de Yahoo Finance al 13/11/2026, sin comisiones ni impuestos. Cuenta en dólares.
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#regladel72 #interescompuesto #inversiones #spy #inflacion #finanzas #argentina

## A revisar (agente financiero)
- Fila 6 redondea 9,92 % a "diez" y 7,3 años a "siete": 30 años dan 4,1 duplicaciones (x17,5 por regla, x17,05 real). ¿Alcanza con "unos"?
- Fila 11: 0,98^36 = 0,48; la regla da "la mitad" como aproximación.
- CPI de octubre de 2026 (337,511) tomado del comunicado del BLS del 2026-11-10; octubre de 2006 (201,8) de la tabla histórica del BLS.
