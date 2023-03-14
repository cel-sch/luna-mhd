# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:11:19 2023

@author: celin
"""
import lunaSolverNoEigGuess as lunsol
import matplotlib.pyplot as plt

#plt.ion()

sol = lunsol.Solver()

sol.out_filepath = 'Output/IK'
sol.in_filename = 'input_IK.in'

### CALCULATE NEW EIGENVALUES OR NOT? ###
#sol.initialisers['RunVMEC'] = True
runVENUS = True
out_filename = '0xb93661.npz'
out_file = f'{sol.out_filepath}/{out_filename}'

#sol.initialisers['ToPlot'] = True

### LOAD DATA ###
data = sol.getData(dataFile = out_file, runSol = runVENUS)

### PLOT DATA ###
plotEigs = True

if plotEigs:
    ws = data['eigenvals']
    gams = [i.real for i in ws]
    if data['scanparams'] == 'mach':
        x = data['v0vas']
        xlabel = 'v0/va'
    else:
        x = data['scanvals']
        xlabel = data['scanparams']
    
    fig, ax = plt.subplots()
    ax.plot(x, gams)
    ax.set_ylabel('gamma')
    ax.set_xlabel(f'{xlabel}')
    
    plt.show()
    

"""
### GET SINGLE RUN PLOTS ###
plotSingle = False

if plotSingle:
    sol.VMEClabel = '0x686720'
    sol.initialisers['ToPlot'] = True
    sol._runVENUS(labelnr=5)
"""
