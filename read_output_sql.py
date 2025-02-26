import openmdao.api as om
import matplotlib.pyplot as plt
import numpy as np

#%% utility function
def load_OMsql(log):
    print('loading {}'.format(log))
    cr = om.CaseReader(log)
    rec_data = {}
    driver_cases = cr.list_cases('driver')
    cases = cr.get_cases('driver')
    for case in cases:
        for key in case.outputs.keys():
            if key not in rec_data:
                rec_data[key] = []
            rec_data[key].append(case[key])
        
    return rec_data

#%%

# rec_data = load_OMsql('opt_output/log_iea15mw_umaine.sql')
# rec_data = load_OMsql('iea15MW_output/opt_output/log_iea15mw_umaine.sql')
rec_data = load_OMsql('iea15MW_output_Raft/opt_output/log_iea15mw_umaine.sql')
for key in rec_data:
    if 'rec_data' in key:
        print(key)

ptfmMass_vec=np.squeeze(rec_data['floatingse.platform_mass'])
plt.figure()
plt.scatter(np.arange(len(ptfmMass_vec)),ptfmMass_vec)
plt.scatter(0,ptfmMass_vec[0], color='k')
plt.scatter(len(ptfmMass_vec),ptfmMass_vec[-1], color='r')
plt.ylabel('ptfmMass (kg)')
plt.xlabel('Iteration')
plt.grid()

LCOE_vec=np.squeeze(rec_data['financese.lcoe'])
plt.figure()
plt.scatter(np.arange(len(LCOE_vec)),LCOE_vec)
plt.scatter(0,LCOE_vec[0], color='k')
plt.scatter(len(LCOE_vec),LCOE_vec[-1], color='r')
plt.ylabel('LCOE_vec ($/kWh)')
plt.xlabel('Iteration')
plt.grid()

# test modifica
# nuovo test -- remoto


