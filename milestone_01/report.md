# Milestone 01 Report

### Summary of Progress
This week team Ruby Brown made some exciting progress! 
We successfully completed the ADC/DAC lab (in place of the I2C lab - 
thank you for the permission to switch due dates for those), 
which enabled us to record and read in values from both our whiskers and light sensors. 
This was an essential step to ensure that our homemade whiskers would give us reproducibly different data: 
i.e. that a bent state (indicating sensing an obstacle) and relaxed state (indicating no obstacle) 
would create measurably diverging values. Below we have analyzed and documented the collected data itself,
as well as the process and techniques utilized to produce it. We feel confident that our homemade whiskers
do indeed produce differing values according to their different states (after applying a filter), but note that calibration prior to 
each sensing run will be critical for proper performance. Indeed, we may switch to 

In addition to setting up a system to capture our sensor data, we assembled our motors, wheels, and encoders 
onto our chassis. A photo of this is also included below. 

### Reading in sensor data
Both the ADC and UART labs were critical for collecting our sensor data. At a high level, 
we used our ADC lab code with some minor modifications (namely, we used a larger 12-bit depth to increase sensitivity)
to read in the data, as well as the UART lab code to write out the data to a CSV file. We then performed a simple
t-test to ensure that our measured values for different states were significantly different.

#### Whisker sensing specifics
To read in our whisker data, we constructed homemade whiskers (rectangular pieces of computer paper 
with graphite traces drawn on them) of varying lengths, with alligator clips connected to the
ends of the graphite trace reading into the STM32 Discovery board. A schematic of this can be seen in Fig 1.
*JACK EDIT THIS A BIT AND ADD SCHEMATIC* 

Fig 1

*BROCK ADD IN HOW THE UART WORKS* You can see the raw data in this directory {filename.csv}. 
We additionally performed a simple t-test to see if our values were significantly different. 
*STEPH DO T-TEST AND ADD FIGURES HERE*

#### Light sensing specifics
*ALL OF US TO DO*

*ALL OF US ADD CODE TO DIR*