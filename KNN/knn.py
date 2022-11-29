import numpy as np
import pandas as pd
from collections import Counter

# array1 = np.array((1, 2, 3))
# array2 = np.array((1, 1, 1))

# array1 = np.array((1,2,3,4,5,6))
# array2 = np.array((10,20,30,1,2,3))

# array1 = np.array([2,1,2,3,2,9])
# array2 = np.array([3,4,2,4,5,5])

def euclidean_distance(a, b):
    """Distancia euclideana entre dos arrays.

    Parametros
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distancia: float
    """
    #return np.sqrt(np.sum( np.square(a - b) ** 2 ))
    return np.linalg.norm(a-b)

#print("euclidean_distance: ", euclidean_distance(array1,array2))


def cosine_distance(a, b):
    """Similitud coseno entre dos arrays.
    Parametros
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distancia: float
    """
    #return dot(a, b)/(norm(a)*norm(b))
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

# print("cosine_distance: ", cosine_distance(array1,array2))


def manhattan_distance(a, b):
    """Distancia Manhattan entre dos arrays.

    Parametros
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distancia: float
    """
    distance = 0
    for x1, x2 in zip(a, b):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance

# print("manhattan_distance: ", manhattan_distance(array1,array2))


class KNNRegressor:
    """Regressor implementing the k-nearest neighbors algorithm.

    Parameters
    ----------
    k: int, optional (default = 5)
        Number of neighbors that are included in the prediction.
    distance: function, optional (default = euclidean)
        The distance function to use when computing distances.
    """

    def __init__(self, k=5, distance=euclidean_distance):
        """Initialize a KNNRegressor object."""
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        """Fit the model using X as training data and y as target values.

        According to kNN algorithm, the training data is simply stored.

        Parameters
        ----------
        X: numpy array, shape = (n_observations, n_features)
            Training data.
        y: numpy array, shape = (n_observations,)
            Target values.

        Returns
        -------
        self
        """
        self.X_train = X
        self.y_train = y
        pass

    def predict(self, X):
        """Return the predicted values for the input X test data.

        Assumes shape of X is [n_test_observations, n_features] where
        n_features is the same as the n_features for the input training
        data.

        Parameters
        ----------
        X: numpy array, shape = (n_observations, n_features)
            Test data.

        Returns
        -------
        result: numpy array, shape = (n_observations,)
            Predicted values for each test data sample.

        """
        
        prediccion = []
        for i in X:
            distancias = []
            posiciones = []
            resultados = []
            for j,k in enumerate(self.X_train):
                distancias.append(self.distance(i, k))
                posiciones.append(j)
                resultados.append(self.y_train[j])

            df = pd.DataFrame({'distancia':distancias, 'posicion':posiciones,'resultado':resultados})
            df = df.sort_values(axis=0,by='distancia')            
            
            prediccion.append(df['resultado'].head(self.k).mean())                        
        return prediccion