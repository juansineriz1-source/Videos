# Motor de reels @tiempofinancierok

Carpeta de trabajo (en la nube): scratchpad `tf/` con `assets/` (fuentes del toro), `clips/`, `img/`. Requiere node + playwright, ffmpeg, PIXABAY_API_KEY.

## Armar un reel
`python3 armar_tf2.py tf-NN.json reel-tfNN-tema.mp4` → mp4 1080x1920 + `...-portada.png`.

`tf-NN.json`:
```json
{"voz":"voz-tfNN.wav","palabras":"voz-tfNN.json","tempo":1.1,"cierre":1.8,
 "portada":{"g":"portada","k":"HISTORIAS DE LA BOLSA","h":"El fondo que <b>nunca perdía</b>","sub":"...","img":"img/x.jpg"},
 "segs":[
  {"txt":"Frase exacta de la voz.","vis":[["c:231177",1],["c:307615@2",1]],"cartel":"ESCAPATE","cartel_en":3.6},
  {"txt":"Otra frase.","vis":[["g",1,{"g":"barras", ...}]]}
 ]}
```
- `txt`: el texto de la voz de ese segmento, igual a lo que se mandó a grabar (la suma de todos los txt = el guion).
- `vis`: una o más tomas para ese segmento, con peso de duración. Regla: ninguna toma dura más de 5 s; segmentos largos llevan 2 tomas.
  - `"c:ID"` o `"c:ID@segundo"`: clip de Pixabay bajado con `clip.py` (se recorta al centro a 9:16: revisar el .jpg para que no quede cortado lo importante).
  - `["g",peso,{...}]`: gráfico animado (abajo).
- `cartel`: texto grande arriba, solo sobre clips (no sobre gráficos); `\\N` = salto. `cartel_en`: segundos desde el inicio del segmento.
- `palabras`: JSON de HeyGen con `original_words` (tiempos por palabra). `tempo`: aceleración de la voz.

## Gráficos (`g2.html`), todos aceptan `k` (volanta), `h` (título, con `<b>` oro, `<i>` rojo, `<u>` verde), `src` (fuente abajo)
Los campos `en` son la palabra de la voz en la que aparece el elemento (o un número de segundos).
- `lista`: `items:["texto",{"t":"texto","r":"derecha","hi":1,"en":"palabra"}]` (hasta 5)
- `sello`: `items:[{"t":"2000","st":"IGNORADO","en":"palabra"}]` (fila + sello rojo)
- `flujo`: `items` como lista, con flechas hacia abajo (hasta 4)
- `num`: `num:"150"`, `sub:"años de cárcel"`, `color:"oro|ver|roj"`, `row:"texto extra"`, `en`, `row_en`
- `barras`: `bars:[{"v":65,"txt":"US$ 65.000 M","label":"En los papeles","color":"roj|oro|ver|gr","en":"palabra"}]` (2 a 4)
- `linea`: `series:[{"pts":[...],"label":"VALOR","color":"ver","en":"palabra"}]`, `xl:["2006","2016","2026"]`, `min:0`
- `foto`: `img:"img/x.jpg"`, `nombre`, `pos:"50% 20%"` (foto entera en marco, sin recortar de más; crédito en `src`)
- `cita`: `texto`, `autor`
- `remate`: `big:"Es una alarma"`, `color` (rojo late; `ver`/`oro` sin latido), `en`
- `encuesta`: `h` (pregunta), `o1`, `o2`
- `portada`: `k`, `h`, `sub`, `img` opcional. `cierre`: sin parámetros.
Probar un gráfico suelto: `node render2.js prueba.png 6 '{"d":6,"at":{},"p":{...}}'` (png = cuadro en el segundo indicado).

## Clips
`python3 clip.py buscar "stock market"` y `python3 clip.py bajar ID ...`. Mirar el .jpg de cada clip antes de usarlo. No repetir clips entre reels (registro: `clips-usados.txt`).

## Voz
HeyGen gratis, voz "Justo - Professional" (voice_id 49d1050d0a764f1394587a6d2409ea80), language es, withTimestamps true. Una sola llamada por reel con el guion entero ya revisado. NUNCA ElevenLabs/Mauricio.

## v3 (2026-11-14, pedido de juan: más real y más profesional)
`armar_tf3.py` + `render3.js` + `g3.html`. Cambios sobre v2:
- Fondo vivo (grilla en perspectiva, velas, partículas), números que cuentan, líneas con brillo y etiqueta que sigue la punta, barras con degradé, sellos con golpe.
- Cualquier gráfico acepta `"bg":"c:ID@ss"` o `"bg":"v:footage/archivo.mp4@ss"`: se dibuja encima del video real oscurecido.
- Escenas nuevas: `tercio` (`nombre`, `rol`, `src`; nombre de la persona sobre el video), `titulo` (`h`, `sub`, `k`; texto grande palabra por palabra, reemplaza al cartel).
- Material real: `["v:footage/archivo.mp4@segundo", peso, {"cred":"AP Archive","pos":0.5}]` (`pos` = dónde cortar el cuadro horizontal, 0 izquierda a 1 derecha).
- `"musica":"musica/mx-188.mp3"`, `"musica_vol":0.11` (Mixkit, licencia gratis).
- `voz.py <resultado_heygen.txt> tfNN` deja `voz-tfNN.wav` y `voz-tfNN.json`.
- El armador avisa las tomas de más de 5,6 s: partirlas.
