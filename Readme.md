# The project aims to propose a network to extract spectral function from correlator.

## problem description:

There is a well known relation correlator G with spectral function $\rho$:

```latex
\begin{equation}
G(\tau,T)=\sum_{x,y,z} 
%\exp(-i\vec{x}\cdot\vec{p}) 
\left\langle J_H(0,\vec{0})J^+(\tau,\vec{x}) \right\rangle_T=\int_0^\infty \!\frac{\mathrm{d}\omega}{2\pi}\ K(\tau, \omega,T) \rho(\omega),
\label{chapter1eq1}
\end{equation}

```

where $T$ is the temperature, and 

```latex
\begin{equation}
	K(\omega,\tau,T) = \frac{\cosh(\omega(\tau-\frac1{2T}))}{\sinh(\frac{\omega}{2T})},
	\label{chapter1eq10}
\end{equation}
```

The correlator from experiment carries noise, and normally has data points less than hundreds, and we want to obtain spectral function more that thousands. Thus, it is traditional ill-posed problem.

## Training sample construction:

 Training samples are constructed by two different formulas base on different channel and temperature. And they are listed following:

```latex
\begin{equation}
	\begin{aligned} 
		&\hat{\rho}_{below} = \sum\limits_{i=1}^{L} C_i\hat{\Theta}(\hat{\omega}, \delta_0, \zeta_0) \exp\left(-(\frac{M-\hat{\omega}}{V})^2\right)（1-\hat{\Theta}(\hat{\omega}, \delta_1, \zeta_1)) + C_0\hat{\Theta}(\hat{\omega}, \delta_2, \zeta_2) \\
		&\hat{\rho}_{above} = \sum\limits_{i=1}^{L} C_i\hat{\Theta}(\hat{\omega}, \delta_0, \zeta_0) \exp\left(-\frac{(M-\hat{\omega})^2}{V^2}\right)（1-\hat{\Theta}(\hat{\omega}, \delta_1, \zeta_1)) + C_0\hat{\Theta}(\hat{\omega}, \delta_2, \zeta_2) + \hat{\rho}_{trans}(\hat{\omega},c_ {trans}, \eta)
	\end{aligned}
\end{equation}   
```

 where:

```latex
\begin{equation}
	\hat{Theta}(\hat{\omega}, \delta, \zeta) = \frac{1}{1+\exp(\frac{\omega-\delta}{\zeta})}
\end{equation}
```

  The parameters within functions above are listed in table:

```latex
\begin{table}[htbp]
	\centering
	\begin{tabular}{cc|cc}
	\hline
	Parameters & interval       & Parameters& interval\\
	$c_{trans}$  & $[0.005, 0.05]$ &$\eta$ &$[0.004,  0.04]$\\
	$C_0$     &$[0,1]$ & $C_i$ & $[0,2]$ \\
	$\delta _{0}$ &[0.1, 0.30] &$\zeta _0$&[0.001,0.01]\\
	$\delta _1$&[0.15, 0.35] &$\zeta _1$&[0.01,0.05]\\
	$\delta _2$&[0.15, 0.35] &$\zeta _2$&[0.01,0.05]\\
	$M_i$&[0.12, 0.38]&$V_i$&[0.005,0.015]\\
	\hline
	\end{tabular}
	\caption{The training windows of parameter in \ref{ch5s2eq1}} 
	\label{ch5table1}
\end{table}
```

For example, the $\hat{\rho}_{below}$ look like:

![training_sample](C:\Users\77511\Desktop\新建文件夹\training_sample.png)

## Network hyper-parameters and training sample  parameters setting

Network hyper-parameters and training sample  parameters are free to change. All are listed in file parameter.py, so you can change setting base on your need.   