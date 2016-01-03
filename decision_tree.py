from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(wine_data_train, wine_labels_train)
tree.predict(wine_data_test)
wine_labels_test
cross_val_score(tree, wine_data, wine_labels, cv=4)
