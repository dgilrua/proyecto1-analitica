

### **Definición del problema.**
<br>

El crédito es una herramienta indispensable en el sistema económico mundial, este instrumento financiero estimula la circulación de los recursos que permiten realizar inversiones en búsqueda del aumento de la competitividad empresarial y la mejora del bienestar social. Sin embargo, las entidades crediticias se encuentran con un negocio asimétrico, en el cual si se dan préstamos de manera irracional y desproporcionada, se perderá mucho más dinero del que se pudo haber ganado, muestra de ello es la crisis financiera del 2008, cimentada en los créditos otorgados a personas con pobre historial crediticio en el sector inmobiliario, afectando no solo a entidades financieras sino también a la economía global.

<br>

De esta manera, para las entidades crediticias es de notable interés tener la capacidad de saber si una persona cumplirá o no con sus obligaciones crediticias antes de realizar el desembolso del dinero. Por tal motivo, recolectan datos del aspirante como el ingreso anual, el número de propiedades, la cantidad de dinero prestada, la finalidad del préstamo, el historial crediticio, entre otras para determinar qué tan probable es que la persona no pague, a lo cual se le da el nombre de PD (Probabilidad de Default) y clasificarlo entre las categorías de pago o no pago. Todo esto con el entrenamiento de modelos soportados por campos como la estadística y la analítica de datos.

<br>

### **Metodología.**


<br>

Para el desarrollo de un modelo que permita afrontar la problemática anteriormente mencionada, se presentan los siguientes pasos.

<br>

> 1. Exploración de datos.
> 1. Limpieza de datos.
> 1. Procesamiento de datos.
> 1. Selección de variables.
> 1. Entrenamiento del modelo.

<br>

## **Desarrollo**

<br>

#### 1. **Exploración de los Datos.**

<br>

En primer lugar se carga la base de datos con nombre *credit\_risk\_dataset.csv,* analizando aspectos básicos como el número de observaciones, la cantidad de variables, las variables con datos *null* y el tipo de dato en el cual se almacena la información. También se determina la variable loan\_status como target.

Variable loan\_status: 

> 0 &nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;No Pago, Incumplimiento de las obligaciones.

> 1 &nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;Pago, Cumplimiento de las obligaciones.

Agregado a esto, se plantean hipótesis del comportamiento de la variable target (loan\_status) frente a cambios en las demás variables:

<br>

<center>

|**income\_group**|**loan\_group**|
| :- | :- |
|loan_percent_income|Aumenta|
|person_income|Disminuye|
|income_group|Disminuye|
|loan_amnt|Aumenta|
|person_emp_length|Disminuye|

</center>

<br>
<br>

Por otra parte, el dataset tiene un total de 32581 observaciones y 12 variables, de las cuales 8 son numéricas y 4 categóricas. Posteriormente, se realiza el análisis de estadísticos descriptivos para variables numéricas y categóricas, en busca de valores atípicos y una idea inicial de la distribución de los datos.

<br>

<div class='img_doc_full'>
  <img src='https://imagizer.imageshack.com/img924/7342/AaQ2rF.png'>
  <br>
  <em>Fig 2. Descriptivos categoricos</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmAie4QEp'>
  <br>
  <em>Fig 2. Descriptivos categoricos</em>
</div>

<br>
<br>

#### 2. **Limpieza de datos.**

<br>

Con el objetivo de asegurar la utilidad del análisis, se realiza un proceso de limpieza de datos. Inicialmente se obtiene la cantidad de valores nulos en cada variable con la siguiente tabla.

<br>

<div class='img_doc'>
  <img src='https://imageshack.com/i/poMgQmbZp'>
  <br>
  <em>Fig 3. Cantidad valores nulos</em>
</div>

<br>

Como el dataset tiene un total de 32581 datos y los datos nulos no superan el 10%, se considera mejor eliminar los datos con variables nulas en lugar de imputarlos. Además, se eliminan 137 observaciones duplicadas. Posteriormente, se analiza la distribución de las variables person\_income, person\_age, person\_emp\_length y loan\_amount.

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/poZPW99tp'>
  <br>
  <em>Fig 4. Distribucion variable person_age</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmz4k45bp'>
  <br>
  <em>Fig 5. Distribucion variable loan_amnt</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/poZzGBAdp'>
  <br>
  <em>Fig 6. Distribucion variable person_emp_length</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/po397d17p'>
  <br>
  <em>Fig 7. Distribucion variable person_income</em>
</div>

<br>

Ademas se realiza un análisis de Boxplots con las variables person\_income, person\_age, person\_emp\_length y loan\_amount en busca de outliers.

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pm1MPu2cp'>
  <br>
  <em>Fig 8. BoxPlot variable person_age</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pnBtPiDrp'>
  <br>
  <em>Fig 9. BoxPlot variable loan_amnt</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmVBVqtqp'>
  <br>
  <em>Fig 10. BoxPlot variable person_emp_length</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pnMDMg2ip'>
  <br>
  <em>Fig 11. BoxPlot variable person_income</em>
</div>

<br>

En cada una de las graficas anteriores se identifican valores extremos, por lo que se deciden eliminar los datos superiores a cierto valor de las variables person\_age (valores mayor a 60 años) y person\_emp\_length (valores mayor a 40 años), esto debido a la anormalidad de estos datos en el contexto actual. 

<br>

#### 3. **Procesamiento de datos.**

<br>

Se realiza la discretización de las variables person\_age, person\_income y loan\_amnt; y se categorizan estos datos en nuevas variables como se muestra a continuación:

<br>

<center>

|**age\_group**|**income\_group**|**loan\_group**|
| :- | :- | :- |
|20-25|low (4000-30000)|small (500-5000)|
|25-30|low-middle (30000-50000)|medium (5000-10000)|
|>30|middle (50000-70000)|large (10000-15000)|
||middle-large (70000-100000)|very large (15000-35000)|
||large (>100000)||

</center>

<br>
<br>

Posteriormente, se aplica un encoder a las variables categóricas en una copia del dataset para convertirlas en variables numéricas y poder realizar el análisis de correlaciones.

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/po9kcSvup'>
  <br>
  <em>Fig 12. Dataset escalado pt.1</em>
</div>

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmzXgWahp'>
  <br>
  <em>Fig 13. Dataset escalado pt.2</em>
</div>

<br>

Se verifica que el encoder se aplicó correctamente con las imagenes anteriores, donde se muestran los 5 primeros datos del dataframe y todas las variables con información de tipo numérico, y se procede a escalar el data.frame con un escalamiento MinMax. Se escogió este tipo de escalamiento en lugar del escalamiento estándar, porque este último se ve afectado por valores atípicos, y como hay una cantidad considerable de ellos.

<br>

#### 4. **Selección de variables.**

<br>

Posteriormente se hace uso de diversas estrategias como la matriz de correlaciones, pruebas chi cuadrado, test ANOVA, análisis WoE y IV para escoger las variables estadísticamente significativas y evitar problemas de multicolinealidad en el modelo. A continuación se presenta la matriz de correlaciones entre las variables:

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmtDuwJpp'>
  <br>
  <em>Fig 14. Matriz Correlacion</em>
</div>

<br>
<br>

##### **Test de hipótesis de relevancia chi cuadrado**

<br>

La prueba de hipótesis de relevancia chi cuadrado, permite evaluar la relevancia de las variables categóricas con el siguiente juego de hipótesis:

> $h_0$: La variable categórica es irrelevante. (Vp > alpha)

> $h_1$: La variable categórica es relevante. (Vp < alpha)

<br>

<div class='img_doc'>
  <img src='https://imageshack.com/i/pn4G3CfPp'>
  <br>
  <em>Fig 15. Tabla Chi2</em>
</div>

<br>

Se puede apreciar que la única variable que no rechaza la hipótesis nula que indica irrelevancia estadística, es la variable cb\_person\_cred\_hist\_length, la cual hace referencia a los años de historial crediticio que tiene la persona.

<br>

##### **Test de hipótesis de relevancia ANOVA**

<br>

También se realizó un test ANOVA para cada variable continua, cuyos resultados fueron

<br>

<div class='img_doc'>
  <img src='https://imageshack.com/i/pm6ZdUmHp'>
  <br>
  <em>Fig 16. Tabla ANOVA</em>
</div>

<br>

De esta manera, como los Vp son tan pequeños, se acepta la significancia estadística de todas las variables continuas.

<br>

#### **Weight of Evidence (WoE) e Information Value (IV)**

<br>

Finalmente, se toma el criterio de Information Value como decisor para escoger las variables a tener en cuenta para la elaboración del modelo. A continuación se presentan las fórmulas para conseguir este resultado y se considerarán las variables cuyo IV sea superior a 0.02.

<div class='img_doc'>
  <img src='https://imageshack.com/i/pmE90ipjp'>
  <br>
  <em>Fig 17. Formula calculo Woe</em>
</div>

<br>

<div class='img_doc'>
  <img src='https://imageshack.com/i/pmfhrVxxp'>
  <br>
  <em>Fig 18. Formula calculo IV</em>
</div>

<br>

Con estas formulas se hizo un calculo general para cada una de las variables y poder filtrar aquellas que tengan un IV superior a 0.02.

<br>

<div class='img_doc'>
  <img src='https://imageshack.com/i/pmbqGXmlp'>
  <br>
  <em>Fig 19. Calculo IV para cada variable</em>
</div>

<br>

Ademas se realiza un calculo de colinealidad entre todas las variables para verificar cuales de estas tiene un alto valor

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pnDL2qWLp'>
  <br>
  <em>Fig 20. Analisis colinealidad</em>
</div>

<br>

Revisando las variables loan\_grade y loan\_int\_rate en la figura anterior, se encuentra un grado de correlación de 0.93, por lo cual se decide eliminar la variable con menor *Information Value,* correspondiente a loan\_int\_rate como se aprecia en la imagen anterior.

De esta manera, se toman las variables mencionadas a continuación para el entrenamiento del modelo:

> 1. loan\_percent\_income: relación entre el crédito y el salario
> 1. loan\_grade: grado de clasificación del crédito
> 1. person\_income: salario anual de la persona
> 1. income\_group: grupo de clasificación al que pertenece el salario
> 1. person\_home\_ownership: estado de la casa (propia, rentada, hipotecada)
> 1. cb\_person\_default\_on\_file: ha hecho default antes?
> 1. loan\_amnt: monto del crédito-
> 1. loan\_intent: intención del crédito.
> 1. loan\_group: clasificación del monto del crédito
> 1. person\_emp\_length: duración de años laborando

<br>

#### **Scorecard**

<br>

Un puntaje crediticio, en el contexto financiero, es un modelo estadístico utilizado para evaluar la solvencia crediticia de individuos o entidades. Asigna una puntuación numérica para evaluar la probabilidad de que un prestatario reembolse sus deudas a tiempo.

Para esto busca identificar las características más importantes que predicen la solvencia crediticia y crea un modelo que genera un puntaje según su predicción.

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmMWEudpp'>
  <br>
  <em>Fig 21. Scorecard query variable income_group</em>
</div>

<br>

Estas características se pueden cuantificar en una variable llamada *Points*, la cual asigna un valor dependiendo de la caracteristica del usuario y como esta relaciona con la variable objetivo. Entre mejor sea esta relacion mas puntos seran asignados a la caracteristica en cuestion y entre menor sea la relacion menos puntos habrá 

<br>

#### **Modelo**

Se presenta a continuación la matriz de confusión asociada al modelo y las métricas arrojadas por el mismo.![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.018.png)

El modelo presenta un accuracy de 0.847 aproximadamente, lo cual indica que acierta en promedio el 84.7% de las clasificaciones totales.

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.019.png)

Además, tiene una precisión aproximada de 0.734, indicando que el porcentaje de acierto de la clase de default es de 73,4%. También tiene un altísimo nivel de recall, indicando que el modelo clasifica correctamente el 95.3% de todos los clientes default.

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.020.png) ![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.021.png)

Finalmente, la métrica del f1\_score es de 0.829 mostrando un rendimiento bastante acertado para predecir clases por parte del modelo.![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.022.png)

Curva ROC
