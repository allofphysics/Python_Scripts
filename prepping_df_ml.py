new_df_transpose = new_df.transpose()
data_into_dict = new_df_transpose.to_dict()
census_data = [v for k, v in data_into_dict.iteritems()]

#Now, let's encode those features and instances.

from sklearn.feature_extraction import DictVectorizer
dv = DictVectorizer()
transformed_data = dv.fit_transform(census_data).toarray()
transformed_data

#Now that we've done that, let's encode the labels.


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
transformed_labels = le.fit_transform(new_df_labels)
transformed_labels

#Now that we've done that, can you separate the `transformed_data` and `transformed_labels` into training and test sets?

from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import cross_val_score

