from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from ModelInitializer import modelInitializer
from KFold import kFoldCrossValidation

import pickle as pk

# Initialize the input features X and target values y
X, y = modelInitializer()

# Define the grid of hyperparameters to test
param_grid = {
    'max_depth': [4, 6, 8],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['squared_error', 'friedman_mse', 'poisson']
}

# Create the GridSearchCV object with DecisionTreeRegressor
grid_search = GridSearchCV(
    estimator=DecisionTreeRegressor(random_state=4),
    param_grid=param_grid,
    cv=3,           # internal k-fold cross-validation for GridSearch
    scoring='r2'    # metric to select the best model
)

# Run the search for the best hyperparameters
grid_search.fit(X, y)

# Get the best model
best_model = grid_search.best_estimator_

# Save the best model
with open("Storage/regressionTree.pickle", "wb") as f:
    pk.dump(best_model, f)

# Perform k-fold cross-validation on the best model
kFoldCrossValidation(best_model, X, y)

# Print the best hyperparameters found
print("Best hyperparameters:", grid_search.best_params_)
