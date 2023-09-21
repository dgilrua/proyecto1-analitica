import streamlit as st
from streamlit_option_menu import option_menu
import time

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

st.title('Analisis de :blue[riesgo crediticio]')


  
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
  
  progress_bar = st.progress(0)
  
  for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)
    
  progress_bar.empty()
  
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
    
  boton = st.button('Analizar', type='primary')

  
  
    
