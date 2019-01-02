"Proyecto-EL4106" 

Link para acceder al dirve con las bases de datos utilizadas (archivos pesan 600 MB aprox):
https://drive.google.com/drive/folders/1ID3UAr14YoxuoChSLnaF-SxtuVNeAxv_?usp=sharing

Se recomienda agregar esta carpeta compartida a la unidad de drive, ingresar a la carpeta *BaseDatos* escribir esa ruta en la variable **ruta_base** en la segunda celda de código. De esta forma, al dar permiso a *Colaboratory* para navegar por drive, se pueden utilizar los archivos **.pkl** necesarios para preprocesar, visualizar y operar con los algoritmos de clustering.

El archivo **Preprocesamiento.ipynb** muestra paso a paso el prepocesamiento de los datos para eliminar outliers, calcular características con la librería FATS e interpolación de las curvas de luz en una fase. Junto con eso, guarda en archivos **.pkl** los resultados que se van obteniendo para evitar volver a iniciar el trabajo desde cero. También guarda los resultados finales como las características calculadas con FATS y las curvas de luz interpoladas.

El archivo **tSNE.ipynb** carga los datos generados con el archivo *Preprocesamiento.ipynb*, junta el periodo con las características calculadas con FATS, y el periodo con las curvas de luz,y utiliza este arreglo para entrenar visualizaciones con t-SNE en 500 iteraciones con una perplexidad de 35. Guarda las visualizaciones para ser utilizadas en el proceso de clustering. Además pinta las visualizaciones con las clases de las estrellas dadas por la base de datos.

El archivo **Clustering.ipynb** carga los datos generados con el archivo *Preprocesamiento.ipynb*, junta el periodo con las características, y el periodo con las curvas de luz y realiza un clustering con dos algoritmos diferentes: k-means y agglomerative clustering. Además carga los archivos que contienen las visualizaciones t-SNE para pintarlos con los clusters encontrados por los algoritmos y así poder comparar con las clases originales.
