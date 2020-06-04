# -*- coding: utf-8 -*-
"""

@author: Richard Vachula
"""
##SETUP
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
directory = 'C:/Users/Richard Vachula/Dropbox/Source area methodology'
os.chdir(directory)


### Model Code
sourceareas=np.zeros((1,1))
particles=np.zeros((1,1))
unknowns=np.zeros((1,1))

sourcearea=np.array([10])

runs=100000


while len(sourceareas)<runs:
    #particle=random.uniform(150,250)
    particle=random.lognormvariate(1,20)
    
    if 1<=particle<=10000:
        
        applier=random.randint(1,32)
        
        while applier>0:
            
            #Clark et al. 1998
            if applier==1:
                if particle>=180:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(0.06),num=10000)
                    which=random.randint(0,9999)
                    sourcearea=sourcearealist[which]
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Leys et al. 2015
            if applier==2:
                if 125<=particle<=1000:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(5.0),num=10000)
                    which=random.randint(0,9999)
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Lynch et al. 2004
            if applier==3:
                if particle>=180:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(0.08),num=10000)
                    which=random.randint(0,9999)
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Ohlson and Tryterund 2000
            if applier==4:
                if 500<=particle<=2000:
                    sourcearea=np.array([0.1**random.betavariate(1,3)])
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(0.1),num=10000)
                    which=random.randint(0,9999)
                    sourcearea=sourcearealist[which]                    
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)                

            if applier==5:                
                if particle>=2000:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(0.1),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Pisaric 2002
            if applier==6:
                if 2000<=particle<=7000:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(20.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Tinner et al. 2006
            if applier==7:
                if 1000<=particle<=10000:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(5.3),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)    
            #Adolf et al. 2018
            if applier==8:
                if 10<=particle<=500:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(40.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            if applier==9:                
                if particle>=100:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(40.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)                
            #Oris et al. 2014
            if applier==10:
                if particle>=150:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(32.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)   
            #Li et al. 2017
            if applier==11:
                if particle<=500:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(5.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)    
            #Aleman et al. 2013
            if applier==12:
                if particle>=160:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(5.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)    
            #Enache and Cumming 2006
            if applier==13:
                if particle>=150:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(20.0),num=10000)
                    which=random.randint(0,999)                    
                    sourcearea=sourcearealist[which]
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)               
            #Kelly et al 2013
            if applier==14:
                if particle>=180:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(20.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)    
            #MacDonald et al 1991
            if applier==15:
                if particle>=8.66:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(120.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)                
            #Miller et al 2017
            if applier==16:
                if particle>=125:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(80.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)    
            #Tinner et al 1998
            if applier==17:
                if particle>=8.66:
                    sourcearealist=np.logspace(np.log10(20.0),np.log10(50.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)                
            #Gavin et al 2003
            if applier==18:
                if 150<=particle<=500:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(0.5),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)    
            #Higuera et al 2010
            if applier==19:
                if 125<=particle<=250:
                    sourcearealist=np.logspace(np.log10(6.0),np.log10(51.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
      
            #Duffin et al 2008
            if applier==20:
                if particle>50:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(5.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)                    
                
            if applier==21:                
                if particle<=50:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(15.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle]) 
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Gardner and Whitlock 2010
            if applier==22:
                if particle>=125:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(3.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
            #Leys et al 2017
            if applier==23:
                if 60<=particle<=1000:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(1.06),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
        
            #Whitlock and Millspaugh 1996
            if applier==24:
                if 125<=particle<=250:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(13.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            #Vachula et al. 2020
            if applier==25:
                if 120<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(102.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)

            if applier==26:                    
                if 125<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(76.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)                    

            if applier==27:                    
                if 150<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(156.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0     
                else:
                    applier=random.randint(1,32)                    

            if applier==28:                    
                if 180<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(149.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0  
                else:
                    applier=random.randint(1,32)                    
                    
            if applier==29:                    
                if 250<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(24.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0                 
                else:
                    applier=random.randint(1,32)

            #Vachula et al. 2018
            if applier==30:
                if 63<=particle<=150:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(150.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)

            if applier==31:
                if 150<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(35.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)
                    
            if applier==32:
                if 250<=particle:
                    sourcearealist=np.logspace(np.log10(0.01),np.log10(25.0),num=10000)
                    which=random.randint(0,9999)                    
                    sourcearea=sourcearealist[which]                    
                    sourceareas=np.append([sourceareas],[sourcearea])
                    particles=np.append([particles],[particle])
                    applier=0
                else:
                    applier=random.randint(1,32)


##END of LOOPS


##Analysis
sourceareas=sourceareas[1:runs]
particles=particles[1:runs]
plt.loglog(particles,sourceareas,'r.')
plt.axis([1, 10000, 0.01, 10**2.5])


fig, ax = plt.subplots()
#ax.hist2d(particles, sourceareas, bins=1000, cmap='Blues')
h=ax.hist2d(particles, sourceareas, bins=[np.logspace(np.log10(1),np.log10(10000)),np.logspace(np.log10(.01),np.log10(1000))], cmap='Reds')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim([0.01,10**2.5])
ax.set_xlim([1,10000])
plt.colorbar(h[3],ax=ax)
plt.xlabel('Charcoal Size (um)')
plt.ylabel('Source Area or Dispersal Distance (km)')
plt.savefig('modelledsourcearea_log.jpeg',dpi=600)

fig2, ax2 = plt.subplots()
#ax.hist2d(particles, sourceareas, bins=1000, cmap='Blues')
h2=ax2.hist2d(particles, sourceareas, bins=[np.logspace(np.log10(1),np.log10(10000)),np.logspace(np.log10(.01),np.log10(1000))], cmap='Reds')
ax2.set_xscale('log')
ax2.set_ylim([0.01,150])
ax2.set_xlim([1,10000])
plt.colorbar(h2[3],ax=ax2)
plt.xlabel('Charcoal Size (um)')
plt.ylabel('Source Area or Dispersal Distance (km)')
plt.savefig('modelledsourcearea_linear.jpeg',dpi=600)



plt.figure()
plt.hist(particles, bins=np.logspace(np.log10(1),np.log10(10000), 50))
plt.gca().set_xscale("log")


plt.show();

