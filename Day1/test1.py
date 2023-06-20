from sklearn.metrics import accuracy_score,classification_report
import numpy as np
y_true=np.array([0,0,0,0,1,1,1,2,2,2])
y_pred=([0,1,0,2,1,1,0,2,1,2])
print('accuracy=',accuracy_score(y_true,y_pred))
print(classification_report(y_true,y_pred))