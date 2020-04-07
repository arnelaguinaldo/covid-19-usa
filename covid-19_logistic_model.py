import matplotlib.pyplot as graph
import numpy as np
import pandas as pd
import scipy.optimize as opt
  
# --------------------------------------------------------------------
# Logistic growth model to predict COVID-19 prevalence and
# incidence rate using existing data from John Hopkins University and
# New York Times Github (https://github.com/nytimes/covid-19-data)
# 
# Written Arnel Aguinaldo, PhD (Point Loma Nazarene University)
# Applicable rights for free reproduction of this program are defined in
# MIT License
# --------------------------------------------------------------------

# growth rates (vary by region)
b0 = 0.20   #full exposure
b1 = 0.12   #60% exposure due to mitigation measures (i.e., social distancing)
b2 = 0.08   #40% exposure due to mitigation measures (i.e., social distancing)

# population max 
Nmin=1
Nmax=10000
a=(Nmax-Nmin)/Nmin
dt=1

# time interval
t=np.arange(1,120,2)

# infection prevalence (total infected per day)
def n0(t):
    return Nmax/(1+a*np.exp(-b0*t))
def n1(t):
    return Nmax/(1+a*np.exp(-b1*t))
def n2(t):
    return Nmax/(1+a*np.exp(-b2*t))

# infection incidence rates (number of new cases per day)
def r0(t):
    return (n0(t)-n0(t-1))/dt
def r1(t):
    return (n1(t)-n1(t-1))/dt
def r2(t):
    return (n2(t)-n2(t-1))/dt
    
# graph style
graph.style.use('seaborn-talk')

# Prevalence plot
graph.figure(1)
graph.plot(t, n0(t),'b', t, n1(t), 'r', t, n2(t), 'g') 
graph.xlabel('Days') 
graph.ylabel('Prevalence (Total Cases)') 
graph.legend([ 'Full Exposure','60% Exposure', '40% Exposure'])  
graph.title('COVID19') 
graph.grid('true')

# Incidence rate plot
graph.figure(2)
graph.plot(t, r0(t),'b', t, r1(t), 'r', t, r2(t), 'g') 
graph.xlabel('Days') 
graph.ylabel('Incidence Rate') 
graph.legend([ 'Full Exposure','60% Exposure', '40% Exposure'])  
graph.title('COVID19') 
graph.grid('true')
  
graph.show() 

#Day 5 and 30 prevalence by exposure
#Full exposure
print(n0(5), n0(30))
#60% exposure
print(n1(5), n1(30))
#40% exposure
print(n2(5), n2(30))

# ----------------------------------------------------------
# Fit logistic model to real data (USA or state)
# ----------------------------------------------------------

#import case data (update with the local path of the csv file)
sPath='total-cases-covid=19-04052020.csv'
alldata=pd.read_csv(
        sPath, 
        sep=',',
        usecols=['Days', 'California']
        )
alldata.head()
alldata=alldata.dropna()

#logistic function to be fitted
def r(t,a,b,c):
    return c/(1+a*np.exp(-b0*t))

# initialize coefficients using known or random values
#init_guess = [1, 1.5, Nmax]   
init_guess = np.random.exponential(size=3)
    
# set array bounds (adjust according to region or target population)
bounds = (0, [1000., 0.5, 100000.])

t = np.array(alldata['Days']) + 1
y = np.array(alldata['California'])

# real infection rate
rate = (y[1:]-y[:-1])        #daily incidence (growth)
t_max = t.size

# ----------------------------------------------------------
# Logistic model to predict prevalence (total cases)
# ----------------------------------------------------------

#non-linear optimization to estimate best fit model on case data
#uncomment next line to find best fit with new regional data
#(a,b,c),covar = opt.curve_fit(r, t, y, bounds=bounds, p0=init_guess)

#BEST FIT FOR CALIFORNIA PREVALENCE (r^2=0.992): 
(a,b,c)=(234.7722, 0.2414, 19362.9526)

# time intervals
tn=np.arange(1,40,2)
tr=np.arange(1,t_max)

# fitted infection prevalence (total infected per day)
def n_lg(tn):
    return c/(1+a*np.exp(-b*tn))

# prevalence plot
graph.figure(1)
graph.scatter(t,y)
graph.plot(tn, n_lg(tn), 'r') 
graph.xlabel('Days') 
graph.ylabel('Prevalence (Total Cases)') 
graph.legend([ 'Model','California'])  
graph.title('COVID19') 
graph.grid('true')

# ----------------------------------------------------------
# Logistic model to predict incidence (daily growth) rate
# ----------------------------------------------------------

y=rate

#non-linear optimization to estimate best fit model on daily rate
#uncomment next line to find best fit with new regional data
#(a,b,c),covar = opt.curve_fit(r, tr, y, bounds=bounds, p0=init_guess)

#BEST FIT FOR CALIFORNIA INCIDENCE (r^2=0.812): 
(a,b,c)=(204.7359, 0.2551, 3021.3831)
    
def rate_lg(tr):
    return c/(1+a*np.exp(-b*tr))

# Incidence rate (%) plot
graph.figure(2)
graph.scatter(tr,rate)
graph.plot(tr, rate_lg(tr), 'r') 
graph.xlabel('Days') 
graph.ylabel('Incidence Rate') 
graph.legend([ 'Model','California']) 
graph.title('COVID19') 
graph.grid('true')

