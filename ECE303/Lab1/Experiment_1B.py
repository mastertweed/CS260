# Experiment 1B-Resistor estimation lab - USB and GPIB
import visa
import numpy as np
import time as time
import matplotlib.pyplot as plt

# rm = visa.ResourceManager()

# Input values
awg_address = 'USB0::0x0957::0x0407::MY44043483::0::INSTR'

dmm_address = 'USB0::0x2A8D::0xB318::MY58160107::0::INSTR'

V_min = 0
V_max = 10
N_Volts = 51
filename = 'experiment1b.csv'

V = np.linspace(V_min, V_max, N_Volts)
V1 = np.linspace(V_min, V_max, 10*N_Volts+1)
Imeas = np.zeros(N_Volts)

rm = visa.ResourceManager()
awg = rm.open_resource(awg_address)
dmm = rm.open_resource(dmm_address)

awg.write("OUTP:LOAD INF")

count = 0
for K in V:
    print("Applying %f Volts" % K)
    awg.write("APPL:DC DEF,DEF,%f" % K)
    time.sleep(1)
    Imeas[count] = dmm.query("MEAS:CURR:DC? 1e-1,1e-5")
    count = count+1


Rest = V.dot(V)/V.dot(Imeas)
Iest = V1/Rest

data = np.append(np.transpose([V]),np.transpose([Imeas*1000]),axis=1)
np.savetext(filename, data, delimiter=',')

plt.plot(V, Imeas*1000, 'bo', markersize=4, label='Measured')
plt.plot(V1, Iest*1000, 'r-', linewidth=2, label='Fitted')
plt.grid()
plt.legend()
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")
plt.title("Estimated Resistance = " + '{:.0f}'.format(Rest) + r' $\Omega$')
plt.show()