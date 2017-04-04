# Load libraries
import pandas
import csv
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


# Read the file and store the read file in a variable
f_reader1=file('After_Dr/Cr_Report.csv','r')
f_config1=file('config1.properties','r')
f_config2=file('config2.properties','r')
f_config3=file('config3.properties','r')

f_check=csv.reader('f_reader1')
f_configFile_reader1=csv.reader('f_config1')
f_configFile_reader2=csv.reader('f_config2')
f_configFile_reader3=csv.reader('f_config3')

# Write our output in a file
f_writeLow=file('abnormal_report1.csv','w')
f_writeToLow=csv.write(f_writeLow)
f_writeMedium=file('abnormal_report2.csv','w')
f_writeToMedium=csv.write(f_writeMedium)
f_writeHigh=file('abnormal_report3.csv','w')
f_writeToHigh=csv.write(f_writeHigh)


# for loop 1 for Low Salaried Customer
for l_all_data in f_check:
	l_abnormal=False
	for l_configurableFile in f_configFile_reader1:
		l_check_abnormal=all_data
		if l_all_data[3] <= l_configurableFile[0] AND l_all_data[3] >= l_configurableFile[3]:
			check_abnormal.append('Abnormal')
			l_abnormal=True
			break
	if not l_abnormal:
		l_check_abnormal.append('Normal')
	f_writeToLow.writerow(l_check_abnormal)
	
# for loop 1 for Medium Salaried Customer
for m_all_data in f_check:
	m_abnormal=False
	for m_configurableFile in f_configFile_reader2:
		m_check_abnormal=m_all_data
		if m_all_data[3] <= m_configurableFile[3]:
			m_check_abnormal.append('Abnormal')
			m_abnormal=True
			break
	if not m_abnormal:
		m_check_abnormal.append('Normal')
	f_writeToMedium.writerow(m_check_abnormal)
	
	
	
