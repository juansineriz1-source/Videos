# tf-28 Lo que se come una comisión de 2 % anual en 30 años
Tipo: la cuenta. Duración objetivo: 60 s. Estado: revisado OK (2026-11-14).
Cálculo: Yahoo Finance, SPY diario con dividendos reinvertidos (adjclose), US$ 10.000 invertidos al cierre del 1996-11-14 y valuados al cierre del 2026-11-13 (30 años). La comisión de 2 % anual se descuenta del saldo en forma diaria (factor 0,98^(1/252) por rueda); cobrándola una vez por año el resultado es casi igual (~US$ 93.000). Sin otras comisiones ni impuestos. Script: `calculos/tf-28.py`.
- Sin comisión: ~US$ 170.500 (9,92 % anual).
- Con 2 % anual: ~US$ 93.100 (7,72 % anual). Diferencia: ~US$ 77.400 = 45 % del resultado.
- Con 1 % anual: ~US$ 126.200 (se va 26 %). Con 0,5 %: ~US$ 146.800 (se va 14 %). Con 3 %: ~US$ 68.500 (se va 60 %).
- Peor caída del período (sin comisión): -55,2 % (2007-10-09 a 2009-03-09).
- La comisión de 2 % es un ejemplo: no es la de ningún fondo o administrador en particular. El SPY ya trae adentro su propio gasto (~0,09 % anual).

## Texto (voz) y visuales
| # | Voz | Cartel | Visual |
|---|---|---|---|
| 1 | Una comisión de dos por ciento anual parece poca cosa. En treinta años se te llevó casi la mitad. | 2 % → -45 % | Gráfico: número grande "-45 %" con subtítulo "se llevó una comisión de 2 % anual" |
| 2 | Hagamos la cuenta con números reales de la bolsa de Estados Unidos. | LA CUENTA | Pixabay: calculator and documents desk |
| 3 | Diez mil dólares en el SPY en noviembre de 1996. Dividendos reinvertidos, sin tocar nada treinta años. | US$ 10.000 EN 1996 | Pixabay: new york skyline 1990s |
| 4 | Sin comisión, hoy serían unos ciento setenta mil dólares. | US$ 170.000 | Gráfico: línea sin comisión, valor anual en noviembre: 1996: 10.000, 1998: 15.776, 2000: 19.806, 2002: 13.264, 2004: 17.938, 2006: 21.898, 2008: 14.134, 2010: 20.519, 2012: 24.172, 2014: 37.837, 2016: 41.816, 2018: 54.194, 2020: 74.668, 2022: 84.811, 2024: 131.115, 2026: 170.544 |
| 5 | Ahora lo mismo, pero alguien te cobra dos por ciento del saldo cada año. | 2 % POR AÑO | Pixabay: businessman signing contract |
| 6 | Hoy tendrías unos noventa y tres mil. Setenta y siete mil dólares menos. | US$ 93.000 | Gráfico: línea con 2 % debajo de la anterior, valor anual: 1996: 10.000, 1998: 15.151, 2000: 18.267, 2002: 11.753, 2004: 15.267, 2006: 17.898, 2008: 11.095, 2010: 15.471, 2012: 17.504, 2014: 26.314, 2016: 27.933, 2018: 34.767, 2020: 46.008, 2022: 50.193, 2024: 74.530, 2026: 93.133 |
| 7 | ¿Por qué tanto? Porque no se cobra sobre lo que pusiste. Se cobra cada año sobre todo lo que tenés. | SOBRE TODO EL SALDO | Gráfico: flujo "saldo → -2 % → saldo → -2 % → saldo" repetido 30 veces |
| 8 | Y cada dólar que se va deja de crecer. Es interés compuesto, pero en contra. | COMPUESTO EN CONTRA | Pixabay: coins falling from jar |
| 9 | Con uno por ciento anual se va la cuarta parte. Con medio punto, catorce por ciento. | 0,5 % · 1 % · 2 % | Gráfico: barras valor final "Sin comisión: 170.500 / 0,5 %: 146.800 / 1 %: 126.200 / 2 %: 93.100 / 3 %: 68.500" |
| 10 | Ojo: la comisión se cobra igual cuando perdés. Entre 2007 y 2009 esa inversión cayó cincuenta y cinco por ciento. | -55 % Y SE COBRA IGUAL | Pixabay: stock market crash red numbers |
| 11 | Ya sabés que un número chico, repetido treinta años, es enorme. Y que lo que pasó no garantiza lo que viene. | CHICO x 30 AÑOS = ENORME | Gráfico: remate "Sin comisión: US$ 170.500 / Con 2 % anual: US$ 93.100" |
| 12 | ¿Qué mirás primero cuando te ofrecen un fondo: cuánto rindió o cuánto cobra? Comentá 1 o 2. | CUÁNTO RINDIÓ / CUÁNTO COBRA | Placa de encuesta + cierre |

## Pregunta de cierre (va dibujada en el video con 1 y 2, y al final del texto)
¿Qué mirás primero en un fondo? / 1: Cuánto rindió / 2: Cuánto cobra

## Caption
US$ 10.000 en el SPY del 14/11/1996 al 13/11/2026, con dividendos reinvertidos: unos US$ 170.500. La misma inversión con una comisión de 2 % anual sobre el saldo: unos US$ 93.100. La comisión se llevó unos US$ 77.400, el 45 % del resultado. Con 1 % anual se va el 26 %; con 0,5 %, el 14 %. En el medio hubo una caída de 55 %, y la comisión se cobra igual.
El 2 % es un ejemplo, no la comisión de ningún fondo en particular. Cálculo con datos de Yahoo Finance al 13/11/2026, comisión descontada día a día, sin otras comisiones ni impuestos. Cuenta en dólares.
¿Qué mirás primero en un fondo? Comentá 1 (Cuánto rindió) o 2 (Cuánto cobra) 👇
Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros.
#comisiones #interescompuesto #inversiones #fondos #spy #finanzas #argentina

## A revisar (agente financiero)
- Supuesto de cobro diario sobre el saldo contra cobro anual: da casi lo mismo (93.133 contra 93.029). ¿Preferís otro esquema?
- ¿Conviene nombrar comisiones típicas de Argentina (administración de FCI, custodia) o dejarlo genérico? Lo dejé genérico para no afirmar cifras sin fuente.
- Fila 9 dice "medio punto" por 0,5 % anual.

## Revisión financiera (2026-11-14)
Verificado: 170.543 contra 93.133 (−45%), 1% −26% y 0,5% −14%. 'La cuarta parte' está bien.
