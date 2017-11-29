#!/usr/bin/env python
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join
import pandas as pd

if __name__ == '__main__':
    img_path = 'img_data/'
    mp3_path = 'data3/'
    all_files = [f for f in listdir(mp3_path) if isfile(join(mp3_path, f)) and f.endswith(".mp3")]

    df_songs = pd.read_csv('song_data.csv')

    #need to loop through all mp3 files
    for filename in all_files:

        # print(filename)

        '''
        make the new img_filename
        species_label (from csv DB) + unique_id + .png
        common_name, species_name: get from database (or csv file in this case)
        unique_id: strip from mp3 filename
        '''
        search_tag = filename.split('.')[0]
        name_parts = search_tag.split('_')
        unique_id = name_parts[2] + '_' + name_parts[3]
        label = df_songs[df_songs.audio_id == search_tag]
        label = label.species_label.item()

        # print('label: {} search_tag: {} unique_id:{}'.format(label, search_tag, unique_id))
        img_filename = '{}_{}.png'.format(label, unique_id)
        # print('filename: {}_{}.png'.format(label, unique_id))
        print(img_filename)

        '''
        code for class or function to create the image from first 30 seconds of mp3
        '''
        y, sr = librosa.load(mp3_path + filename, duration=30, sr=22050) #load only 30 seconds

        #S = librosa.stft(y)
        M = librosa.feature.melspectrogram(y=y, sr=sr,n_fft=4096, hop_length=1024,n_mels=128,fmax=11025)
        plt.clf()
        plt.figure(figsize=(1,1), dpi=138)
        plt.subplot(1,1,1)
        librosa.display.specshow(librosa.logamplitude(M,ref_power=np.max),sr=sr, hop_length=1024,\
                                 fmax=11025,cmap='gray')

        plt.savefig(img_path + img_filename)
        plt.close()
