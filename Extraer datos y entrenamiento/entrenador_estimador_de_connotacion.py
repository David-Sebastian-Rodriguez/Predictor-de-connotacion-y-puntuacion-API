#!pip install -U textblob
nltk.download('punkt')
import nltk
import joblib
import json
from textblob.classifiers import NaiveBayesClassifier
#Carga los datos de entrenamiento y entrena el modelo
with open('trainData.json','r') as dat:
  estimador = NaiveBayesClassifier(dat,format="json")
#Carga datos de validacion
with open('validationData.json') as f:
  validacion = json.load(f)

#Realiza la validacion del modelo resultante
cont=0
for val in validacion:
  if(estimador.classify(val['text'])==val['label']):
      cont+=1
      
print('porcentaje de aciertos: ' + str(100*cont/len(validacion)) + '%')
#Guarda el modelo
joblib.dump(estimador,'model.pkl',compress=9)