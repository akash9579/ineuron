import pandas as pd
#import seaborn as sns
from sklearn import preprocessing 
#from scipy import stats
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

class train:
    null_list=[]
    
    def input(self):
        data = pd.read_excel('Data_Cortex_Nuclear.xls')
        cat_features=[i for i in data.columns if data.dtypes[i]=='object'] 
        for i in range (0,data.isnull().sum().shape[0]-1):
            if(data.isnull().sum()[i]>0):
                self.null_list.append(data.isnull().sum().index[i])
        self.data=data
        self.cat_features=cat_features
        #print(data.head(1))
        #print(cat_features)
        #print(null_list)
        
    def pre(self):
        #handle null values
        null_list=self.null_list
        data=self.data
        for i in range (0,len(null_list)-1):
            data[null_list[i]]=data[null_list[i]].fillna(data[null_list[i]].mean())            
        data['H3MeK4_N']=data['H3MeK4_N'].fillna(data['H3MeK4_N'].mean())  
        #handle catogorial values
        label_encoder = preprocessing.LabelEncoder() 
        data['MouseID']=label_encoder.fit_transform(data['MouseID']) 
        data['Genotype']= label_encoder.fit_transform(data['Genotype']) 
        data['Treatment']= label_encoder.fit_transform(data['Treatment']) 
        data['Behavior']= label_encoder.fit_transform(data['Behavior'])   
        data['class']= label_encoder.fit_transform(data['class']) 
        #handle outlire
        for i in range(1,len(data.columns)-5):
            IQR=data[data.columns[i]].quantile(0.75)-data[data.columns[i]].quantile(0.25)
            upper_bridge=data[data.columns[i]].quantile(0.75)+(IQR*1.5)
            data.loc[data[data.columns[i]]>=upper_bridge,data.columns[i]]=upper_bridge


    def model(self):
        data=self.data
        x=data.iloc[:,0:79]
        y=data.pop('class')
        norm = MinMaxScaler().fit(x)
        new_x = norm.transform(x)
        X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size = 0.25)
        
        dt = tree.DecisionTreeClassifier()
        model = dt.fit(X_train, y_train)
        prad = model.predict(X_test)
        final=accuracy_score(y_test, prad)
        print("DecisionTreeClassifier")
        print(final)        
        pickle_out = open("modules/DecisionTreeClassifier.pkl","wb")
        pickle.dump(model, pickle_out)
        pickle_out.close()
        

        model1 = KNeighborsClassifier(n_neighbors=3)
        model1.fit(X_train, y_train)
        prad1=model1.predict(X_test)
        final1=accuracy_score(y_test, prad1)
        print("KNeighborsClassifier")
        print(final1)  
        pickle_out = open("modules/KNeighborsClassifier.pkl","wb")
        pickle.dump(model1, pickle_out)
        pickle_out.close()
        
        
        

        model2 = RandomForestClassifier(max_depth=2, random_state=0)
        model2.fit(X_train, y_train)
        prad2=model2.predict(X_test)
        final2=accuracy_score(y_test, prad2)   
        print("RandomForestClassifier")
        print(final2)  
        pickle_out = open("modules/RandomForestClassifier.pkl","wb")
        pickle.dump(model2, pickle_out)
        pickle_out.close()
        






#a = train()
#a.input()
#a.pre()
#a.model()