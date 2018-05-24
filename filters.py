import numpy as np
from scipy import signal

def calculate_M(slope_width):
    return int(4/slope_width)

def lowpass(cutoff,slope_width,rate):
    M = calculate_M(slope_width)
    Fc = cutoff/rate
    
    #Calculate Filter
    h = np.zeros(M)
    for i in range(M):
        offset = i-(M/2)
        if (offset) == 0:
            h[i] = 2*np.pi*Fc
        else:
            h[i] = np.sin(2*np.pi*Fc*offset)/offset
            
        h[i] *= (0.54 - 0.46* np.cos(2*np.pi*i/M) )
        
    #normalize H
    h = h/np.sum(h)
    
    return h

def highpass(cutoff,slope_width,rate):
    lp_h = lowpass(cutoff,slope_width,rate)
    h = -lp_h
    h[int(len(lp_h)/2)] = 1
    
    return h

def bandpass(band_start,band_stop,slope_width,rate):
    hp = highpass(band_start,slope_width,rate)
    lp = lowpass(band_stop,slope_width,rate)
    
    bp = signal.convolve(hp,lp)
    
    return bp

def rolling(size):
    return np.ones(size)
