#librerias para correr los modelos
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split, KFold, GridSearchCV, cross_val_score
from sklearn.metrics import (r2_score, mean_squared_error, accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, roc_curve, precision_recall_curve, make_scorer,
                             confusion_matrix, multilabel_confusion_matrix, ConfusionMatrixDisplay)

# models
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Lasso, Ridge, ElasticNet, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb



class Models:
    def __init__(self, modelo):
        self.modelo = modelo
        
    def mod(self, X_train, y_train, X_test, y_test):
        modelo1=self.modelo().fit(X_train, y_train)
        prediccion=modelo1.predict(X_test)
        r2=r2_score(y_test,prediccion)
        acc=accuracy_score(y_test,prediccion)
        prec=precision_score(y_test,prediccion)
        
        return r2, acc, prec
    
    
            
    def run_gs(modelo, params, X_train, y_train, X_test, y_test):
        model2 = modelo()
        gs = GridSearchCV(model2, params, cv=5, n_jobs=-1)
        gs.fit(X_train, y_train)
        return gs.best_score_, gs.best_params_
    
  
        
    
   