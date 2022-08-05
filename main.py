import torch
import pandas as pd
from sklearn.model_selection import train_test_split

# Loads the dataset used from drive
from google.colab import drive
drive.mount("/content/drive")
dt = pd.read_csv("/content/6ECEINATOR.csv")
dt.head()
dt.tail()
dt.info()
parameters = dt.drop('Target',axis='columns')
targets = dt['Target'] 
parameters
targets

# assign each paramter to a label
from sklearn.preprocessing import LabelEncoder

le_Gender = LabelEncoder()
le_Part_of_India = LabelEncoder()
le_Height_is_Taller_than_Mousie = LabelEncoder()
le_Do_wear_glasses = LabelEncoder()
le_Bencher_is_Front_Back_or_Middle = LabelEncoder()
le_Character_is_Introvert_Extrovert_or_Noidea = LabelEncoder()
le_Participation_only_if_Not_forced = LabelEncoder()
le_Licence_haveit_yes_no_dk = LabelEncoder()
le_Age_morethan_21 = LabelEncoder()

parameters['Gender_n'] = le_Gender.fit_transform(parameters['Gender']) 
parameters['Part_of_India_n'] = le_Part_of_India.fit_transform(parameters['Part_of_India'])
parameters['Do_wear_glasses_n'] = le_Do_wear_glasses.fit_transform(parameters['Do_wear_glasses'])
parameters['Height_is_Taller_than_Mousie_n'] = le_Height_is_Taller_than_Mousie.fit_transform(parameters['Height_is_Taller_than_Mousie']) 
parameters['Bencher_is_Front_Back_or_Middle_n'] = le_Bencher_is_Front_Back_or_Middle.fit_transform(parameters['Bencher_is_Front_Back_or_Middle'])
parameters['Character_is_Introvert_Extrovert_or_Noidea_n'] = le_Character_is_Introvert_Extrovert_or_Noidea.fit_transform(parameters['Character_is_Introvert_Extrovert_or_Noidea'])
parameters['Participation_only_if_Not_forced_n'] = le_Participation_only_if_Not_forced.fit_transform(parameters['Participation_only_if_Not_forced'])
parameters['Licence_haveit_yes_no_dk_n'] = le_Licence_haveit_yes_no_dk.fit_transform(parameters['Licence_haveit_yes_no_dk'])
parameters['Age_morethan_21_n'] = le_Age_morethan_21.fit_transform(parameters['Age_morethan_21'])
parameters.head()

parameters_n = parameters.drop(['Gender','Part_of_India','Do_wear_glasses','Height_is_Taller_than_Mousie','Bencher_is_Front_Back_or_Middle','Character_is_Introvert_Extrovert_or_Noidea','Participation_only_if_Not_forced','Licence_haveit_yes_no_dk','Age_morethan_21'],axis='columns')
parameters_n

# Decision tree classifier

from sklearn import tree

model = tree.DecisionTreeClassifier()

model.fit(parameters_n,targets)

# Base Model Accuracy
model.score(parameters_n,targets)

model.predict([[0,1,0,1,0,0,0,1,0,0]])


