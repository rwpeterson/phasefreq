# phasefreq
 Phase-frequency detector PCB built around the AD9901

## Design goals

* Simple, connectorized element to replace an analog mixer in rf test setups
* Requires only dc power to operate (no programming)
* 10 MHz, ideally 100 MHz bandwidth (10 MHz is reasonable without impedance control in fabrication)
* Accommodate analog input (Analog ADCMP564 comparator, with settable threshold and hysteresis)
* Perform PFD calculation (Analog AD9901 phase-frequency discriminator, ECL logic family)
* Low-pass filter to convert PFD output's pulse train duty cycle to a dc voltage
* Tunable output offset, jumper-switchable sign of gain
* This is basically a subset of the reference design in Fig. 12 of the [AD9901 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/AD9901.pdf), which describes a complete PLL circuit with discrete comparator, PFD, VCO, divider, etc. Here we wish to implement only the comparator, phase-frequency detector, and loop filter

## What is a PFD?

A phase-frequency detector (or phase-frequency discriminator) is similar to an analog mixer, in that if the LO and RF frequencies are the same, its output is proportional to the relative phase between them. However, if the LO and RF frequencies differ, a PFD will output a constant voltage whose sign indicates which of the two frequencies is larger. In this case, an analog mixer would produce IF beatnotes at the sum and difference frequencies. This second characteristic of a PFD is useful to more quickly bring a feedback system such as a PLL into lock.

## Other options?

Of course, an analog mixer may be perfectly suitable for your application. More sophisticated PLL ICs contain builtin PFDs as part of the feedback loop. Some evaluation boards expose enough functionality to use them solely as a PFD, but they are prohibitively expensive for many applications where a simple PFD would be beneficial, and often need to be programmed or initialized at the point of use.

## Characterization

![Figure 1](doc/bidirectional-phase.png?raw=true)
### Figure 1: Bidirectional phase sweep (RF and LO at 10 MHz)
Scanning the relative phase of the inputs demonstrates the linear phase detection and capture range. The location of the linear phase detection is modulo 2 pi as expected. However, when the phase is scanned away from a given phase detection range, the IF output will rail for one additional phase cycle before phase-slipping to the *second* capture range 4 pi away (as shown). For frequencies > 50 MHz, the ends of the phase detection range will be distorted (see AD9901 datasheet, Fig. 7).

![Figure 2](doc/frequency-sweep.png?raw=true)
### Figure 2: Frequency discrimination characteristic, LO = 10 MHz
When the RF and LO frequencies differ substantially, the PFD outputs a constant voltage indicating which is higher.

## Prototype

![Prototype](doc/prototype.jpg?raw=true)
### Figure 3: revB1 prototype in 3D-printed case (lid removed)
This is the device used for the above characterization plots.
