

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

Como el dataset tiene un total de 32581 datos y los datos nulos no superan el 10%, se considera mejor eliminar los datos con variables nulas en lugar de imputarlos. Además, se eliminan 137 observaciones duplicadas. Posteriormente, se analiza la distribución de las variables person\_income y loan\_amount.

También se realiza un análisis de Boxplots con las variables person\_age y person\_emp\_length en busca de outliers.

En el Boxplot de la variable person\_age se identifican valores extremos, por lo que se decide eliminar aquellos mayores a 60.

Análogamente se realiza para la variable person\_emp\_length, donde se eliminan los valores mayores a 30.

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

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.009.png)![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.010.png)

Se verifica que el encoder se aplicó correctamente con la imagen anterior, donde se muestran los 5 primeros datos del dataframe y todas las variables con información de tipo numérico, y se procede a escalar el data.frame con un escalamiento MinMax. Se escogió este tipo de escalamiento en lugar del escalamiento estándar, porque este último se ve afectado por valores atípicos, y como hay una cantidad considerable de ellos.

<br>

#### 4. **Selección de variables.**

<br>

Posteriormente se hace uso de diversas estrategias como la matriz de correlaciones, pruebas chi cuadrado, test ANOVA, análisis WoE y IV para escoger las variables estadísticamente significativas y evitar problemas de multicolinealidad en el modelo. A continuación se presenta la matriz de correlaciones entre las variables:

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.011.png)

**Test de hipótesis de independencia chi cuadrado**

La prueba de hipótesis de independencia chi cuadrado, permite evaluar la independencia de las variables categóricas con el siguiente juego de hipótesis:

h0: La variable categórica es dependiente. (Vp > alpha)

h1: La variable categórica es independiente. (Vp < alpha)

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.012.png)

Se puede apreciar que la única variable que no rechaza la hipótesis nula que indica dependencia estadística, es la variable cb\_person\_cred\_hist\_length, la cual hace referencia a los años de historial crediticio que tiene la persona.

**Test ANOVA**

También se realizó un test ANOVA para cada variable continua, cuyos resultados fueron

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.013.png)

De esta manera, como los Vp son tan pequeños, se acepta la significancia estadística de todas las variables continuas.

**Weight of Evidence (WoE) y Information Value (IV)**

Finalmente, se toma el criterio de Information Value como decisor para escoger las variables a tener en cuenta para la elaboración del modelo. A continuación se presentan las fórmulas para conseguir este resultado y se considerarán las variables cuyo IV sea superior a 0.02.

WoE =ln(% Buenos clientes% Malos clientes)  	IV = (%non\_events - %events)\*WoE

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.014.png)

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.015.png)![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.016.png)

Revisando las variables loan\_grade y loan\_int\_rate en la figura X, se encuentra un grado de correlación de 0.93, por lo cual se decide eliminar la variable con menor *Information Value,* correspondiente a loan\_int\_rate como se aprecia en la imagen siguiente.

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.017.png)

De esta manera, se toman las variables mencionadas a continuación para el entrenamiento del modelo:

1. loan\_percent\_income: relación entre el crédito y el salario
1. loan\_grade: grado de clasificación del crédito
1. person\_income: salario anual de la persona
1. income\_group: grupo de clasificación al que pertenece el salario
1. person\_home\_ownership: estado de la casa (propia, rentada, hipotecada)
1. cb\_person\_default\_on\_file: ha hecho default antes?
1. loan\_amnt: monto del crédito-
1. loan\_intent: intención del crédito.
1. loan\_group: clasificación del monto del crédito
1. person\_emp\_length: duración de años laborando

**Scorecard**

**Modelo**

Se presenta a continuación la matriz de confusión asociada al modelo y las métricas arrojadas por el mismo.![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.018.png)

El modelo presenta un accuracy de 0.847 aproximadamente, lo cual indica que acierta en promedio el 84.7% de las clasificaciones totales.

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.019.png)

Además, tiene una precisión aproximada de 0.734, indicando que el porcentaje de acierto de la clase de default es de 73,4%. También tiene un altísimo nivel de recall, indicando que el modelo clasifica correctamente el 95.3% de todos los clientes default.

![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.020.png) ![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.021.png)

Finalmente, la métrica del f1\_score es de 0.829 mostrando un rendimiento bastante acertado para predecir clases por parte del modelo.![](Aspose.Words.660d6141-9d24-4417-b3b8-487aa590e777.022.png)

Curva ROC
