# phasefreq
# plotgen for documentation
# Bob Peterson
# 2020-02-19

import numpy as np
import scipy as sp
import scipy.io as sio
import matplotlib.pyplot as plt

# Load phase scan data
bds = np.loadtxt(r"bidirectional-phase.txt", delimiter=';', skiprows=5)
bds_phase = bds.transpose()[0]
bds_ifvoltage = bds.transpose()[1]
# Split phase scan data into ltr and rtl sweeps so we can plot separately
split = bds_phase.size // 2
bds_phase_ltr = bds_phase[:split]
bds_phase_rtl = bds_phase[split:]
bds_ifvoltage_ltr = bds_ifvoltage[:split]
bds_ifvoltage_rtl = bds_ifvoltage[split:]

# Load frequency sweep data
fqs = np.loadtxt(r"frequency-sweep.txt", delimiter=';', skiprows=5)
fqs = fqs[:-1].T #note that [:-1] grabs all but the last point, which is the frequency limit of the instrument and behaves erratically

# Generate phase scan figure
fig1 = plt.figure()
# First subplot of the ltr scan
plt.subplot(211)
plt.plot(bds_phase_ltr, bds_ifvoltage_ltr, 'b-', label=r'$\rightarrow$')
plt.ylabel('IF voltage (V)')
plt.grid(True)
plt.xticks(np.arange(-1080,1081,360),['$-6\pi$','$-4\pi$','$-2\pi$','$0$','$2\pi$','$4\pi$','$6\pi$'])
plt.xlim(-1170,1170)
plt.ylim(-0.1,2.3)
plt.title('Bidirectional phase sweep')
plt.legend()
# Second subplot of the rtl scan
plt.subplot(212)
plt.plot(bds_phase_rtl, bds_ifvoltage_rtl, 'g-', label=r'$\leftarrow$')
plt.xlabel('RF input phase, relative to LO (deg)')
plt.ylabel('IF voltage (V)')
plt.grid(True)
plt.xticks(np.arange(-1080,1081,360),['$-6\pi$','$-4\pi$','$-2\pi$','$0$','$2\pi$','$4\pi$','$6\pi$'])
plt.xlim(-1170,1170)
plt.ylim(-0.1,2.3)
plt.legend()
plt.tight_layout()
plt.savefig('bidirectional-phase.png')
plt.close(fig1)

# Generate frequency sweep figure
fig2 = plt.figure(figsize=(6.4,3.5))
plt.plot(fqs[0],fqs[1])
plt.semilogx()
plt.xlim(0.9*1e6,50e6/0.9)
plt.xticks([1e6,10e6,50e6],[1,10,50])
plt.xlabel('RF frequency (MHz)')
plt.ylim(-0.1,2.3)
plt.yticks([0,0.5,1,1.5,2])
plt.ylabel('IF voltage (V)')
plt.title('Frequency discrimination')
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig('frequency-sweep.png', dpi=300, bbox_inches='tight')
plt.close(fig2)
