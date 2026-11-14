# tf-32 Acciones argentinas en dólares contra el SPY
Tipo: la cuenta. Duración objetivo: 60 s. Estado: corregido (2026-11-14).
Cálculo: no se consiguió una serie confiable de 20 años del Merval en dólares CCL (Yahoo devuelve el ^MERV incompleto y no hay CCL histórico verificable desde este entorno). Se usa el ETF ARGT (Global X MSCI Argentina), que cotiza en dólares en Nueva York desde el 2011-03-03. Período redondo: 15 años, del 2011-11-14 al 2026-11-13. Yahoo Finance, ARGT y SPY diarios con dividendos reinvertidos (adjclose), US$ 1.000 en cada uno. Sin comisiones ni impuestos. Script: `calculos/tf-32.py`.
- OJO: el ARGT NO es el Merval. Sigue un índice de MSCI que incluye empresas argentinas que cotizan afuera (MercadoLibre pesa mucho) y deja afuera a otras del panel local.
- ARGT: US$ 1.000 → ~US$ 3.800 (x3,82; 9,3 % anual). SPY: US$ 1.000 → ~US$ 7.800 (x7,81; 14,7 % anual).
- Camino del ARGT: ~US$ 693 en nov-2012, ~US$ 1.043 en nov-2019 (ocho años para volver al punto de partida).
- Peor caída ARGT: -61,7 % (2018-01-26 a 2020-03-23). Peor caída SPY en el mismo período: -33,7 % (2020-02-19 a 2020-03-23).
- 2019-08-12 (lunes posterior a las PASO): ARGT -24,4 % en un día.
- Años calendario del ARGT: 2023 +54 %, 2024 +63 %, 2026 hasta el 13/11: -19 %.
- Control: desde el lanzamiento (2011-03-03) ARGT x2,89 y SPY x7,45.

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Si hace quince años ponías mil dólares en acciones argentinas, hoy tenés unos cinco mil trescientos. Suena bien, hasta que mirás el camino. | US$ 1.000 → US$ 5.300 | Pixabay: buenos aires obelisk aerial |
| 2 | Hagamos la cuenta, en dólares y contra las acciones de Estados Unidos. | ARGENTINA vs SPY | Gráfico: número grande "x5,3 contra x7,8" con subtítulo "15 años, en dólares" |
| 3 | Para medir Argentina usamos cinco de las empresas argentinas más grandes que cotizan en Nueva York, en partes iguales: Galicia, YPF, Pampa, Macro y TGS. | 5 EMPRESAS ARGENTINAS | Gráfico: los cinco nombres en texto (sin logos) |
| 4 | Mil dólares en noviembre de 2011, con dividendos reinvertidos. Hoy son unos cinco mil trescientos. | US$ 5.300 | Gráfico: línea US$ 1.000 en las 5 argentinas, valor en noviembre: 2011: 1.000, 2012: 474, 2013: 874, 2014: 1.473, 2015: 2.330, 2016: 2.837, 2017: 5.742, 2018: 3.214, 2019: 1.600, 2020: 1.052, 2021: 1.318, 2022: 1.787, 2023: 2.360, 2024: 6.284, 2025: 8.080, 2026: 5.326 |
| 5 | Los mismos mil en el SPY son unos siete mil ochocientos. Casi cincuenta por ciento más. | SPY: US$ 7.800 | Gráfico: línea US$ 1.000 en SPY sobre la anterior, valor anual: 2011: 1.000, 2012: 1.107, 2013: 1.491, 2014: 1.732, 2015: 1.752, 2016: 1.914, 2017: 2.324, 2018: 2.481, 2019: 2.899, 2020: 3.418, 2021: 4.523, 2022: 3.883, 2023: 4.479, 2024: 6.003, 2025: 6.880, 2026: 7.808 |
| 6 | Y el camino fue una montaña rusa. Al año eran menos de quinientos. En 2017 ya eran casi seis mil. | 474 → 5.742 | Gráfico: barras "2011: 1.000 / 2012: 474 / 2017: 5.742" |
| 7 | El lunes después de las PASO de 2019, cayeron cincuenta y dos por ciento en un día. | -52 % EN UN DÍA | Pixabay: stock market crash red numbers |
| 8 | Entre 2018 y 2020 perdieron ochenta y seis por ciento. La peor caída del SPY fue treinta y cuatro. | -86 % vs -34 % | Gráfico: barras peor caída "5 argentinas: -86 %" contra "SPY: -34 %" |
| 9 | En 2024 subieron ciento cuarenta y cuatro por ciento en un año. Y en lo que va de 2026 bajan treinta y tres. | 2024: +144 % / 2026: -33 % | Gráfico: barras por año calendario "2017: +116 % / 2018: -48 % / 2019: -40 % / 2024: +144 % / 2026: -33 %" |
| 10 | Ya sabés que Argentina en dólares paga a los saltos. Y que lo que pasó no garantiza lo que viene. | A LOS SALTOS | Gráfico: remate "15 años: Argentina x3,8 / SPY x7,8" |
| 11 | ¿Qué te pesa más de las acciones argentinas: el año que suben sesenta por ciento o cuando caen sesenta? Votá abajo. | EL +60 % / EL -60 % | Placa de encuesta + cierre |

## Encuesta para poner
¿Qué te pesa más de las acciones argentinas? / El año de +60 % / La caída de -60 %

## Caption
Acciones argentinas en dólares contra el SPY, 15 años (14/11/2011 al 13/11/2026). US$ 1.000 en el ARGT: unos US$ 3.800. US$ 1.000 en el SPY: unos US$ 7.800. El camino argentino: ocho años para volver al punto de partida, una caída de 62 % entre 2018 y 2020 (24 % en un solo día después de las PASO de 2019), y casi toda la suba en 2023 y 2024.
Aclaración: usamos el ETF ARGT (cotiza en dólares en Nueva York desde 2011) porque no conseguimos una serie confiable de 20 años del Merval en dólares CCL. El ARGT no es el Merval: incluye empresas argentinas que cotizan afuera, como MercadoLibre.
Cálculo con datos de Yahoo Finance al 13/11/2026, dividendos reinvertidos, sin comisiones ni impuestos.
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#merval #argt #spy #accionesargentinas #inversiones #finanzas #argentina

## A revisar (agente financiero)
- El pedido original era Merval en CCL a 20 años. Si el agente financiero tiene una serie de CCL confiable (por ejemplo GGAL local contra ADR, o Ámbito/Rava), conviene rehacerlo con el Merval real; el resultado puede cambiar bastante porque el ARGT tiene mucho MercadoLibre.
- Control casero a 20 años con ADR en dólares (con dividendos): GGAL x5,3; YPF x1,5; SPY x7,8.
- Confirmar que el 2019-08-12 (-24,4 %) corresponde al lunes posterior a las PASO.
- "El doble": 7.808 / 3.816 = 2,05.

## Revisión financiera (2026-11-14)
Se reemplazó el ARGT por una canasta de 5 empresas argentinas en partes iguales (GGAL, YPF, PAM, BMA, TGS, ADR con dividendos, sin rebalancear). El ARGT dio x3,8 aunque tiene MercadoLibre (x17,8): no representa a 'las acciones argentinas' y la comparación no era justa. Nuevos números (calculos/tf-32-arg5.py): 5.326 contra SPY 7.808, −86% (2018-2020), −52% el lunes de las PASO, +144% en 2024 y −33% en 2026. La enseñanza 'paga a los saltos' sale más fuerte.
