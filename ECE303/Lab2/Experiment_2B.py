# Experiment 1B-Resistor estimation lab - USB and GPIB
import visa
import numpy as np
import time as time
import matplotlib.pyplot as plt


# File to save data
filename = 'experiment2b.csv'

# Equipment Addresses
awg_address = 'USB0::0x0957::0x0407::MY44043483::0::INSTR'
scope_address = 'USB0::0x0957::0x1799::MY58100820::INSTR'  # OscilloscopeAddress

# Min and Max Voltages
V_min = 0
V_max = 5

# Voltages to awg
V = np.linspace(V_min, V_max, 50)

# Equipment Setup
rm = visa.ResourceManager()
awg = rm.open_resource(awg_address)
scope = rm.open_resource(scope_address)

# Set awg to high z
awg.write("OUTP:LOAD INF")

volts_per_division = 2  # ScopeVoltsperdivision
time_range = 3E-3  # Scopetimerange( s)

numpoints = 5000

# Initialize measurement vectors
freq = np.zeros(len(V))


# Set up wave form generator

cmd_str = "APPL:DC DEF , DEF, " + "0"
awg.write(cmd_str)

# Setup oscilloscope
scope.values_format.is_binary = False
scope.values_format.datatype = ' f'
scope.values_format.is_big_endian = True
scope.values_format.container = np.array;
scope.write(":CHANNEL1:RANGE " + str(8 * volts_per_division))
scope.write(":TIMEBASE:MODENORMAL; RANGE" + str(time_range))
scope.write(":AUTOSCALE; ")
scope.write("WAV:SOUR CHAN1")
scope.write("WAV:FORM ASC;")
scope.write("WAV:POINTS:MODE RAW")
tempstr = "WAV:POIN " + str(numpoints)
scope.write(tempstr)
scope.write(":WAVEFORM:BYTEORDER LSBFIRST")
scope.write(":TRIG:EDGE:SOUR CHAN1")
scope.write(":TRIG:EDGE:LEV 0.4")

# ---------------------
#
# Conduct Measurments

count = 0
for I in V:
    print("AWG DC Voltage %d".format(I))

    # Command awg
    volt_str = "VOLT:OFFS " + str(I)
    awg.write(volt_str)

    scope.write("DIG CHAN1;")
    operationComplete = bool(scope.query("*OPC?"))
    while not operationComplete:
        operationComplete = bool(scope.query("*OPC?"))

    # Give 5 seconds for arduino stablize
    time.sleep(5)

    # data = scope.query("WAV:DATA?")
    # temp = data[10:-1]
    # temp = temp.split(',')
    # temp = np.array([float(x) for x in temp])

    # Measure Frequency
    freq[count] = scope.query(":MEAS:FREQUENCY? CHAN1")

    print("Frequency = %d".format(freq[count]))

    # signals[:, count] = temp

    count = count + 1


# ---------------------
#
# Data Analysis


# Write data to file
data = np.append(freq, axis=1)
np.savetxt(filename, data, delimiter=' , ')



# # Plot Frequency
# plt.plot(freq, markersize=4)
#
# plt.xlabel("Input (ms) ")
# plt.ylabel("Frequency (V) ")
#
# plt.title("PWM Signal Analysis")
# plt.grid(True)
# plt.show()
