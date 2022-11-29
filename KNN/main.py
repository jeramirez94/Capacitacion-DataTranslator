# imports
from make_data import make_data
from knn import euclidean_distance, manhattan_distance, cosine_distance, KNNRegressor

# get data
X, y = make_data(n_features=2, n_pts=300, noise=0.1)

# separate into training and test
X_train = X[5:]
y_train = y[5:]
X_test = X[:5]
y_test = y[:5]

# perform a KNN Regression using multiple distance functions
for f in [euclidean_distance, manhattan_distance, cosine_distance]:
    knn = KNNRegressor(k=3, distance=f)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    print(f.__name__)
    print("Compare our predictions to the actual values. Are our predictions similar?")
    print("Predictions", y_pred)
    print("Actual", y_test)
    print('*' * 50)
