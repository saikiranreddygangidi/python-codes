from sklearn import tree
from sklearn.metrics import accuracy_score
iris_test_ids = np.random.permutation(len(iris_data)) #randomly splitting the data set
#splitting and leaving last 15 entries for testing, rest for training
iris_train_one = iris_data[iris_test_ids[:-15]]
iris_test_one = iris_data[iris_test_ids[-15:]]
iris_train_two = iris_target[iris_test_ids[:-15]]
iris_test_two = iris_target[iris_test_ids[-15:]]
iris_classify = tree.DecisionTreeClassifier()#using the decision tree for classification
iris_classify.fit(iris_train_one, iris_train_two) #training or fitting the classifier using the training set
iris_predict = iris_classify.predict(iris_test_one)
print(iris_predict) #lables predicted (flower species)
print (iris_test_two) #actual labels
print (accuracy_score(iris_predict, iris_test_two)*100) 
