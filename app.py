"""
Inteligencia Artificial — versión web (Streamlit) de la app de escritorio.
Ejecutar localmente con:  streamlit run app.py
"""

import html
import os
import unicodedata

import streamlit as st

import contenido as C

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE_DIR, "imagenes")
DOC = os.path.join(BASE_DIR, "documentos")

TITULO_APP = "Inteligencia Artificial"
COLOR_PRIMARIO = "#7a1f1f"
COLOR_ACENTO = "#d4af37"

st.set_page_config(page_title=TITULO_APP, page_icon="🧠", layout="wide")

st.markdown(
    f"""
    <style>
    .block-container {{padding-top: 3.5rem; max-width: 1100px;}}
    .encabezado {{background: {COLOR_PRIMARIO}; color: #fff; font-size: 1.4rem;
                 font-weight: 700; padding: 12px 18px; border-radius: 10px;
                 margin-bottom: 18px;}}
    .texto {{text-align: justify; font-size: 1.05rem; line-height: 1.6;}}
    .tarjeta {{background: #1f2937; border-radius: 12px; padding: 16px 20px;
              margin-bottom: 12px;}}
    .tarjeta h4 {{margin: 0 0 6px 0;}}
    .tarjeta a {{color: {COLOR_ACENTO};}}
    .portada {{text-align: center; font-size: 2.8rem; font-weight: 800;
              margin-top: 3rem;}}
    .doc p {{text-align: justify; white-space: pre-wrap; margin: 0 0 .7rem 0;
            line-height: 1.55;}}
    .doc-fondo {{background: #fff; color: #111; border-radius: 10px; padding: 24px 32px;}}
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------------
def normalizar(texto: str) -> str:
    sin = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in sin if not unicodedata.combining(c)).lower().strip()


def encabezado(titulo: str):
    st.markdown(f'<div class="encabezado">{html.escape(titulo)}</div>', unsafe_allow_html=True)


def existe(ruta: str) -> bool:
    return bool(ruta) and os.path.exists(ruta)


def mostrar_imagen(ruta: str, **kwargs):
    if existe(ruta):
        st.image(ruta, **kwargs)
    else:
        st.warning(f"No se encontró la imagen: {os.path.basename(ruta)}")


@st.cache_data(show_spinner="Cargando documento...")
def paginas_pdf(ruta: str, zoom: float = 1.8) -> list:
    import fitz  # PyMuPDF

    paginas = []
    with fitz.open(ruta) as doc:
        for pagina in doc:
            pix = pagina.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            paginas.append(pix.tobytes("png"))
    return paginas


def mostrar_pdf(nombre: str):
    ruta = os.path.join(DOC, nombre)
    if not existe(ruta):
        st.warning(f"No se encontró el documento: {nombre}")
        return
    with open(ruta, "rb") as f:
        st.download_button("⬇️ Descargar PDF", f.read(), file_name=nombre,
                           mime="application/pdf")
    for i, png in enumerate(paginas_pdf(ruta), start=1):
        st.image(png, width="stretch", caption=f"Página {i}")


def _runs_a_html(parrafo) -> str:
    partes = []
    for run in parrafo.runs:
        if not run.text:
            continue
        t = html.escape(run.text)
        if run.bold:
            t = f"<b>{t}</b>"
        if run.italic:
            t = f"<i>{t}</i>"
        if run.underline:
            t = f"<u>{t}</u>"
        partes.append(t)
    return "".join(partes)


@st.cache_data(show_spinner="Cargando documento...")
def word_a_html(ruta: str) -> str:
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    doc = docx.Document(ruta)
    bloques = []
    for hijo in doc.element.body.iterchildren():
        etiqueta = hijo.tag.rsplit("}", 1)[-1]
        if etiqueta == "p":
            p = Paragraph(hijo, doc)
            contenido = _runs_a_html(p)
            if not contenido.strip():
                continue
            nombre = (p.style.name if p.style is not None else "").lower()
            if nombre in ("title", "título"):
                bloques.append(f"<h2>{contenido}</h2>")
            elif nombre.startswith(("heading ", "título ", "encabezado ")):
                bloques.append(f"<h3>{contenido}</h3>")
            else:
                alin = int(p.alignment) if p.alignment is not None else 3
                estilo = {1: "center", 2: "right"}.get(alin, "justify")
                bloques.append(f'<p style="text-align:{estilo}">{contenido}</p>')
        elif etiqueta == "tbl":
            t = Table(hijo, doc)
            filas = []
            for r, fila in enumerate(t.rows):
                celdas, previa = [], None
                for c in fila.cells:
                    if c._tc is previa:
                        continue
                    previa = c._tc
                    tag = "th" if r == 0 else "td"
                    celdas.append(f"<{tag} style='border:1px solid #ccc;padding:4px 8px'>"
                                  f"{html.escape(c.text.strip())}</{tag}>")
                filas.append("<tr>" + "".join(celdas) + "</tr>")
            bloques.append("<table style='border-collapse:collapse;margin-bottom:12px'>"
                           + "".join(filas) + "</table>")
    return "\n".join(bloques)


def mostrar_word(nombre: str):
    ruta = os.path.join(DOC, nombre)
    if not existe(ruta):
        st.warning(f"No se encontró el documento: {nombre}")
        return
    with open(ruta, "rb") as f:
        st.download_button(
            "⬇️ Descargar Word", f.read(), file_name=nombre,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    try:
        st.markdown(f'<div class="doc-fondo doc">{word_a_html(ruta)}</div>',
                    unsafe_allow_html=True)
    except Exception as e:  # noqa: BLE001
        st.error(f"No se pudo mostrar el documento: {e}")


# ----------------------------------------------------------------------------
# Secciones
# ----------------------------------------------------------------------------
def seccion_portada():
    st.markdown(f'<div class="portada">{TITULO_APP}</div>', unsafe_allow_html=True)
    _, centro, _ = st.columns([1, 1, 1])
    with centro:
        mostrar_imagen(os.path.join(IMG, "portada.png"), width="stretch")
    st.caption("Elige una sección en el menú de la izquierda.")


def seccion_concepto():
    encabezado("¿Qué es la IA?")
    st.subheader("¿Qué es la Inteligencia Artificial?")
    st.markdown(f'<div class="texto">{html.escape(C.TEXTO_DEFINICION_IA)}</div>',
                unsafe_allow_html=True)
    st.write("")
    cols = st.columns(len(C.IMAGENES_BANNER))
    for col, (archivo, _ancho) in zip(cols, C.IMAGENES_BANNER):
        with col:
            mostrar_imagen(os.path.join(IMG, "concepto", archivo), width="stretch")


def seccion_antecedentes():
    encabezado("Antecedentes de la IA")
    mostrar_imagen(os.path.join(IMG, "antecedentes", "LineaTiempo.png"), width="stretch")


def seccion_clasificacion():
    encabezado("Clasificación de la IA")
    tipos = list(C.TIPOS_IA)
    if st.session_state.get("sub_tipo") not in tipos:
        st.session_state["sub_tipo"] = tipos[0]
    tipo = st.selectbox("Selecciona un tipo de IA", tipos, key="sub_tipo")
    info = C.TIPOS_IA[tipo]
    _, centro, _ = st.columns([1, 2, 1])
    with centro:
        mostrar_imagen(os.path.join(BASE_DIR, info["imagen"]), width="stretch")


def seccion_herramientas():
    encabezado("Herramienta que utilizo")
    for nombre, definicion, url, logo in C.HERRAMIENTAS:
        col_logo, col_texto = st.columns([1, 8], vertical_alignment="center")
        with col_logo:
            ruta = os.path.join(IMG, "herramientas", logo)
            if existe(ruta):
                st.image(ruta, width=64)
        with col_texto:
            enlace = url.replace("https://", "").rstrip("/")
            st.markdown(
                f'<div class="tarjeta"><h4>{html.escape(nombre)}</h4>'
                f'<div class="texto">{html.escape(definicion)}</div>'
                f'<a href="{url}" target="_blank">🌐 {enlace}</a></div>',
                unsafe_allow_html=True,
            )


def seccion_disciplinas():
    encabezado("Disciplinas que formaron las bases")
    st.markdown(f'<div class="texto">{html.escape(C.INTRO)}</div>', unsafe_allow_html=True)
    st.write("")
    for titulo, cuerpo in C.DISCIPLINAS:
        st.markdown(
            f'<div class="tarjeta"><h4>{html.escape(titulo)}</h4>'
            f'<div class="texto">{html.escape(cuerpo)}</div></div>',
            unsafe_allow_html=True,
        )


def seccion_esquema():
    encabezado("Esquema de Sistema Inteligente")
    mostrar_imagen(os.path.join(IMG, "esquema", "EsquemaSistemaInteligente.png"),
                   width="stretch")


def seccion_glosario():
    encabezado("Glosario")
    terminos = list(C.TERMINOS)
    if st.session_state.get("sub_termino") not in terminos:
        st.session_state["sub_termino"] = terminos[0]

    izq, der = st.columns([2, 3])
    with izq:
        st.markdown(f"**Términos ({len(terminos)})**")
        st.radio("Términos", terminos, key="sub_termino", label_visibility="collapsed")
    with der:
        termino = st.session_state["sub_termino"]
        idx = terminos.index(termino) + 1
        st.markdown(
            f'<div class="tarjeta"><h3>{idx}. {html.escape(termino)}</h3>'
            f'<div class="texto">{html.escape(C.TERMINOS[termino])}</div></div>',
            unsafe_allow_html=True,
        )


def seccion_ensayo():
    encabezado("Ensayo")
    mostrar_pdf("SubProducto5.pdf")


def seccion_busquedas():
    encabezado("Búsquedas de algoritmo")
    mostrar_word("Subproducto1_Unidad2.docx")


def seccion_clasif_busqueda():
    encabezado("Clasificación de búsqueda de algoritmo")
    mostrar_pdf("ClasificacionBusquedaAlgoritmo.pdf")


# (clave, título, función, nombre de la clave de sub-opción o None, lista de sub-opciones)
SECCIONES = [
    ("portada", "🏠 Inicio", seccion_portada, None, []),
    ("concepto", "¿Qué es la IA?", seccion_concepto, None, []),
    ("antecedentes", "Antecedentes de la IA", seccion_antecedentes, None, []),
    ("clasificacion", "Clasificación de la IA", seccion_clasificacion, "sub_tipo", list(C.TIPOS_IA)),
    ("herramientas", "Herramienta que utilizo", seccion_herramientas, None, []),
    ("disciplinas", "Disciplinas que formaron las bases", seccion_disciplinas, None, []),
    ("esquema", "Esquema de Sistema Inteligente", seccion_esquema, None, []),
    ("glosario", "Glosario", seccion_glosario, "sub_termino", list(C.TERMINOS)),
    ("ensayo", "Ensayo", seccion_ensayo, None, []),
    ("busquedas", "Búsquedas de algoritmo", seccion_busquedas, None, []),
    ("clasif_busqueda", "Clasificación de búsqueda de algoritmo", seccion_clasif_busqueda, None, []),
]
TITULOS = [s[1] for s in SECCIONES]


# ----------------------------------------------------------------------------
# Navegación y buscador (barra lateral)
# ----------------------------------------------------------------------------
if "seccion" not in st.session_state:
    st.session_state["seccion"] = TITULOS[0]


def ir_a(titulo, clave_sub=None, sub=None):
    st.session_state["seccion"] = titulo
    if clave_sub and sub:
        st.session_state[clave_sub] = sub
    st.session_state["busqueda"] = ""


with st.sidebar:
    st.markdown(f"### {TITULO_APP}")
    consulta = st.text_input("Buscar", key="busqueda", placeholder="Buscar una sección o término...")

    if consulta.strip():
        q = normalizar(consulta)
        resultados = []
        for _clave, titulo, _f, clave_sub, subs in SECCIONES:
            if q in normalizar(titulo):
                resultados.append((titulo, titulo, None, None))
            for s in subs:
                if q in normalizar(s):
                    resultados.append((f"{s} · {titulo}", titulo, clave_sub, s))
        if not resultados:
            st.caption(f'Sin resultados para "{consulta}".')
        for i, (texto, titulo, clave_sub, sub) in enumerate(resultados[:12]):
            st.button(texto, key=f"res_{i}", on_click=ir_a, args=(titulo, clave_sub, sub),
                      width="stretch")
        st.divider()

    st.radio("Secciones", TITULOS, key="seccion", label_visibility="collapsed")

# ----------------------------------------------------------------------------
# Contenido
# ----------------------------------------------------------------------------
for _clave, titulo, funcion, _cs, _subs in SECCIONES:
    if titulo == st.session_state["seccion"]:
        funcion()
        break
