import tensorflow as tf
import math, time 
from units import *
from tf_function import *

omega_dim = 3000
N_tau = 96
omega_low = 0
omega_up = 2.5
mb_size = 100
name = 'Vae_spectra'
tau_begin = 6
channel = 'P'
case = 'rescont'
training_epochs = 500000
maxkeep = 100
learning_rate = 1e-4
step_save = 500
path = 'Conf_data_charmonium_copy/'
num_gaussion_like = 20
reloading = True
Path = case + str(N_tau)
record_loss_step = 500

mean_low, mean_up = 0.12, 0.38
var_low, var_up = 0.005, 0.015
const_low, const_up = 0, 2
cont_low, cont_up = 0, 1
C_trans_low, C_trans_up = 5e-3, 5e-2
eta_low,   eta_up = 4e-3, 4e-2
deta0_low, deta0_up = 0.10, 0.30
deta1_low, deta1_up = 0.15, 0.35
deta2_low, deta2_up = 0.15, 0.35
zeta0_low, zeta0_up = 0.001, 0.01
zeta1_low, zeta1_up = 0.01, 0.05
zeta2_low, zeta2_up = 0.01, 0.05

Encoder1_units = [1500,  750,  350]
Encoder2_units = [150,   200,  350]
Decoder_units  = [750, 1500,  omega_dim]

Encoder1_activation = [Prelu, Prelu, [None, tf.exp]]
Encoder2_activation = [Prelu, Prelu, [None, tf.exp]]
Decoder_activation  = [Prelu, Prelu, [square, tf.exp]]

mean_mat, error_mat, mean = filereader(N_tau, tau_begin, channel, path)
