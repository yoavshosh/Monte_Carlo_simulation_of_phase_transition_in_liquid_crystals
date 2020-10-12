"""
This file define the parameters for the Monte Carlo simulation of the Onsager model for the nematic-isotropic phase transition
please read the user guide for more information about the programm and the parameters
you can also contact shoshan.yoav@gmail.com for more information
"""

rods_n = 1000 #number of rods in the system
rod_l = 5 #length of each rod
iterations = 1000 # number of iterations of the metropolis process for each simulation


factor_sd_normal = 0.1 #see description bellow
"""
this factor determine the SD of the normal distribution 
based on which rod's locations are being change in the metropolis process
the SD will be calculated as follows:
sd_normal = factor_sd_normal*(Lx+Ly)/2
"""


Lx_arr = [10,40,100]  #vlaues for horizontal dimention of the she system size
Ly_arr = [10,40,100]  #vlaues for vertical dimention of the she system size
"""
IMPORTANT NOTE: Lx_arr and Ly_arr must contain the same number of elements
for the i'th simulation (system with a defined concentration) the system vol will be: 
V = Lx_arr[i]*Ly_arr[i]
the concentration of the system wil be calculated as follows:
C = rods_n/V
the program will iterate over the values of those to arrays together 
and for each iteration will start a the Monte Carlo simulation
"""


