# The project aims to propose a network to extract spectral function from correlator

## problem description:

There is a well known relation correlator G with spectral function $\rho$:

<img src="https://github.com/Chern2/Network-approach-to-extract-spectral-function-from-correlator-/blob/master/image/correlator_spectral.png" width = "350" height = "40"/>

where:

<img src="https://github.com/Chern2/Network-approach-to-extract-spectral-function-from-correlator-/blob/master/image/kernel_function.png" width = "200" height = "30"/>

The correlator from experiment carries noise, and normally has data points less than hundreds, and we want to obtain spectral function more that thousands. Thus, it is traditional ill-posed problem.

## Training sample construction:

 Training samples are constructed by two different formulas base on different channel and temperature. And they are listed following:

<img src="https://github.com/Chern2/Network-approach-to-extract-spectral-function-from-correlator-/blob/master/image/training_function.png" width = "350" height = "120"/>

 where:

<img src="https://github.com/Chern2/Network-approach-to-extract-spectral-function-from-correlator-/blob/master/image/zheta_function.png" width = "200" height = "40"/>

  The parameters within functions above are listed in table:

<img src="https://github.com/Chern2/Network-approach-to-extract-spectral-function-from-correlator-/blob/master/image/sample_parameters.png" width = "350" height = "125"/>

For example, the $\hat{\rho}_{below}$ look like:

<img src="https://github.com/Chern2/Network-approach-to-extract-spectral-function-from-correlator-/blob/master/image/training_sample.png" width = "250" height = "250"/>

## Network hyper-parameters and training sample  parameters setting：

Network hyper-parameters and training sample  parameters are free to change. All are listed in file parameter.py, so you can change setting base on your need.   
