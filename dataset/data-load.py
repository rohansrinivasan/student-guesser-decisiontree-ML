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