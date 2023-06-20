import random

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay,classification_report,mean_squared_error
import numpy as np
y_true=[]
y_pred=[]
for i in range(1000):
    y_true.append(random.randint(0,2))
    y_pred.append(random.randint(0, 2))
# y_true=np.array([0,0,0,0,1,1,1,2,2,2])
# y_pred=([0,1,0,2,1,1,0,2,1,2])
print(classification_report(y_true,y_pred))
print(mean_squared_error(y_true,y_pred))
ConfusionMatrixDisplay.from_predictions(y_true,y_pred)
plt.show()