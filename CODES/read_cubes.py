import numpy as np
import matplotlib.pyplot as plt
file_in = "/var/lib/libvirt/images/nbody/baorsd/run101/density_field/S020_CIC1024_for_xi.bin"


nc = 1024
file_0 = np.fromfile(file_in, dtype=np.single)

