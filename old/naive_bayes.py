from sklearn.naive_bayes import GaussianNB


from sklearn.datasets import load_digits
gnb = GaussianNB()
digits = load_digits()
digits_data = digits.data
digits_labels = digits.target

# Once again, split the data into training and test sets.
digits_data_train,digits_data_test,digits_labels_train,digits_labels_test=train_test_split(digits_data,digits_labels)

# Fit the model to our data.
gnb.fit(digits_data_train,digits_labels_train)

# Predict on the test set
gnb.predict(digits_data_test)
cross_val_score(gnb,digits_data,digits_labels)
