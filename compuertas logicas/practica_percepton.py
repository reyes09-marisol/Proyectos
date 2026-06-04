import numpy as np
#1.Definir conjunto de ejmplos X y Etiquetas y

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1],])
y = np.array([0,0,0,1])

#2. Se define las epocas y la tasa de aprendizaje
epochs = 1000
Ir = 0.1

# 3. Se agrega el cesgo 

Xb = np.hstack ([X, np.ones((X.shape[0],1))])

# 4. Se inicializan los pesos

np.random.seed(42)
w = np.random.uniform(-0.5, 0.5, size=(Xb.shape[1],))

#5. Se define la función de activación escalón

def lineal(z):
    return z

#6. Se encuentra el perceptrón
for epoch in range (epochs):                                                #Para cada epoca se itera sobre cada ejemplo
    errors = 0                                                              #Se inicializa el contador de errores
    for xi, yi in zip(Xb, y):                                               #Para cada ejemplo i=1, 2, 3, 4 se obtiene el vector de características xi y la etiqueta yi
        z = np.dot (xi, w)                                                  #Calcular potencial de activación Z = w1*x1 + w2+x2 + b
        yout = 1 if lineal(z) >= 0 else 0                                                      #Calcular salida del perceptrón yout = f(z)
        delta = yi -yout                                                    #Calcular error delta = yi - yout
        if delta != 0:                                                      #Si el error es diferente de cero, se actualizan los pesos 
            w += Ir * delta * xi                                             #Se actualizan los pesos w = w + Ir * delta xi 
            errors += 1                                                    #Se incrementa el contador de errores
    print (f"Epoch {epoch+1}/{epochs}, Errores: {errors}")
    if errors == 0:
        print(f"convergencia alcanzada en la epoca:{epoch+1}con pesos:{w}") 
        break
    
#7. Predición dado de un nuevo x E {0,1}d : formar Xb = [x;1], calcular step((w,xb)) y mostrar el resultado
def predict (x):
    Xb = np.append(x,1)     #Agregar el sesgo al vector de características
    z =np.dot(Xb, w)        #Calcular el potencial de activación
    return 1 if lineal(z) >= 0 else 0      #Devolver la prediciión usando la función de activación
#8. Imprimir predicciones para cada combinación de entrada 
for x in X:
    print(f"Entrada: {x}, Predicción: {predict(x)}")
#Se definen funciones de evaluación para medir el desempeño del modelo
def mse(y_true, y_pred):
    return float(np.mean((y_true - y_pred) ** 2))
# El coeficiente de determinación R² se calcula como 1 menos la proporción de la suma de los residuos al total de la suma de los cuadrados, proporcionando una medida de qué tan bien el modelo explica la variabilidad de los datos.
def r2_score(y_true, y_pred):
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0
    return 1.0 - (ss_res / ss_tot)
 # Se utiliza la función de evaluación para medir el desempeño del modelo en el conjunto de entrenamiento
y_pred = np.array([1 if lineal(np.dot(xi, w)) >= 0 else 0 for xi in Xb])
print(f"MSE: {mse(y, y_pred)}, R²: {r2_score(y, y_pred)}")

