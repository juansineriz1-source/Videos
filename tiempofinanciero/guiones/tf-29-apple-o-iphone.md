# tf-29 El primer iPhone o acciones de Apple
Tipo: la cuenta. Duración objetivo: 60 s. Estado: borrador, espera revisión financiera (2026-11-14).
Cálculo: Yahoo Finance, AAPL diario con dividendos reinvertidos (adjclose). Compra al cierre del 2007-06-29 (día en que salió a la venta el primer iPhone en EE. UU.; cierre ~US$ 122,04 de la época, US$ 4,36 ajustado por splits 7x y 4x) y valuación al cierre del 2026-11-13 (19,4 años: la fecha la fija el lanzamiento, no es un período redondo). Precio del iPhone: US$ 599 el modelo de 8 GB (US$ 499 el de 4 GB), con contrato de dos años. Sin comisiones ni impuestos. Script: `calculos/tf-29.py`.
- US$ 599 → ~US$ 58.500 con dividendos reinvertidos (x97,7; 26,7 % anual). Solo por precio, sin reinvertir: ~US$ 49.000 (x81,7).
- Con US$ 499 (modelo de 4 GB): ~US$ 48.700.
- Peor momento: 2009-01-20, los US$ 599 valían ~US$ 384; caída de -60,9 % desde el pico del 2007-12-28.
- Otras caídas: -43,8 % (sep-2012 a abr-2013), -38,5 % (oct-2018 a ene-2019), -30,9 % (ene-2022 a ene-2023), -33,4 % (dic-2024 a abr-2025).
- Mismo período, US$ 599 en SPY con dividendos: ~US$ 4.270.

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Si en 2007, en vez del primer iPhone, comprabas acciones de Apple, hoy tendrías más de cincuenta y ocho mil dólares. | US$ 599 → US$ 58.500 | Gráfico: número grande "US$ 58.500" con subtítulo "lo que serían hoy los US$ 599 del primer iPhone" |
| 2 | Hagamos la cuenta, con el precio de aquel día. | LA CUENTA | Pixabay: old smartphone on table |
| 3 | El primer iPhone salió a la venta en Estados Unidos el veintinueve de junio de 2007. | 29 DE JUNIO DE 2007 | Pixabay: people waiting in line outside store |
| 4 | El modelo de ocho gigas costaba quinientos noventa y nueve dólares, con contrato. | US$ 599 | Gráfico: número grande "US$ 599" con subtítulo "8 GB, con contrato" |
| 5 | Ese mismo día, esa plata en acciones de Apple, reinvirtiendo dividendos y sin vender nunca. | MISMA PLATA, EN ACCIONES | Pixabay: hand holding smartphone stock chart |
| 6 | Hoy serían unos cincuenta y ocho mil quinientos dólares. Casi cien veces más. | x98 | Gráfico: línea US$ 599 en AAPL, valor cada 29 de junio: 2007: 599, 2009: 697, 2011: 1.640, 2013: 1.988, 2015: 4.555, 2017: 5.466, 2019: 7.762, 2021: 21.788, 2023: 30.656, 2025: 32.839, nov-2026: 58.509 |
| 7 | Pero ojo. En enero de 2009, tus quinientos noventa y nueve valían trescientos ochenta y cuatro. | US$ 384 | Gráfico: línea con zoom 2007-2009: 599 → pico en dic-2007 → 384 el 20/1/2009 (-61 % desde el pico) |
| 8 | La acción había caído sesenta y uno por ciento. Y después cayó más de treinta otras cuatro veces. | -61 % | Gráfico: lista de caídas "2008: -61 % / 2013: -44 % / 2019: -38 % / 2022: -31 % / 2025: -33 %" |
| 9 | Además, en 2007 nadie sabía que ganaba Apple. Nokia y BlackBerry dominaban, y sus acciones después se hundieron. | NOKIA Y BLACKBERRY | Pixabay: old mobile phones pile |
| 10 | La misma plata en el SPY, repartida entre quinientas empresas, hoy serían unos cuatro mil trescientos dólares. | SPY: US$ 4.300 | Gráfico: barras "Apple: US$ 58.500" contra "SPY: US$ 4.270" contra "iPhone: pieza de colección" |
| 11 | Ya sabés que elegir a la ganadora es fácil mirando para atrás. Y que lo que pasó no garantiza lo que viene. | FÁCIL MIRANDO PARA ATRÁS | Gráfico: remate "US$ 599 en 2007 → US$ 58.500 en 2026, con una caída de 61 % en el medio" |
| 12 | ¿Qué es más difícil: no comprarte el teléfono o aguantar la acción cuando cae sesenta por ciento? Votá abajo. | NO COMPRAR EL TELÉFONO / AGUANTAR LA CAÍDA | Placa de encuesta + cierre |

## Encuesta para poner
¿Qué es más difícil? / No comprar el teléfono / Aguantar la caída

## Caption
El primer iPhone salió a la venta el 29/6/2007 a US$ 599 (8 GB, con contrato). Esa plata en acciones de Apple ese mismo día, con dividendos reinvertidos, hoy serían unos US$ 58.500. Pero no fue un paseo: en enero de 2009 valían US$ 384, con la acción 61 % abajo de su pico, y después hubo otras cuatro caídas de más de 30 %. Y en 2007 las líderes eran Nokia y BlackBerry. La misma plata en el SPY: unos US$ 4.270.
Cálculo con datos de Yahoo Finance del 29/6/2007 al 13/11/2026 (precio de cierre, ajustado por splits), sin comisiones ni impuestos. Cuenta en dólares.
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#apple #iphone #aapl #inversiones #cedears #bolsa #finanzas

## A revisar (agente financiero)
- Precio de lanzamiento: usé US$ 599 (8 GB); el de 4 GB salía US$ 499 (daría ~US$ 48.700). Confirmar precio y fecha (29/6/2007) con una fuente.
- Período no redondo (19,4 años) porque la fecha la fija el lanzamiento. ¿Está bien así?
- Fila 9 (Nokia y BlackBerry líderes en 2007 y caída posterior de sus acciones) va sin cifra: es conocido, pero no lo calculé. Si se quiere número, hay que sumarlo al script.
- "Otras cuatro veces más de treinta por ciento": -43,8 %, -38,5 %, -30,9 % y -33,4 %.
