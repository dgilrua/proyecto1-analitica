import streamlit as st
from streamlit_option_menu import option_menu
import time
import joblib
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

columns = ['person_income',
 'person_home_ownership',
 'person_emp_length',
 'loan_intent',
 'loan_grade',
 'loan_amnt',
 'loan_percent_income',
 'cb_person_default_on_file',
 'income_group',
 'loan_group']

# Codigo CSS

st.markdown(
  """
  <style>
  
  .ea3mdgi4 {
    padding-top: 0;
  }
  
  input {
    all: unset;
  }
  
  .e1f1d6gn2 {
    margin-bottom: 2rem;
  }
  
  .e1nzilvr1 {
    text-align: center;
  }
  
  .css-1y4p8pa {
    width: 90%;
    max-width: 1200rem;
  }
  
  .st-emotion-cache-16idsys p{
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    font-weight: 600;
  }
  
  .stProgress {
    width: 80%;
    margin: 0 auto;
  }
  
  .stButton {
    margin: 0 auto;
    width: 40%!important;
  }
  
  .ef3psqc12 {
    width: 100%;
    align-items: center;
    background-color: #1E90FF;
    border: none;
    margin-top: 30px;
  }
  
  .ef3psqc12:hover {
    background-color: #1773cd;
  }
  
  .e115fcil1 {
    margin: 0 auto;
  }
  
  .nav-link-horizontal {
    font-weight: 600;
    font-size: 1.2rem;
  }
  
  .st-emotion-cache-10oheav {
    padding: 2rem 1rem;
  }
  
  .st-emotion-cache-10oheav h1{
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
  }
  
  .st-emotion-cache-1p1nwyz p {
    font-weight: 400;
  }
  
  .st-emotion-cache-1kyxreq img{
    width: 100%;
    max-width: 90%;
    margin: 0 auto;
  }
  
  .st-emotion-cache-ul2nnp p {
    font-weight: 400;
  }
  
  .st-emotion-cache-ul2nnp p a{
    background-color: transparent;
    font weight: bold;
    text-decoration: none;
    text-align: center;
  }
  
  .st-emotion-cache-5rimss p{
    line-height: 2.0; 
    font-size: 1.1rem;
    text-align: justify;
  }
  
  .st-emotion-cache-5rimss img{
    width: auto;
    max-width: 100%;
  }
  
  .img_doc {
    width: 100%;
    text-align: center;
  }
  
  .img_doc_full {
    width: 100%;
    text-align: center;
  }
  
  .img_doc img {
    width: 300px;
    display: block;
    margin: 0 auto;
  }
  
  .img_doc_full img {
    width: 90%;
    display: block;
    margin: 0 auto;
  }
  
  """, unsafe_allow_html=True
)

#Definir variables de estado

if 'clicked' not in st.session_state:
  st.session_state.clicked = False

if 'saved_data' not in st.session_state:
  st.session_state.saved_data = []

#Manejo de estados

def handle_click_send (arr):
  st.session_state.clicked = True
  st.session_state.saved_data = arr
  
def handle_click_back ():
  st.session_state.clicked = False
  
st.title('Analisis de :blue[riesgo crediticio]')

# Menu de opciones

selected = option_menu(
  menu_title=None,
  options=['Video', 'Scorecard', 'Reporte'],
  icons=['camera-video', 'bar-chart-line', 'file-earmark-pdf'],
  default_index=1,
  orientation='horizontal',
  styles={
    "menu": {"width": "120rem", "display": "flex", "justify-content": "space-between", "margin":"0"},
    "nav-link-selected": {"background-color": "#1E90FF"},
  }
)

if selected == 'Scorecard':
  
  
  
  if st.session_state.clicked == False:
    
    # Formulario de ingreso de datos
    
    col1, col2 = st.columns(2)

    person_income = col1.number_input(':blue[Ingresa tus ganancias mensuales]', 0, 5000000, 0)
    
    person_home_ownership = col2.selectbox(':blue[Ingresa tu tipo de vivienda]', ['Hipotecada', 'Renta', 'Propia', 'Otros'], placeholder='Selecciona tu tipo de vivienda')  
    
    person_emp_length = col1.number_input(':blue[Ingresa tu antiguedad laboral]', 0, 40, 0)
    
    loan_intent = col2.selectbox(':blue[Ingresa el proposito del prestamo]', ['Personal', 'Educacion', 'Gastos Medicos', 'Empresa', 'Hogar', 'Consolidar deuda'], 
                                placeholder='Selecciona el proposito del prestamo')
                                
    loan_grade = col1.selectbox(':blue[Ingresa el grado de riesgo del prestamo]',
                                ['A: Bajo riesgo', 'B: Bajo riesgo relativo', 'C: Riesgo moderado', 'D: Riesgo altamente moderado', 'E: Riesgo alto', 'F: Riesgo muy alto', 'G: Riesgo extremadamente alto'], 
                                placeholder='Selecciona el grado del prestamo')
    
    loan_amnt = col2.number_input(':blue[Ingresa el monto del prestamo]', 0, 1000000, 0)
    
    loan_percent_income = col1.number_input(':blue[Ingresa el porcentaje de ganancia del prestamo]', 0.00, 100.00, 0.00, step=0.01)
    
    cb_person_default_on_file = col2.selectbox(':blue[Ingresa si tienes historial de incumplimiento crediticio]', ['Si', 'No'], placeholder='Selecciona si tienes historial de incumplimiento crediticio')
    
    #Establecer rangos para la variable de ingresos y prestamos
    
    if 0 <= person_income <= 30000:
      incomme_group = 'low'
    elif 30000 < person_income <= 50000:
      incomme_group = 'low-middle'
    elif 50000 < person_income <= 70000:
      incomme_group = 'middle'
    elif 70000 < person_income <= 100000:
      incomme_group = 'middle-high'
    elif 100000 < person_income:
      incomme_group = 'high' 
    
    if 0 <= loan_amnt <= 5000:
      loan_group = 'small'
    elif 5000 < loan_amnt <= 10000:
      loan_group = 'medium'
    elif 10000 < loan_amnt <= 15000:
      loan_group = 'large'
    elif 15000 < loan_amnt:
      loan_group = 'very large'
      
    # Definir el boton de analisis
    
    boton = st.button(
      'Analizar', 
      type='primary', 
      on_click=handle_click_send, 
      args=([person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group],)
    )
    
  # Despliegue condicional luego de la ejecucion del boton 
    
  if st.session_state.clicked: 
    
    # Barra de progreso
    st.empty()
    progress_bar = st.progress(0)

    for percent_complete in range(100):
      time.sleep(0.01)
      progress_bar.progress(percent_complete + 1)
    
    progress_bar.empty()
    
    person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group = st.session_state.saved_data
    
    if person_home_ownership == 'Hipotecada':
      person_home_ownership = 'MORTGAGE'
    elif person_home_ownership == 'Renta':
      person_home_ownership = 'RENT'
    elif person_home_ownership == 'Propia':
      person_home_ownership = 'OWN'
    else:
      person_home_ownership = 'OTHER'
      
    if loan_intent == 'Personal':
      loan_intent = 'PERSONAL'
    elif loan_intent == 'Educacion':
      loan_intent = 'EDUCATION'
    elif loan_intent == 'Gastos Medicos':
      loan_intent = 'MEDICAL'
    elif loan_intent == 'Empresa':
      loan_intent = 'VENTURE'
    elif loan_intent == 'Hogar':
      loan_intent = 'HOMEIMPROVEMENT'
    elif loan_intent == 'Consolidar deuda':
      loan_intent = 'DEBTCONSOLIDATION'
    
    if loan_grade == 'A: Bajo riesgo':
      loan_grade = 'A'
    elif loan_grade == 'B: Bajo riesgo relativo':
      loan_grade = 'B'
    elif loan_grade == 'C: Riesgo moderado':
      loan_grade = 'C'
    elif loan_grade == 'D: Riesgo altamente moderado':
      loan_grade = 'D'
    elif loan_grade == 'E: Riesgo alto':
      loan_grade = 'E'
    elif loan_grade == 'F: Riesgo muy alto':
      loan_grade = 'F'
    elif loan_grade == 'G: Riesgo extremadamente alto':
      loan_grade = 'G'
    
    if cb_person_default_on_file == 'Si':
      cb_person_default_on_file = 'Y'
    else:
      cb_person_default_on_file = 'N'
    
    encoder = joblib.load('encoder.pkl') 
      
    datos = encoder.transform([[person_home_ownership, loan_intent, loan_grade, cb_person_default_on_file, incomme_group, loan_group]])
    
    person_home_ownership, loan_intent, loan_grade, cb_person_default_on_file, incomme_group, loan_group = datos[0]
    
    values = np.array([person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group])
    
    Dataframe = pd.DataFrame(values.reshape(-1, len(values)), columns=columns)
    
    model = joblib.load('scorecard_model.pkl')
    
    score = model.score(Dataframe)
    
    score = int(score[0])
    
    if cb_person_default_on_file == 1:
      score = score - 40
    
    global_mean_score = 632
    
    st.image('score-crediticio.svg', width=800)
    
    st.title('Tu score es: ' + str(score))
    
    progress_bar = st.progress(0)
    
    for i in range(int((100/850)*score)):
      progress_bar.progress(i + 1)
      time.sleep(0.001)
    
    time.sleep(0.4)  
    
    st.title('El score promedio de la poblacion es: ' + str(global_mean_score))
    
    progress_bar2 = st.progress(0)
    
    for i in range(int((100/850)*global_mean_score)):
      progress_bar2.progress(i + 1)
      time.sleep(0.001)
    
    time.sleep(0.4)  
    
    boton = st.button('Regresar', type='primary', on_click=handle_click_back)
    
    st.toast('Para regresar presiona el boton!', icon='🎉')
    
    time.sleep(1)
    
    sidebar = st.sidebar
    
    sidebar.title('¿Que es el score crediticio?')
    
    sidebar.write('es una medida numérica que evalúa la solvencia crediticia de una persona o entidad. Este puntaje se utiliza para determinar la probabilidad de que un individuo o negocio pague sus deudas de manera oportuna. En otras palabras, el score crediticio es una herramienta que los prestamistas, como bancos y compañías de tarjetas de crédito, utilizan para evaluar el riesgo crediticio de un solicitante antes de aprobar una solicitud de préstamo o línea de crédito.')
    
    url = 'https://www.transunion.co/score-de-credito'
    sidebar.write(f"[Para saber mas haz click aqui]({url})") 

if selected == 'Video':
  
  st.video('https://www.youtube.com/watch?v=H0rQc9yJlXk')

if selected == 'Reporte':
  col1, col2, col3 = st.columns([1,3,1])
  
  with open('Reporte_Tecnico/reporte.md', "r",encoding='UTF-8') as markdown_file:
    col2.markdown(markdown_file.read(), unsafe_allow_html=True)
  
  
    
