# phasefreq
 Phase-frequency discriminator PCB

## Design goals

* Simple, connectorized element to replace an analog mixer in rf test setups
* Requires only dc power to operate (no programming)
* 10 MHz, ideally 100 MHz bandwidth (10 MHz is reasonable without impedance control in fabrication)
* Accommodate analog input (Analog ADCMP564 comparator, with settable threshold and hysteresis)
* Perform PFD calculation (Analog AD9901, ECL logic family)
* Low-pass filter to convert PFD output pulse train's duty cycle to a dc voltage
* Tunable output offset, jumper-switchable sign of gain

## What is a PFD?

A phase-frequency discriminator is similar to an analog mixer, in that if the lo and rf frequencies are the same, its output is proportional to the relative phase between them. However, if the lo and rf frequencies differ, a PFD will output a constant voltage whose sign indicates which of the two frequencies is larger. In this case, an analog mixer would produce IF beatnotes at the sum and difference frequencies. This second characteristic of a PFD is useful to more quickly bring a frequency-feedback system into lock.

## Other options?

More sophisticated PLL ICs contain builtin PFDs as part of the feedback loop. Some evaluation boards expose enough functionality to use them solely as a PFD, but they are prohibitively expensive for many applications where a simple PFD would be beneficial, and often need to be programmed or initialized at the point of use.

