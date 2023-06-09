# -*- coding: utf-8 -*-
"""crackdepth.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TyQHMGh_8UIZPhksH-l_rLofi7He4LeB
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from scipy import stats

dataset = pd.read_excel(r"C:\Users\Admin\Desktop\btp2_data\newdataset25.xlsx")

X = dataset.iloc[:,:5].values
y = dataset['Depth'].values

X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.99)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 42)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
#print(y_pred)
#df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
#pd.set_option('display.max_rows',None,'display.max_columns',None)
##print(df)

#er=mean_squared_error(y_test,y_pred,squared=False)
#print(er)

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
xaxes=np.arange(50)#len(y_test)
ax.bar(xaxes+0.0,y_test[:50],color='b',width=0.25)
ax.bar(xaxes+0.25,y_pred[:50],color='r',width=0.25)
ax.legend(labels=["real_val","predicted"])
ax.set_ylabel("depths")
ax.set_title("comparision between real and predicted depths")
plt.show()

####x=np.arange(0,len(y_test),1)
####plt.plot(x,y_test,"r")
####plt.plot(x,y_pred,"b")
####plt.xlabel("n_th data in y_test,y_pred")
####plt.ylabel("Depth")     
####plt.show()

m,c,r,p,std_err=stats.linregress(y_pred,y_test)
def f(x):
    return m*x+c
print(f"eq is {m}*x {c}")
model=list(map(f,y_pred))
plt.plot(y_pred,model,"r")
plt.plot(y_pred,y_test,"*")
plt.xlabel("Y_predicted")
plt.ylabel("Y_actual")
plt.legend(["fit","data"])
plt.title("Regression curve for predicted and actual")
plt.show()