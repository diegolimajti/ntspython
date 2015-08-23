# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 17:07:01 2014

@author: diego
"""
import scipy.io
import pandas as pd

def load_data():
    """
    --Parameters--
    filename - Where sampleEEGdata.mat will be stored. The file can be downloaded at
    http://www.mikexcohen.com/
    
    --Returns--
    data - The processed EEG data in 64 channels (acessed through [0:63] x
    640 data points x 99 trials (acessed through [0:98]) in an ndarray
    
    time - The actual millisecond timing of the 640 datapoints in an ndarray
    
    channels - The names of channels in a list
    ---------
    
    Its possible to see all fields in the EEG object with numpy.dtype(eeg).
    Function can be changed to return other relevant data.
    """
    
    mat = scipy.io.loadmat(file_name = 'sampleEEGdata.mat')
    
    #eeg is a single matlab structure (0x0 matrix) that have all the relevant fields
    eeg = mat['EEG'][0,0]
    
    data = eeg['data']
    time = eeg['times'][0]
    channels = [d[0] for d in eeg['chanlocs']['labels'][0]]
    srate = eeg['srate'][0,0]
    
    return data, time, channels, srate
    
