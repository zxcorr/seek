# SEEK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SEEK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SEEK.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on October 1, 2018

author: Lucas Olivari
'''

import numpy as np
import os
import seek

####################################################################
#### THIS IS THE SCRIPT THAT WILL RUN HIDE FOR EACH HORN
####################################################################

# ==================================================================
# CHOOSE NUMBER OF HORNS
# ==================================================================

number_horns = 28

# ==================================================================
# CHOOSE BINGO MODEL
# ==================================================================

bingo_model = 0 # either 1 or 2

# ==================================================================
# CHOOSE DESTINATION AND WORKING PATHS
# ==================================================================

destination_path = os.path.join(seek.__path__[0], '/seek/config/') #"/usr/local/lib/python2.7/dist-packages/seek-0.1.0-py2.7.egg/seek/config/" #'~/anaconda2/lib/python2.7/site-packages/seek-0.1.0-py2.7.egg/seek/config/' # change to your destination (the place where your hide package is located within your python repository)
output_path = "/scratch/bingo/joao.barretos/hide_and_seek/resultados/healpix/256_128/zernike_auto_150_MINUS110_nearest/"
working_path = os.getcwd() + "/seek/config/"   # change to your working path

# ==================================================================
# SETTING THE CONFIG FILES FOR EACH HORN
# ==================================================================

dfile_short = 'bingo_horn'

for i in range(0, number_horns):
    destination = open(working_path + 'bingo_horn_' + str(i) + '.py', 'w')
    source = open(working_path + 'bingo.py', 'r')
    for line in source:
        if line == 'map_name\n':
            destination.write('map_name = "'+ output_path + 'bingo_maps_horn_' + str(i) + '.hdf"' + '\n')    
            #destination.write('map_name = "bingo_maps_horn_' + str(i) + '.hdf"' + '\n')
                             # map file name for each horn -- output

        elif line == 'params_file_fmt\n':
            destination.write('params_file_fmt = "params_bingo_' + str(i) + '_' + '{}.txt"' + '\n') 
                             # params file name for each horn

        elif line == 'data_file_prefix\n':
            destination.write('data_file_prefix = "bingo_tod_horn_' + str(i) + '_"' + '\n') 
                             # tod file name for each horn -- input     

        elif line == 'coord_prefix\n':
            destination.write('coord_prefix = "coord_bingo_' + str(i) + '_"' + '\n') 
                             # coordinates file name for each horn -- input

        elif line == 'gain_file_default\n':
            destination.write('gain_file_default = "data/gain_template_fake_bingo_model_{}_{}.dat"\n'.format(bingo_model, i)) 
                             # gain template used for each horn
            
        else:
            destination.write(line)	
    source.close()
    destination.close()

# ==================================================================
# SETTING AND RUNNING SEEK
# ==================================================================

for i in range(0, number_horns):
    print("\nExecuting horn {}\n".format(i))
    os.system('cp ' + working_path + 'bingo_horn_' + str(i) + '.py' + ' ' + destination_path)	 
    os.system('seek seek.config.' + dfile_short + '_' + str(i)) # run seek
