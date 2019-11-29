import numpy as np
import time
import sys
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


start_time = time.time()
neigh = KNeighborsClassifier(n_neighbors=3)

raw_data_set = pd.read_csv("boards_output.csv")

print(raw_data_set)
print("\tARRAY:\n" + str(raw_data_set.__array__()))

neigh.fit(raw_data_set.__array__(), raw_data_set["score"].tolist())
print("\tPREDICT\n" + str(neigh.predict(raw_data_set)))
col_names = list(raw_data_set)
labels = raw_data_set["score"].values
print("\tLABELS:\n" + str(labels))

predictor_cols = col_names[0 : len(col_names) - 1]
print("\tPredictor_Coloumns:\n" + ", ".join(predictor_cols))
predictors = raw_data_set[predictor_cols].values
print("\tPREDICTORS:\n" + str(predictors))

clf_knn = KNeighborsClassifier(
    n_neighbors=10,
    weights='distance'
    )
clf_knn = clf_knn.fit(predictors, labels)

score_knn = cross_val_score(clf_knn, predictors, labels, cv=2)
print("\tCross Validation score :\n" + str(score_knn))
print("\tCross Validation Mean score :\n" + str(score_knn.mean()))

col_names_ml = list(raw_data_set)
print("\tColoumn_names:\n" + ", ".join(col_names_ml))
labels_ml = raw_data_set["score"].values
print(labels_ml)

predictor_cols_ml = col_names_ml[0 : len(col_names_ml)-1]
print("\tPredictor_Coloumns:\n" + ", ".join(predictor_cols_ml))
predictors_ml = raw_data_set[predictor_cols_ml].values
print("\tPREDICTORS_M1\n" + str(predictors_ml))

X_train, X_test, y_train, y_test = train_test_split(predictors_ml, labels_ml, test_size=0.3, random_state=42)

print("X_train:\t" + str(X_train))
print("X_test:\t" + str(X_test))
print("y_train:\t" + str(y_train))
print("y_test:\t" + str(y_test))

clf_knn_ml = KNeighborsClassifier(n_neighbors=10,weights='distance')
clf_knn_ml = clf_knn.fit(X_train,y_train)
pred = clf_knn_ml.predict(X_test)
target_names = [str(i) for i in range(29)]
print("\tCLASSIFICATION_REPORT\n" + str(classification_report(y_test,pred,target_names=target_names)))
# print("\tCONFUSION_MATRIX\n" + str(confusion_matrix(y_test,pred)))

print("\tACCURACY SCORE\n" + str(accuracy_score(y_test,pred)))
# Precision, recall, accuracy, false negative and true positive.

end_time = time.time() - start_time
mins, seconds = divmod(end_time, 60)

print('\n\tTIME:\t\tMIN\tSEC')
print('\tTOTAL:\t\t( {:0d} : {:0f} )'.format(int(mins), seconds))
print("\n\t--- %s seconds ---" % (seconds + (60 * mins)))
print("\n\tKNN size:\t" + str(sys.getsizeof(clf_knn_ml)) + " Bytes\n" + "\tdata set:\t" + str(sys.getsizeof(raw_data_set)) + " Bytes\n")

print("#################################################################################################################################")
test_case = [[14,12,13,10,11,13,4,7,8,13,12,7,5,9,11,8,4,11,6,3,4,14,8,10,9]]
print(clf_knn_ml.predict(test_case))

