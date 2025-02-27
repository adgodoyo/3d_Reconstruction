Realizado por Nicolas Dussan y Nicolas Gallego

Para la implementación usamos la libreria cv2 que contiene la mayor parte de los metodos implementados y open3d para visualizar el modelo generado.

El proceso de nuestro proyecto consta de una calibración de la camara a partir de unas imagenes de chess que nos retorna la matriz intrinseca y la distorción para ser usadas en la corrección de distorsión de las imagenes usadas para el proceso, Luego se convierten las imagenes a usar a escala de grises y se les aplica undistort para corregir la distorsión. Luego se realizan los emparejamientos para lo que se uso un matcher con norma L2 que conssite en distancia euclidiana y se seleccionaron los mejores matches con una prueba lowe. Finalmente de los emparejamientos obtenemos las matrices fundamental y escencial por medio de los metodos findfundamentalmat y findessentialmat, y la escencial la desconponemos en la matriz de rotacion y la matriz de traslación. Luego corremos las imagenes en colmap para obtener un modelo ply y lo visualizamos con open3d. Los resultados de los otros pasos quedan guardados en las carpetas que crea el codigo y el modelo final alcanza a denotar la silueta del carro sin mucho detalle en las imagenes y colores que este tiene a los lados, pero se cumple con una reconstrucción 3d que se logra distinguir el objeto.

Resultados para las matrices solicitadas:

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa01.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa02.jpg
Matriz Fundamental (F):
 [[-1.38772393e-06  3.20769874e-06 -2.51426768e-03]
 [-4.15736492e-06 -1.29814300e-06 -6.01580685e-03]
 [ 1.39885890e-03  7.80361117e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[-0.07482269  0.11383198 -0.18642071]
 [-0.22640691 -0.02430955 -0.63903701]
 [-0.04170431  0.69579233  0.02460894]]
Matriz de Rotación (R):
 [[ 0.92410883  0.34765215 -0.15862173]
 [-0.33817425  0.93731308  0.08415683]
 [ 0.17793553 -0.02412828  0.9837463 ]]
Vector de Traslación (t, normalizado):
 [[ 0.94518904]
 [-0.28206613]
 [-0.16448822]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa02.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa03.jpg
Matriz Fundamental (F):
 [[ 7.88156715e-07 -1.04794260e-06  7.40348548e-04]
 [ 6.73057938e-07  1.45901377e-07 -2.55106782e-03]
 [-2.46527560e-03  2.19375120e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.17826065 -0.03782455  0.24810166]
 [-0.10597131 -0.19193984 -0.6199838 ]
 [-0.5209388   0.44836841  0.01938604]]
Matriz de Rotación (R):
 [[ 0.78434427  0.35366602 -0.50963164]
 [-0.49810595  0.84872987 -0.17761776]
 [ 0.36972223  0.39316403  0.84185956]]
Vector de Traslación (t, normalizado):
 [[0.90026442]
 [0.36755754]
 [0.23329259]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa03.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa04.jpg
Matriz Fundamental (F):
 [[ 8.52999059e-07 -2.02010232e-06  1.04549847e-03]
 [ 1.88315296e-07 -2.86540249e-07 -6.34835409e-03]
 [-2.92023847e-03  6.80484091e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.1231491  -0.21660225  0.08690566]
 [-0.12164428 -0.09124693 -0.68549361]
 [-0.28215631  0.59810305  0.00095358]]
Matriz de Rotación (R):
 [[ 0.80604784  0.24147878 -0.54034699]
 [-0.32748459  0.94245398 -0.06733747]
 [ 0.4929916   0.23123254  0.83874358]]
Vector de Traslación (t, normalizado):
 [[0.92775554]
 [0.11811165]
 [0.35400466]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa04.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa05.jpg
Matriz Fundamental (F):
 [[ 6.35846394e-07 -1.01821311e-06  2.97791173e-04]
 [ 3.30918310e-07  2.19790769e-08 -3.10975761e-03]
 [-2.04500462e-03  2.94381671e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.10815863 -0.1444695   0.04705348]
 [-0.13180049 -0.0878158  -0.68734648]
 [-0.37394586  0.57246724  0.01156848]]
Matriz de Rotación (R):
 [[ 0.77473456  0.42861623 -0.46483813]
 [-0.49178114  0.87055439 -0.01692224]
 [ 0.39741373  0.24170886  0.88523395]]
Vector de Traslación (t, normalizado):
 [[0.96458929]
 [0.07031117]
 [0.25421221]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa05.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa06.jpg
Matriz Fundamental (F):
 [[ 6.34538127e-07 -1.44792911e-06 -4.76706028e-04]
 [ 1.09178509e-06  5.52369182e-07 -3.26853449e-03]
 [-1.27546731e-03  2.85849390e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.2009634  -0.42051073 -0.19008228]
 [ 0.39117372  0.22873574 -0.5178382 ]
 [-0.07583889  0.51668087  0.02119405]]
Matriz de Rotación (R):
 [[ 0.89272979  0.44808707 -0.04745002]
 [-0.44535729  0.89345743  0.05822973]
 [ 0.06848656 -0.0308512   0.99717491]]
Vector de Traslación (t, normalizado):
 [[ 0.70235769]
 [-0.2302463 ]
 [ 0.67355795]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa06.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa07.jpg
Matriz Fundamental (F):
 [[-6.19404034e-07  2.69853585e-06  7.48145569e-04]
 [-4.29753844e-06 -2.48076074e-06 -3.40522860e-03]
 [-2.00459233e-03  5.22756951e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[-0.06935373  0.07986761 -0.0617008 ]
 [ 0.19462773  0.10515346  0.66830848]
 [ 0.34385377 -0.60908459 -0.01453841]]
Matriz de Rotación (R):
 [[ 0.81679247  0.36259078 -0.44875158]
 [-0.41571069  0.90923089 -0.02199574]
 [ 0.40004335  0.20451678  0.89338581]]
Vector de Traslación (t, normalizado):
 [[0.98489008]
 [0.09409166]
 [0.14539012]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa07.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa08.jpg
Matriz Fundamental (F):
 [[-1.59886492e-06  1.26946585e-05 -6.70918184e-03]
 [-1.17495943e-05 -2.24370992e-06 -1.29722218e-03]
 [ 6.95972904e-03  8.68138190e-04  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.08969225 -0.63271986  0.10369646]
 [ 0.59996239  0.09435968  0.34639675]
 [-0.05925475 -0.29729491 -0.01109994]]
Matriz de Rotación (R):
 [[ 0.98281644  0.15559605  0.09930613]
 [-0.1565813   0.98766272  0.0021575 ]
 [-0.09774527 -0.01766991  0.99505459]]
Vector de Traslación (t, normalizado):
 [[ 0.40216396]
 [-0.14933635]
 [-0.90330659]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa08.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa09.jpg
Matriz Fundamental (F):
 [[ 5.18602347e-06 -1.18660265e-05  1.02449139e-03]
 [ 1.39376129e-05  8.38381861e-06 -3.02408882e-03]
 [-4.77861976e-03 -2.61770078e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[-0.02750923 -0.07511532 -0.11669453]
 [-0.25597543 -0.03528315 -0.64662661]
 [-0.17697477  0.68072389  0.01959416]]
Matriz de Rotación (R):
 [[ 0.79958674  0.40128835 -0.44679829]
 [-0.39729343  0.91136821  0.10754493]
 [ 0.45035429  0.09151853  0.88814716]]
Vector de Traslación (t, normalizado):
 [[ 0.97977887]
 [-0.17381428]
 [ 0.0991058 ]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa09.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa10.jpg
Matriz Fundamental (F):
 [[ 8.33416357e-08 -9.35646831e-06 -4.78774457e-03]
 [ 9.42612956e-06  5.06751371e-06 -1.47682103e-02]
 [ 3.00511136e-03  1.31385097e-02  1.00000000e+00]]
Matriz Esencial (E):
 [[-0.18561758  0.04747226 -0.41757491]
 [-0.1691172   0.15206978 -0.49203102]
 [ 0.32841714  0.62211414  0.01481542]]
Matriz de Rotación (R):
 [[ 0.89128528  0.26807761 -0.36571156]
 [-0.14192841  0.93092654  0.33649978]
 [ 0.43065865 -0.24801244  0.86776895]]
Vector de Traslación (t, normalizado):
 [[ 0.76016274]
 [-0.64215205]
 [ 0.09896139]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa10.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa11.jpg
Matriz Fundamental (F):
 [[-7.43597196e-07  1.13196820e-05  3.51119773e-03]
 [-1.28142347e-05 -3.37602325e-06 -6.16952712e-03]
 [-4.83869716e-03  8.63490046e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.0490208  -0.00581706  0.21408436]
 [-0.10783411 -0.06276597 -0.66103081]
 [-0.33452191  0.62231312  0.0047947 ]]
Matriz de Rotación (R):
 [[ 0.96180961  0.16856966 -0.21565374]
 [-0.18593024  0.98055561 -0.06277453]
 [ 0.2008786   0.1004737   0.97445001]]
Vector de Traslación (t, normalizado):
 [[0.95050619]
 [0.308125  ]
 [0.03996207]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa11.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa12.jpg
Matriz Fundamental (F):
 [[-2.68372004e-07  2.17457574e-06  1.47811392e-03]
 [-3.30951413e-06 -4.81774482e-07 -6.10790844e-03]
 [-2.90089221e-03  6.70495650e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.00672258  0.08424308  0.1092611 ]
 [-0.23306131 -0.07715437 -0.65315426]
 [-0.28536996  0.64222168  0.01242475]]
Matriz de Rotación (R):
 [[ 0.93838225  0.24336772 -0.24537912]
 [-0.25651459  0.96627583 -0.02261148]
 [ 0.23160101  0.08416153  0.96916346]]
Vector de Traslación (t, normalizado):
 [[ 0.98073434]
 [ 0.16198239]
 [-0.10918727]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa12.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa13.jpg
Matriz Fundamental (F):
 [[ 1.25880184e-07 -7.48777731e-07 -4.74711064e-04]
 [ 3.55365274e-07  1.05393661e-06 -6.30127986e-03]
 [-8.23538130e-04  6.24318603e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.03989581 -0.11286004  0.10255514]
 [ 0.21312668 -0.00763582  0.66473022]
 [ 0.03194482 -0.69672191 -0.03693158]]
Matriz de Rotación (R):
 [[ 0.96671169  0.21326406 -0.14137521]
 [-0.2040922   0.97594651  0.0766471 ]
 [ 0.15432072 -0.04524208  0.98698443]]
Vector de Traslación (t, normalizado):
 [[ 0.97483679]
 [-0.15907512]
 [-0.15616769]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa13.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa14.jpg
Matriz Fundamental (F):
 [[ 1.37972341e-06 -2.77890895e-06 -3.50418684e-04]
 [ 2.89399825e-07 -1.09350409e-07 -3.32314908e-03]
 [-2.14294244e-03  4.24970329e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.18189272 -0.33587274 -0.06122293]
 [-0.31399809 -0.17124919 -0.60667553]
 [-0.33433197  0.49251146 -0.0058823 ]]
Matriz de Rotación (R):
 [[ 0.31754426  0.33375269 -0.88756678]
 [-0.59886683  0.79630583  0.08517949]
 [ 0.73520348  0.50448605  0.45273576]]
Vector de Traslación (t, normalizado):
 [[ 0.83708577]
 [-0.08970747]
 [ 0.53966655]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa14.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa15.jpg
Matriz Fundamental (F):
 [[ 1.14058919e-06 -2.95599582e-06 -1.12372893e-03]
 [ 2.18180908e-06  1.22550792e-06 -4.13646870e-03]
 [-1.21604702e-03  3.83740623e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.1190388  -0.33512324 -0.19672759]
 [ 0.15896591  0.13319013 -0.65233277]
 [-0.11126435  0.5948673  -0.00507504]]
Matriz de Rotación (R):
 [[ 0.85154974  0.45518486 -0.26013416]
 [-0.45328044  0.88853911  0.07095842]
 [ 0.26343857  0.05748911  0.96296164]]
Vector de Traslación (t, normalizado):
 [[ 0.81831587]
 [-0.25080745]
 [ 0.51716028]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa15.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa16.jpg
Matriz Fundamental (F):
 [[ 9.37344425e-07  1.20974097e-05 -4.25975174e-03]
 [-1.22244533e-05  9.64326491e-07  7.75784401e-03]
 [ 2.75124591e-03 -9.33662629e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[-0.05392388 -0.69377079 -0.0603706 ]
 [ 0.69664585 -0.05924954 -0.07579222]
 [ 0.08245535  0.10372104  0.001532  ]]
Matriz de Rotación (R):
 [[ 0.99544441 -0.08165498  0.04922288]
 [ 0.08267359  0.99639512 -0.01902233]
 [-0.04749217  0.0230051   0.99860666]]
Vector de Traslación (t, normalizado):
 [[ 0.15575424]
 [-0.10420744]
 [ 0.98228378]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa16.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa17.jpg
Matriz Fundamental (F):
 [[-1.45423720e-07  2.62819410e-07 -2.67991779e-05]
 [-1.59324558e-06 -6.40568977e-07 -2.92623121e-03]
 [-1.27772885e-03  3.96109287e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[ 0.01173994 -0.07228541 -0.0443765 ]
 [-0.30145186 -0.09544587 -0.63088912]
 [-0.2971531   0.63617436  0.04056755]]
Matriz de Rotación (R):
 [[ 0.72437387  0.44229595 -0.52882586]
 [-0.469458    0.87820567  0.09145487]
 [ 0.50486799  0.18201402  0.84378861]]
Vector de Traslación (t, normalizado):
 [[ 0.99264064]
 [-0.06317889]
 [ 0.10331016]]

🔢 Calculando matrices para: C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa17.jpg ↔ C:/Users/nicol/OneDrive/Escritorio/camaro1\mejoradas\imgwa18.jpg
Matriz Fundamental (F):
 [[-1.15092587e-06  2.28959001e-06 -6.39025213e-04]
 [-4.55256479e-06 -2.01644447e-06 -5.61228951e-03]
 [-1.29159491e-03  8.73359869e-03  1.00000000e+00]]
Matriz Esencial (E):
 [[-0.04052731  0.06245698 -0.02313632]
 [-0.3140829  -0.12330772 -0.62079458]
 [-0.27175813  0.64860502  0.01190165]]
Matriz de Rotación (R):
 [[ 0.83317614  0.39866203 -0.38325722]
 [-0.41939062  0.90724238  0.03198068]
 [ 0.36045668  0.13408895  0.92308783]]
Vector de Traslación (t, normalizado):
 [[ 0.99390279]
 [-0.03901873]
 [-0.10312513]]