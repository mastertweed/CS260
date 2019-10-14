
# Experiment1C-OscilloscopeDataLab
import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt

# Input values

awg_address = 'USB0::0x0957::0x0407::MY44043465::INSTR'  # WaveformGenerator Address# WaveformGeneratorAddress
scope_address = 'USB0::0x0957::0x1799::MY58100820::INSTR'  # OscilloscopeAddress

pulse_frequency = 1400  # pulse_frequency(Hz)
pulse_amplitude = 5  # pulse_amplitude(V)
volts_per_division = 2  # ScopeVoltsperdivision
time_range = 3E-3  # Scopetimerange( s)
duty_cycle = np.linspace(20, 80, 13)  # Dutycyclevector(%)
numpoints = 5000
filename = 'experiment1c.csv'  # Filenamefordataoutput

# Initialize important matrices
num_dc = duty_cycle.size  # Numberofdutycycletrials
freq = np.zeros(num_dc)
signals = np.zeros((numpoints, num_dc))
times = np.zeros(numpoints)

# Initiate communications with and open instruments
rm = visa.ResourceManager()
awg = rm.open_resource(awg_address)
scope = rm.open_resource(scope_address)

# Place waveform generator in High-Z
awg.write("OUTP:LOADINF")

# Set up wave form generator
freq_str = str(pulse_frequency)
amp_str = str(pulse_amplitude)
offset_str = str(pulse_amplitude / 2)
cmd_str = "APPL:SQU" + freq_str + " , " + amp_str + " , " + offset_str
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

# Conduct Measurements
count = 0
for I in duty_cycle:
    print("DutyCycle%i%c" % (I, '%'))
    pulse_str = "PULSE:DCYC " + str(I)
    awg.write(pulse_str)
    scope.write("DIG CHAN1;")
    operationComplete = bool(scope.query("*OPC?"))
    while not operationComplete:
        operationComplete = bool(scope.query("*OPC?"))

    time.sleep(1)

    data = scope.query("WAV:DATA?")
    temp = data[10:-1]
    temp = temp.split(',')
    temp = np.array([float(x) for x in temp])
    freq[count] = scope.query(":MEAS:FREQUENCY? CHAN1")
    signals[:, count] = temp
    count = count + 1

# Break up the preamble block
preambleBlock = scope.query(":WAVEFORM:PREAMBLE?")
preamble = preambleBlock.split(",")
dt = float(scope.query(":WAV:XINC?"))
t0 = float(scope.query(":WAV:XOR?"))
dV = float(scope.query("WAV:YINC?"))
V0 = float(scope.query(":WAV:YOR?"))
V_ref = float(scope.query(":WAV:YREF?"))

# Convert to use fuldata
times = (np.linspace(0, numpoints - 1, numpoints)).dot(dt) + t0

# volts = ((signals - Vref)).dot(dV) + V0
volts = signals

# Write data to file
data = np.append(np.transpose([times]), volts, axis=1)
np.savetxt(filename, data, delimiter=' , ')

# Plot Signals vs. Voltage
plt.plot(times * 1000, volts, markersize=4)
plt.xlabel("Time(ms) ")
plt.ylabel(" Voltage(V) ")
plt.title("PWM Signal Analysis")
plt.grid(True)
plt.show()  # Makeplotvisible