import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import pickle
from matplotlib import style, pyplot

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"
# delete the column that we want to predict
X = np.array(data.drop(columns=[predict]))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
'''
best = 0
for i in range(30):
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)
    if acc > best:
        # Write the pickled representation of the object obj to the open file object file.
        # This is equivalent to Pickler(file, protocol).dump(obj).
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
        best = acc
'''
pickle_in = open("studentmodel.pickle", 'rb')
linear = pickle.load(pickle_in)
# print("Best score is: ", best)
print("Co: \n", linear.coef_)
print("Intercept \n", linear.intercept_)
'''
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
'''
p = "G1"
style.use("ggplot")
plt.scatter(data[p], data["G3"])
plt.xlabel(p)
plt.ylabel("Final Grade")
plt.show()