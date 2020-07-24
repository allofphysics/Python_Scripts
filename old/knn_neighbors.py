# We're going to be using scikit-learn's built in datasets for this.

from sklearn.datasets import load_iris

iris = load_iris()
iris_data = iris.data
iris_labels = iris.target

# Can you split the data into training and test sets
from sklearn.cross_validation import train_test_split
iris_data_train,iris_data_test,iris_labels_train,iris_labels_test=train_test_split(iris_data,iris_labels)

# Now, let's use the training data and labels to train our model.
knn=KNeighborsClassifier()
knn.fit(iris_data_train,iris_labels_train)

# And now, let's predict on our test set.
knn.predict(iris_data_test)

# Let's compare the predictions to the actual labels. Output the real labels.
iris_labels_test

# Let's score our model using cross-validation to see how good it is.
cross_val_score(knn,iris_data,iris_labels)
