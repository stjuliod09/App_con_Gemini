
import re
import streamlit as st

def evaluar_contrasena(contrasena):
  # Expresiones regulares
  mayuscula = re.compile(r'[A-Z]')
  minuscula = re.compile(r'[a-z]')
  numero = re.compile(r'\d')
  especial = re.compile(r'[^a-zA-Z0-9]')

  # Evaluar
  tiene_mayuscula = bool(mayuscula.search(contrasena))
  tiene_minuscula = bool(minuscula.search(contrasena))
  tiene_numero = bool(numero.search(contrasena))
  tiene_especial = bool(especial.search(contrasena))

  # Sugerencias
  sugerencias = []
  if not tiene_mayuscula:
    sugerencias.append("Incluir al menos una mayúscula.")
  if not tiene_minuscula:
    sugerencias.append("Incluir al menos una minuscula.")
  if not tiene_numero:
    sugerencias.append("Incluir al menos un número.")
  if not especial:
    sugerencias.append("Incluir al menos un caracter especial.")
  return sugerencias




st.title("Evaluador de Contraseñas")
st.write("Este codigo fue elaborado por Stiven Julio Doval")
contrasena = st.text_input("Ingrese su contraseña")

if contrasena:
  sugerencias = evaluar_contrasena(contrasena)
  if sugerencias:
    st.error("La contraseña es débil. Sugerencias:")
    for sugerencia in sugerencias:
      st.write("- " + sugerencia)
  else:
    st.success("¡Excelente! Tu contraseña es fuerte.")
