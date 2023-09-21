import streamlit as st
from streamlit_option_menu import option_menu
import time
import joblib

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
    max-width: 120rem;
  }
  
  .e1nzilvr5 p{
    font-size: 1.2rem;
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
    margin-top: 60px;
  }
  
  .ef3psqc12:hover {
    background-color: #1773cd;
  }
  
  </style>
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
  st.session_state.saved_data = []
  
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

    person_income = col1.number_input(':blue[Ingresa tus ganancias mensuales]', 0, 1000000, 0)
    
    person_home_ownership = col2.selectbox(':blue[Ingresa tu tipo de vivienda]', ['Hipotecada', 'Renta', 'Propia', 'Otros'], placeholder='Selecciona tu tipo de vivienda')  
    
    person_emp_length = col1.number_input(':blue[Ingresa tu antiguedad laboral]', 0, 40, 0)
    
    loan_intent = col2.selectbox(':blue[Ingresa el proposito del prestamo]', ['Personal', 'Educacion', 'Gastos Medicos', 'Empresa', 'Hogar', 'Consolidar deuda'], 
                                placeholder='Selecciona el proposito del prestamo')
                                
    loan_grade = col1.selectbox(':blue[Ingresa el grado de riesgo del prestamo]',
                                ['A: Bajo riesgo', 'B: Bajo riesgo relativo', 'C: Riesgo moderado', 'D: Riesgo altamente moderado', 'E: Riesgo alto', 'F: Riesgo muy alto', 'G: Riesgo extremadamente alto'], 
                                placeholder='Selecciona el grado del prestamo')
    
    loan_amnt = col2.number_input(':blue[Ingresa el monto del prestamo]', 0, 1000000, 0)
    
    loan_percent_income = col1.number_input(':blue[Ingresa el porcentaje del prestamo]', 0, 100, 0)
    
    cb_person_default_on_file = col2.selectbox(':blue[Ingresa si tienes historial crediticio]', ['Si', 'No'], placeholder='Selecciona si tienes historial crediticio')
    
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
    
    scaler = joblib.load('scaler_min_max2.pkl')
    
    datos_escalados = scaler.transform([[person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group]])
    
    print(datos)
    print(datos_escalados)
    
    boton = st.button('Regresar', type='primary', on_click=handle_click_back)

  

  

  
  
    
