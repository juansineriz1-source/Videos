# tf-25 El costo de esperar diez años para empezar
Tipo: la cuenta. Duración objetivo: 60 s. Estado: revisado OK (2026-11-14).
Cálculo: Yahoo Finance, SPY diario con dividendos reinvertidos (adjclose), 100 USD el primer día hábil de cada mes. Plan A: desde 1996-11 hasta 2026-10 (360 aportes, 30 años). Plan B: desde 2006-11 hasta 2026-10 (240 aportes, 20 años; es el mismo de tf-02). Los dos valuados al cierre del 2026-11-13. Sin comisiones ni impuestos. Script: `calculos/tf-25.py`.
- Plan A (empezó a los 25, en 1996): puesto US$ 36.000, valor ~US$ 239.500 (x6,65).
- Plan B (esperó, empezó a los 35, en 2006): puesto US$ 24.000, valor ~US$ 111.600 (x4,65).
- Diferencia: ~US$ 127.900 de resultado por US$ 12.000 más de aportes. Los primeros 120 aportes (1996-2006) solos valen hoy ~US$ 127.900, más que todo el plan B.
- Peor momento del plan A: 2009-03-09, puesto US$ 14.900, valía ~US$ 10.000 (-33 %), después de más de 12 años aportando. Plan B ese día: puesto US$ 2.900, valía ~US$ 1.600 (-45 %).
- Las edades (25 y 35) son el marco del ejemplo; las fechas son las de los períodos redondos de 30 y 20 años hasta hoy.

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Esperar diez años para empezar a invertir te pudo costar ciento veintiocho mil dólares. | -US$ 128.000 | Gráfico: número grande "-US$ 128.000" con subtítulo "por esperar 10 años" |
| 2 | Hagamos la cuenta: dos personas, el mismo aporte de cien dólares por mes. | LA CUENTA | Pixabay: two people walking city street |
| 3 | Las dos compran SPY, unas quinientas de las empresas más grandes de Estados Unidos, y reinvierten los dividendos. | SPY ≈ 500 EMPRESAS | Pixabay: new york stock exchange building |
| 4 | La primera arrancó a los veinticinco años, en noviembre de 1996. | EMPEZÓ A LOS 25 | Gráfico: flujo "1996 (25 años) → 2026 (55 años)", 360 aportes de US$ 100 |
| 5 | En treinta años puso treinta y seis mil dólares. Hoy tiene unos doscientos treinta y nueve mil. | US$ 239.000 | Gráfico: línea plan A, valor anual en noviembre: 1996: 105, 1998: 3.114, 2000: 6.378, 2002: 6.268, 2004: 11.299, 2006: 16.526, 2008: 12.203, 2010: 20.669, 2012: 26.886, 2014: 44.978, 2016: 52.276, 2018: 70.338, 2020: 99.862, 2022: 115.755, 2024: 182.065, 2026: 239.493 |
| 6 | La segunda esperó. Arrancó a los treinta y cinco, en noviembre de 2006. | EMPEZÓ A LOS 35 | Pixabay: hourglass sand time |
| 7 | En veinte años puso veinticuatro mil dólares. Hoy tiene unos ciento once mil. | US$ 111.000 | Gráfico: línea plan B sobre la del plan A, valor anual: 2006: 102, 2008: 1.602, 2010: 5.279, 2012: 8.756, 2014: 16.600, 2016: 20.913, 2018: 29.691, 2020: 43.859, 2022: 52.144, 2024: 83.725, 2026: 111.580 |
| 8 | Diferencia de aportes: doce mil dólares. Diferencia de resultado: ciento veintiocho mil. | 12.000 vs 128.000 | Gráfico: barras "Aportes de más: US$ 12.000" contra "Resultado de más: US$ 127.900" |
| 9 | Esos primeros doce mil, con diez años más para crecer, hoy valen más que todo lo de la segunda. | EL TIEMPO HIZO EL RESTO | Pixabay: tree growing time lapse |
| 10 | Pero ojo: la primera también se comió la caída de las puntocom y la de 2008. | DOS CRISIS | Pixabay: stock market crash red screen |
| 11 | En marzo de 2009, tras doce años aportando, había puesto catorce mil novecientos y tenía diez mil. | -33 % | Gráfico: barras al 2009-03-09 "Puesto: US$ 14.900" contra "Valía: US$ 10.000" (-33 %) |
| 12 | Ya sabés que el tiempo pesa más que el monto. Y que lo que pasó no garantiza lo que viene. | TIEMPO > MONTO | Gráfico: remate "30 años: US$ 239.500 / 20 años: US$ 111.600" |
| 13 | ¿Qué te frenó más para empezar: la falta de plata o el miedo a perder? Votá abajo. | FALTA DE PLATA / MIEDO A PERDER | Placa de encuesta + cierre |

## Encuesta para poner
¿Qué te frenó más para empezar? / Falta de plata / Miedo a perder

## Caption
Dos personas, 100 dólares por mes en el SPY. Una empezó en noviembre de 1996 (30 años): puso US$ 36.000 y hoy tendría unos US$ 239.500. La otra esperó diez años (desde noviembre de 2006): puso US$ 24.000 y tendría unos US$ 111.600. Doce mil dólares menos de aportes, casi 128 mil menos de resultado. La que empezó antes también pasó dos crisis: en marzo de 2009 tenía 33 % menos de lo que había puesto.
Cálculo con datos de Yahoo Finance al 13/11/2026: aporte el primer día hábil de cada mes, dividendos reinvertidos, sin comisiones ni impuestos. Cuenta en dólares.
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#interescompuesto #spy #inversiones #ahorro #bolsa #finanzas #argentina

## A revisar (agente financiero)
- El marco "25 vs 35 años" se resolvió con datos reales (empezar en 1996 vs 2006, ambos hasta hoy) y no con una tasa supuesta hasta los 65. ¿Está bien, o preferís el ejemplo teórico con tasa fija?
- El peor momento del plan B me da 2009-03-09 con ~US$ 1.606 (-45 %); en tf-02 figura 2/3/2009 con ~US$ 1.665 (-43 %). Unificar criterio.
- "Más de la mitad del resultado": 127.900 / 239.500 = 53 %.

## Revisión financiera (2026-11-14)
Verificado con calculos/tf-25.py: 239.493 contra 111.580, diferencia de 127.912, y −33% el 2009-03-09. Criterio unificado: el peor momento se mide con el cierre diario (tf-02 también se ajustó).
