# Diseño del reel de noticias @tiempofinancierok: "papel y marcador"
Lab de diseño, 2026-11-14. Pedido de juan: buen diseño, gráficos dinámicos, estética linda, imágenes HD, humor.

## Idea
El look anterior (brillos, grilla en perspectiva, velas, partículas) parece plantilla de cripto. Este es de diario financiero con humor: fondo azul noche plano, papel crema, tinta, un solo acento oro que funciona como marcador, y una cinta de teletipo arriba. Nada de sombras de neón ni degradés.
- Colores: noche #070D1A, papel #F1E7D3, tinta #0A1226, oro #F2B84B, verde #2FCB85 (sube), rojo #F0525B (baja). Sobre papel el oro se oscurece a #B26A00.
- Letras: Anton (títulos y números), DM Serif Display Italic (solo el refrán y el lema), JetBrains Mono (cinta, volantas, fuente, crédito), Montserrat (bajadas).
- Zona segura: todo entre y 260 y 1420, x 60 a 1000.

## Archivos
- `n1.html`: escenas. Misma interfaz que g3.html (`window.render(t,{d,at,p,t0})`, `en` con palabra de la voz o segundos). Para integrarlo: copiar n1.html y `fuentes/` al motor y usar render3.js apuntando a n1.html, o pegar los `if(p.g===...)` en g3.html.
- `rn.js`: `node rn.js salida.png 4.6 '{"d":5,"at":{},"p":{...}}'` (cuadro) o `node rn.js salida.mp4 0 "$(cat muestra.json)"` (lista de escenas encadenadas).
- `muestra.json` + `muestra-noticias.mp4`: día de 3 noticias, 22 s (los datos son de ejemplo, no reales). `cuadros/`: 7 cuadros 1080x1920.

## Escenas
Todas aceptan `cinta` (texto del teletipo), `src` (zócalo de fuente abajo, entra desde la izquierda), `paso:[i,n]` (barrita 1/3 2/3 3/3; `av0`/`av1` de 0 a 1 si la noticia usa varias escenas) y `wipe:true` (barrido oro de entrada).
- `gancho`: apertura. `refran` (serif; lo que va entre `<m>` se pinta con marcador), `vuelta` (tira de papel torcida que cae con golpe: la vuelta de rosca), `k`, `img`+`pos`+`cred` opcional. Tiempos: `en`, `marca_en`, `vuelta_en`.
- `sep`: separador del día de tres. `n`, `de`, `tema`, `h`. Fondo papel (invierte los colores: marca el cambio de noticia), el número rueda desde el anterior. Duración 1,5 a 2 s.
- `dato`: `num` (cuenta solo), `color`, `delta`+`dir:"up|down"` (sello verde o rojo), `sub`, `serie:[...]` (línea que se dibuja), `row`, `k`, `h`.
- `foto`: `img`, `pos`, `cred`, `k`, `h`, `alto`. Ventana con borde papel y crédito pegado a la foto.
- `cierre`: marca; `lema` opcional.

## Movimiento
- Cada escena abre con algo en 0,1 s y suma un elemento cada 0,3 a 0,7 s: volanta, título palabra por palabra, número que cuenta, sello, línea, zócalo. Nada queda quieto más de 2 s: la cinta corre siempre, las rayas del fondo se mueven, la foto avanza 4 %.
- Transiciones: barrido oro inclinado (0,4 s) al abrir el gancho y cada separador; entre escenas de la misma noticia, corte seco.
- Golpes (escala 1,9 a 1 en 0,22 s con sacudida) solo para la vuelta de rosca y el sello del dato: uno por escena como mucho.
- Ritmo sugerido: gancho 4 a 5 s; noticia = sep 1,8 s + 2 o 3 escenas de 3 a 4 s; cierre 2,4 s.

## Imágenes: de dónde y cómo
- Fuentes, en este orden: sala de prensa oficial de la empresa u organismo (Nvidia, Fed, BCRA, Casa Rosada: suelen dar 4K y permiten uso editorial), Wikimedia Commons (filtrar más de 3000 px, anotar autor y licencia), Unsplash/Pexels/Pixabay para ambiente (bolsa, billetes, ciudades), y cuadro de video real 1080p cuando no hay foto.
- Mínimo 2000 px del lado largo. La ventana mide 900 px de ancho: nunca agrandar más de 1,15 veces. Si la imagen es chica, usarla en ventana más baja (`alto`), no estirarla.
- Encuadre: persona o edificio entero, cara en el tercio de arriba (`pos`), sin cortar cabezas ni logos. Sin textos ni zócalos en inglés adentro de la foto: recortarlos antes.
- Color (ya lo hace `ventana()` en n1.html, igual para todas): saturación 0,8, contraste 1,06, sombras hacia azul noche y luces hacia crema, grano fino encima de todo. Así una foto de prensa y una de archivo parecen de la misma familia. No usar filtros propios por foto.
- Crédito siempre visible en la etiqueta papel de la foto ("Foto: Reuters", "Video: CNBC"), y la fuente del dato en el zócalo.
- Sin emojis; flechas y triángulos se dibujan con CSS.
