# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:11:19 2023

@author: celin
"""

import lunaSolver as lunsol
import matplotlib.pyplot as plt
import numpy as np

#plt.ion()

sol = lunsol.Solver()

sol.out_filepath = 'Output/IK'
sol.in_filename = 'input_IK.in'

### CALCULATE NEW EIGENVALUES OR NOT? ###
#sol.initialisers['RunVMEC'] = True

runVENUS = True
if runVENUS == False:
    out_filename = '0xf3cff5.npz'
else:
    out_filename = 'blah.npz'    
out_file = f'{sol.out_filepath}/{out_filename}'


sol.initialisers['ToPlot'] = False

### LOAD DATA ###
data = sol.getData(dataFile = out_file, runSol = runVENUS)

### PLOT DATA ###
plotEigs = True
plotEigGuess = False

if plotEigs:
    ws = data['eigenvals']
    gams = [i.real for i in ws]
    if data['scanparams'] == 'mach':
        x = data['v0vas']
        xlabel = 'v0/va'
        """ # for kh-like instability
        profparams = data['profparams'].item()
        params = data['params'].item()
        
        eps_a = params['r0']/params['R0']
        beta = [i/eps_a**2 for i in profparams['beta0']]
        mach = data['scanvals']
        Omega = [np.sqrt(i*j) for i, j in zip(mach, beta)]
        
        x = Omega
        xlabel = data['scanparams']
        """
    else:
        x = data['scanvals']
        xlabel = data['scanparams']
    
    fig, ax = plt.subplots()
    ax.plot(x, gams, '-x')
    if plotEigGuess:
        wsguess = data['eigenguesses']
        gamguess = [i.real for i in wsguess]
        ax.plot(x, gamguess, '-x', label='EV guess')
    ax.set_ylabel('gamma')
    ax.set_xlabel(f'{xlabel}')
    ax.set_title(f'{sol.VMEClabel}') # not perfect
    if runVENUS == False:
        ax.set_title(f'{out_filename}'.replace('.npz',''))
    plt.grid()
    plt.legend()
    plt.show()
    

### GET SINGLE RUN PLOTS ###
# Get plots with profiles and eigenfunctions etc
# Need to find a way to do this without re-running the eigenfunction guess
# Also this loads default parameters for IdealMHDFlow-Euler model?
plotSingle = False
if plotSingle:
    sol.VMEClabel = '0xf3cff5'
    sol.initialisers['ToPlot'] = True
    sol._runVENUS(labelnr=0)
    

