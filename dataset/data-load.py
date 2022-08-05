# Loads the dataset used from drive
# Dataset consists of three modalities, i.e. Surface Electro-myogram or sEMG, tri-axis gyroscope and tri-axis accelerometer.
# Signals were captured using six Delsys wireless sensors, consisting of one sEMG sensor and one IMU containing a tri-axis accelerometer and a tri-axis gyroscope each. 

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