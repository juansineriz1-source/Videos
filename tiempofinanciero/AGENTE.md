# Agente de reels @tiempofinancierok

Cuenta de Instagram nueva de juan (creada 2026-11-14, foto: el toro de Wall Street). Reels de ~60 s en castellano rioplatense con dos tipos de pieza:

1. **Historias de la bolsa** contadas en un minuto: casos reales (Madoff, GameStop, Newton y los Mares del Sur, Enron, Lehman, tulipanes, Buffett, Livermore, Long-Term Capital, FTX, YPF en Nueva York, el corralito...).
2. **La cuenta**: enseñanzas con números reales (100 USD por mes en el SPY durante 20 años, interés compuesto, el costo de no invertir, dólar colchón contra plazo fijo, cuánto rinde esperar, comisiones).

Meta: **2 reels por día**, publicados solos por Buffer cuando juan lo autorice. Hasta entonces, nada sale sin su ok.

## Reglas heredadas de @eltoroagro (no negociables)
- 60 s aprox. (55-75). Gancho en 2ª persona en la frase 1; mito roto o dato que choca en la frase 2.
- La imagen cambia cada 3-5 s; nada quieto más de 2-3 s. Alternar video real, foto de archivo y gráfico animado.
- Sin zoom excesivo ni cuadros cortados: la imagen se tiene que entender entera.
- No repetir clips ni fotos entre reels. Nada de tomas con subtítulos en inglés.
- Subtítulos palabra por palabra, carteles cortos en mayúscula, barra de progreso.
- **Cierre** (juan 2026-11-14, 19:19Z): SIN encuesta ni "Comentá 1 o 2" (juan: "si no podemos poner botones, no tiene ningún sentido"). El reel termina con la idea final ("Ya sabés X") y la placa de marca. El caption tampoco pide comentar 1 o 2.
- Portada diseñada (1080x1920, lo clave en el centro 1080x1440).
- Fuentes y créditos de todo video o foto de terceros en el caption.

## Reglas propias de esta cuenta
- **Voz: siempre gratis.** NUNCA Mauricio ni ElevenLabs. Voz elegida por juan: **Justo** (HeyGen gratis, voice_id 49d1050d0a764f1394587a6d2409ea80). Muestras (https://claude.ai/artifact/KFQYKBPJEAv61rQkDxAaZA).
- **Revisión financiera obligatoria**: cada guion pasa por el agente financiero (hilo "Agente financiero", cmsg_012iAc6VdP7eYJXjbazkX5KbADCKJgTiF33bho4iEiQ4Td; desde el 14/11 el hilo de IOL ya no revisa reels) antes de grabar. Revisa datos, fechas, cuentas y que la enseñanza tenga sentido. Si marca algo, se corrige antes de armar.
- Números calculados con datos reales (Yahoo con period1/period2, dividendos reinvertidos cuando corresponda) y con la fecha del cálculo en el guion.
- Nunca recomendar comprar o vender algo. Caption con: "Contenido educativo. No es recomendación de inversión. Rendimientos pasados no garantizan rendimientos futuros."
- Lo dudoso o atribuido se dice como tal ("se le atribuye", "según...").
- Vos, che, guita con moderación: argentino natural, no caricatura. Cifras dichas como se dicen ("ciento once mil dólares").
- Ángulo argentino cuando sume (CEDEAR, dólar colchón, plazo fijo, Merval), sin forzarlo.

## Flujo de cada reel
1. Idea de la lista (abajo) → guion en `guiones/tf-NN-tema.md` con texto, segmentos visuales, caption y fuentes.
2. Revisión del agente financiero → correcciones.
3. Voz gratis (Edge TTS o HeyGen free) con tiempos por palabra.
4. Armado con el motor del toro (`contenido/reels-stock/armar3.py`: voz + subtítulos + clips Pixabay/Mixkit + gráficos HTML) con la paleta de esta cuenta.
5. Video y portada al NAS (`nas:contenido/tiempofinanciero/`) y al repo `videos/tiempofinanciero/` (URL pública para Buffer).
6. juan lo ve y da ok → programado en Buffer (canal IG @tiempofinancierok, 2 por día).

## Publicación
- Buffer plan gratis: 3 canales (2 ocupados por @eltoroagro IG y TikTok; el tercero es para esta cuenta) y hasta 10 posts programados por canal (5 días de cola).
- Requisito: @tiempofinancierok como cuenta profesional (Creador o Empresa) y conectada en Buffer por juan.
- Metricool está al límite de cuentas hasta 2026-12-01.

## Identidad visual (propuesta)
- Fondo azul tinta #0B1426, bronce del toro #E8B64C, verde suba #2BD67B, rojo baja #FF5A5F, blanco #F4F6FA.
- Tipografías del toro disponibles: Anton / Bebas Neue para carteles, Montserrat para textos.

## Lista de ideas (ir sumando)
Historias: Madoff, GameStop 2021, Newton y los Mares del Sur (1720), tulipanes (1637), crack del 29, lunes negro 1987, Long-Term Capital (1998), burbuja puntocom, Enron, Lehman 2008, Jesse Livermore, Buffett compra Coca-Cola, Michael Burry y la gran apuesta, FTX y SBF, Archegos, Nick Leeson y la quiebra del Barings, Hetty Green, el corralito 2001, YPF en Nueva York, el Merval en dólares desde 2001.
La cuenta: 100 USD por mes en el SPY 20 años, 100 USD una vez en 1990, el costo de esperar 10 años para empezar, regla del 72, comisiones de 2% en 30 años, perderse los 10 mejores días, dólar colchón vs inflación de EE. UU., Apple vs iPhone (comprar la acción o el teléfono), Coca-Cola y sus dividendos, el Merval vs el SPY en dólares.

## Música y velocidad de la voz (juan 2026-11-14, 19:43Z)
- SIN música de fondo en los reels (rechazó la de los tres primeros y, después de escuchar opciones, eligió no poner). En el spec no va la clave `musica`.
- Voz 10 % más rápida que en los tres primeros reels: `"tempo": 1.21` (antes 1.1).

## Plan diario (juan 2026-11-14, 21:02Z)
Dos reels por día, todos los días:
1. **Reel de la noticia del día**, a las 10:00 de Buenos Aires: la noticia financiera o de negocios más relevante del día, verificada en 2 fuentes, máximo 58 s. El mismo reel se sube también a la historia (reemplaza a la placa de noticia).
2. **Reel de historia o enseñanza** (historias famosas, cuentas con números, cosas del mercado), a las 19:00: los guiones de la lista.
Las historias de precios siguen igual. La tarea diaria arranca 7:07 para llegar a las 10:00 con el aprobado del juez.
