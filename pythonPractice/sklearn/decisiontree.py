from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)
clf = tree.DecisionTreeClassifier(random_state=0, max_depth=2)
clf = clf.fit(X_train, y_train)
tree.plot_tree(clf)
dot_data = tree.export_graphviz(clf,
                                out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")
