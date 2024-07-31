from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

#Carregar cinjunto de dados
iris = datasets.load_iris()

#Dividir o conjunto de dados em treinamento e teste
X_train, X_test