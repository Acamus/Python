# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection	
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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
print("###########################")
print("Started Loading Dataset..........")
url = "txnDetails.csv"
names = ['Customer_ID', 'Txn_Date','Txn_Amount', 'Credit/Debit']
txn_dataset = pandas.read_csv(url, names=names)
print(txn_dataset.shape)
print("Dataset Successfully Loaded.....")
print("###########################")

############################################################
##Customer Transactions[CREDIT] before 8 Nov 2016(Demonitization)
############################################################
print("##SORTING ...Customer Transactions[CREDIT] before 8 Nov 2016#STARTED#")
before_Demo_Credit=txn_dataset[(txn_dataset['Credit/Debit']=="Cr") & (txn_dataset['Txn_Date']< '8/11/2016')].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
print("#END of SORTING ...Customer Transactions[CREDIT] before 8 Nov 2016#")
print(before_Demo_Credit.shape)

############################################################
##Customer Transactions[DEBIT] before 8 Nov 2016(Demonitization)
############################################################
print("##SORTING ...Customer Transactions[DEBIT] before 8 Nov 2016##")
before_Demo_Debit=txn_dataset[(txn_dataset['Credit/Debit']=="Dr") & (txn_dataset['Txn_Date']< '8/11/2016')].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
print("#END of SORTING ...Customer Transactions[DEBIT] before 8 Nov 2016#")
print(before_Demo_Debit.shape)

############################################################
##Customer Transactions[CREDIT] after 8 Nov 2016(Demonitization)
############################################################
print("##SORTING ....Customer Transactions[CREDIT] after 8 Nov 2016##")
after_Demo_Credit=txn_dataset[(txn_dataset['Credit/Debit']=="Cr") & (txn_dataset['Txn_Date']>= '8/11/2016')].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
print("#END of SORTING ...Customer Transactions[CREDIT] after 8 Nov 2016#")
print(after_Demo_Credit.shape)

############################################################
##Customer Transactions[DEBIT] after 8 Nov 2016(Demonitization)
############################################################
print("##SORTING....Customer Transactions[DEBIT] after 8 Nov 2016##")
after_Demo_Debit=txn_dataset[(txn_dataset['Credit/Debit']=="Dr") & (txn_dataset['Txn_Date']>= '8/11/2016')].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
print("#END of SORTING ...Customer Transactions[DEBIT] after 8 Nov 2016#")
print(after_Demo_Debit.shape)

#############################
#Writing Sorted datas to a csv file
#############################
print("Started writing sorted datas to file.....")
before_Demo_Credit.to_csv(path='before_demonCr_8Nov16.csv',sep=',')
before_Demo_Debit.to_csv(path='before_demonDr_8Nov16.csv',sep=',')
after_Demo_Credit.to_csv(path='after_demonCr_8Nov16.csv',sep=',')
after_Demo_Debit.to_csv(path='after_demonDr_8Nov16.csv',sep=',')
print("Sorte datas successfully written !")
################################
##END OF Writing Datas
################################



############################
#Loading Sorted Datas
#############################
print("Loading Datas started...")
before_Demo_Credit_url=('before_demonCr_8Nov16.csv')
before_Demo_Credit_names=['Customer_ID','Txn_Date','Credit/Debit','Txn_Amount']
before_Demo_Debit_url=('before_demonDr_8Nov16.csv')
before_Demo_Debit_names=['Customer_ID','Txn_Date','Credit/Debit','Txn_Amount']
after_Demo_Credit_url=('after_demonCr_8Nov16.csv')
after_Demo_Credit_names=['Customer_ID','Txn_Date','Credit/Debit','Txn_Amount']
after_Demo_Debit_url=('after_demonDr_8Nov16.csv')
after_Demo_Debit_names=['Customer_ID','Txn_Date','Credit/Debit','Txn_Amount']
tot_before_Demo_Credit=pandas.read_csv(before_Demo_Credit_url,names=before_Demo_Credit_names)
tot_before_Demo_Debit=pandas.read_csv(before_Demo_Debit_url,names=before_Demo_Debit_names)
tot_after_Demo_Credit=pandas.read_csv(after_Demo_Credit_url,names=after_Demo_Credit_names)
tot_after_Demo_Debit=pandas.read_csv(after_Demo_Debit_url,names=after_Demo_Debit_names)
print("Data Loading Successfull....")

####################################
#Plotting the sorted datas
###################################
"""
scatter_matrix(tot_before_Demo_Credit)
plt.show()
scatter_matrix(tot_before_Demo_Debit)
plt.show()
scatter_matrix(tot_after_Demo_Credit)
plt.show()
scatter_matrix(tot_after_Demo_Debit)
plt.show()

tot_before_Demo_Credit.plot(kind='box', subplots=True, layout=(2,1), sharex=False, sharey=False)
plt.show()
tot_before_Demo_Debit.plot(kind='box', subplots=True, layout=(2,1), sharex=False, sharey=False)
plt.show()
tot_after_Demo_Credit.plot(kind='box', subplots=True, layout=(2,1), sharex=False, sharey=False)
plt.show()
tot_after_Demo_Debit.plot(kind='box', subplots=True, layout=(2,1), sharex=False, sharey=False)
plt.show()

"""

##################################################################
#Total Credited Txn_Amount per Customer before 8 Nov 2016(COUNT&SUM)
##################################################################
tot_cr_txn_before=tot_before_Demo_Credit.groupby('Customer_ID').agg({'Txn_Amount':'sum','Credit/Debit':'count'})
print(tot_cr_txn_before.head(10))
#####################################################
#Total Debited Txn_Amount per Customer before 8 Nov 2016
#####################################################
tot_dr_txn_before=tot_before_Demo_Debit.groupby('Customer_ID').agg({'Txn_Amount':'sum','Credit/Debit':'count'})
print(tot_dr_txn_before.head(10))
#####################################################
#Total Credited Txn_Amount per Customer after 8 Nov 2016
#####################################################
tot_cr_txn_after=tot_after_Demo_Credit.groupby('Customer_ID').agg({'Txn_Amount':'sum','Credit/Debit':'count'})
#####################################################
#Total Debited Txn_Amount per Customer after 8 Nov 2016
#####################################################
tot_dr_txn_after=tot_after_Demo_Debit.groupby('Customer_ID').agg({'Txn_Amount':'sum','Credit/Debit':'count'})
print(tot_dr_txn_after.head(10))


#########################################################
#Writing the Total Credited/Debited Txn Details of a Customer in file
#########################################################
print("Started writting datas to a file.....")
tot_cr_txn_before.to_csv('tot_cr_txn_before.csv',sep=',')
tot_dr_txn_before.to_csv('tot_dr_txn_before.csv',sep=',')
tot_cr_txn_after.to_csv('tot_cr_txn_after.csv',sep=',')
tot_dr_txn_after.to_csv('tot_dr_txn_after.csv',sep=',')
print("Datas Written to file successfull...!")


####################################################
#Loading the Total Credited/Debited Txn Details of a Customer
####################################################
print("Started Loading the Total Credited/Debited Txn Details of a Customer.....")
tot_customer_cr_before_url=('tot_cr_txn_before.csv')
tot_customer_cr_before_names=['Customer_ID','Credit/Debit','Tot_Txn_Amount']
tot_customer_dr_before_url=('tot_dr_txn_before.csv')
tot_customer_dr_before_names=['Customer_ID','Credit/Debit','Tot_Txn_Amount']
tot_customer_cr_after_url=('tot_cr_txn_after.csv')
tot_customer_cr_after_names=['Customer_ID','Credit/Debit','Tot_Txn_Amount']
tot_customer_dr_after_url=('tot_dr_txn_after.csv')
tot_customer_dr_after_names=['Customer_ID','Credit/Debit','Tot_Txn_Amount']

tot_customer_cr_before_ds=pandas.read_csv(tot_customer_cr_before_url,names=tot_customer_cr_before_names)
tot_customer_dr_before_ds=pandas.read_csv(tot_customer_dr_before_url,names=tot_customer_dr_before_names)
tot_customer_cr_after_ds=pandas.read_csv(tot_customer_cr_after_url,names=tot_customer_cr_after_names)
tot_customer_dr_after_ds=pandas.read_csv(tot_customer_dr_after_url,names=tot_customer_dr_after_names)
print("Loading the Total Credited/Debited Txn Details of a Customer Successfully loaded....")

#####################################################
#Plotting the Total Credited/Debited Txn Details of a Customer
#####################################################
#Scatter_Matirx
"""
scatter_matrix(tot_customer_cr_before_ds)
plt.show()
scatter_matrix(tot_customer_dr_before_ds)
plt.show()
scatter_matrix(tot_customer_cr_after_ds)
plt.show()
scatter_matrix(tot_customer_dr_after_ds)
plt.show()
"""

#Box&Wiskhers plot
"""
tot_customer_cr_before_ds.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
tot_customer_dr_before_ds.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
tot_customer_cr_after_ds.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
tot_customer_dr_after_ds.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
"""

print("REACHED END OF PORGRAM")