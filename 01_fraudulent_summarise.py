# Load libraries
import pandas
from pandas.tools.plotting 
import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load Bank Transcation dataset
#url
url = "bankTranscation.data"
names = ['Customer_ID', 'Txn_Amount', 'Txn_Date', 'Credit/Debit']
txn_dataset = pandas.read_csv(url, names=names)
# converting date from string to date times
#txn_dataset['Txn_Date']  = txn_dataset['Txn_date'].apply(dateutil.parser.parse, dayfirst=True)

# transcations done on particular dates and Credited
txn_dataset['Txn_Date'][txn_Dataset['Credit/Debit']=="Credit"].value_Counts()

# transcations done on particular dates and Debited
txn_dataset['Txn_Date'][txn_Dataset['Credit/Debit']=="Debit"].value_Counts()

# Checking non-null unique Customer_ID's in dataset
txn_dataset['Customer_ID'].nunique()

# Sum of Credit before 8 Nov,2016
txn_dataset['Txn_Amount'][txn_dataset['Txn_Date']<"08/11/2016"][txn_dataset['Credit/Debit']=="Credit"].sum()

# Sum of Debit after 8 Nov,2016
txn_dataset['Txn_Amount'][txn_dataset['Txn_Date']>="08/11/2016"][txn_dataset['Credit/Debit']=="Debit"].sum()

# get the sum of transcations credited for every month for each customer 
txn_dataset[txn_dataset['Credit/Debit']=="Credit"].groupby('Customer_ID')['Txn_Amount'].sum()

# get the sum of transcations debited for every month for each customer
txn_dataset[txn_dataset['Credit/Debit']=="Debit"].groupby('Customer_ID')['Txn_Amount'].sum()

# transcations Credited/Debited for each customer per month
txn_dataset.groupby(['Customer_ID','Credit/Debit'])['Txn_Date'].count()




# analysing how many datas
print(txn_dataset.shape)

# printing sample data for check
print(txn_dataset.head(10))

# describe my txn_dataset
print(txn_dataset.describe())

# reading config.properties file file 
url = "configFile.properties"