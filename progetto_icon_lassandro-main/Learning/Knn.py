from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from ModelInitializer import modelInitializer
from KFold import kFoldCrossValidation
import pickle as pk

# Initialize the input features X and target values
X, y = modelInitializer()

# Define the grid of hyperparameters to test
param_grid = {
    'n_neighbors': [3, 5, 7],
    'weights': ['uniform', 'distance'],
    'p': [1, 2]
}

# Create the GridSearchCV object with KNN
grid_search = GridSearchCV(
    estimator=KNeighborsRegressor(algorithm='brute'),
    param_grid=param_grid,
    cv=3,           # internal k-fold cross-validation for GridSearch
    scoring='r2'    # metric to select the best model
)

# Run the search for the best hyperparameters
grid_search.fit(X, y)

# Get the best model
best_model = grid_search.best_estimator_

# Save the best model
with open("Storage/knn.pickle", "wb") as f:
    pk.dump(best_model, f)

# Perform k-fold cross-validation on the best model
kFoldCrossValidation(best_model, X, y)

# Print the best hyperparameters found
print("Best hyperparameters:", grid_search.best_params_)