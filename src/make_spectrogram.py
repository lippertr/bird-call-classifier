#!/usr/bin/env python
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import sklearn.model_selection as sms
from collections import defaultdict
import sys

random_seed = 83
class sound_features():
    def __init__(self):
        return

    def make_spectrogram(self):
        return

    def read_meta(self):
        return

    def set_feature(self):
        return

    def _feature1(self):
        return

    def _feature2(self):
        return

"""
creat function to read all the files from the input directory
create % train test split
process features as decided
output images to directories for imagedatagenerator to use
"""
def make_spectrograms_from_master(X,y,t_or_v, number=50):
    #source_dir = '/home/ubuntu/s3_data/'
    source_dir = 'data/'

    out_root = 'img_data/'
    count = 0
    count_dict = defaultdict()
    for x,y_val in zip(X,y):
        #load the file in
        # filename = x.split('.')
        # filename = filename[0].split('_')
        # id_slug = filename[-2] + '_' + filename[-1]
        audio_filename = x + '.mp3'
        load_filename = source_dir + audio_filename
        img_path = out_root + t_or_v + '/' + y_val + '/'
        img_filename = img_path + x +'.png'
        if isfile(img_filename):
            continue

        print('{}: processing: {} label:{}'.format(t_or_v, x, y_val))
        print(load_filename)

        if not isfile(load_filename):
            print('file not found: {}'.format(audio_filename))
            continue

        song_data, sr = librosa.load(load_filename, duration=30, sr=22050) #load only 30 seconds,sr=22050
        plt.clf()
        plt.figure(figsize=(1,1), dpi=138)
        plt.subplot(1,1,1)
        '''
        for perceptual weighted log CQT
        '''
        # CQT = librosa.cqt(song_data, sr=sr)
        # freqs = librosa.cqt_frequencies(CQT.shape[0], fmin=50)
        # perceptual_CQT = librosa.perceptual_weighting(CQT**2,
        #                                               freqs,
        #                                               ref=np.max)
        # librosa.display.specshow(perceptual_CQT, fmin=50,fmax=20000, cmap='gray')
        '''
        end perceptual weighted log CQT
        '''

        '''
        for melspectrogram (log)
        '''
        #M = librosa.feature.mfcc(y=song_data, sr=sr, n_mfcc=40) #this doesn't give a good spectrogram
        M = librosa.feature.melspectrogram(y=song_data, sr=sr,n_fft=4096, hop_length=1024,n_mels=128,fmin=500)
        librosa.display.specshow(librosa.core.logamplitude(M, ref=np.max), fmin=500, cmap='gray') #log???
        '''
        end melspectrogram
        '''

        '''
        for stft
        '''
        #####S_stft, phase = librosa.magphase(librosa.stft(song_data)) #works well 55% on 33k/ 70% on 1k sample
        # S_stft, phase = librosa.magphase(librosa.stft(song_data, hop_length=32))
        # librosa.display.specshow(librosa.amplitude_to_db(S_stft, ref=np.max), cmap='gray')
        '''
        end for stft mfcc
        '''

        '''
        for central q frequency
        '''
        # cqt = librosa.cqt(y=song_data, sr=sr)
        # librosa.display.specshow(librosa.amplitude_to_db(cqt, ref=np.max), cmap='gray')
        '''
        end for cqt
        '''


        if not os.path.isdir(img_path):
            print('making filepath:{}'.format(img_path))
            os.makedirs(img_path)
        count += 1
        print(count)
        plt.savefig(img_filename)
        plt.close()
    return None


def make_spectrograms(X,y,t_or_v):

    # df_db = pd.read_csv('song_data.csv')
    # onlyfiles = [f for f in listdir('data/') if isfile(join('data/', f))]
    count = 0
    for x,y_val in zip(X,y):
        # print('{}: processing: {} label:{}'.format(t_or_v, x, y_val))

        #load the file in
        filename = x.split('.')
        filename = filename[0].split('_')
        id_slug = filename[-2] + '_' + filename[-1]
        audio_filename = 'xc_audio_' + id_slug + '.mp3'
        img_path = 'img_data/' + t_or_v + '/' + y_val + '/'
        img_filename = img_path + y_val + '_' + id_slug + '.png'

        if isfile(join('data/', audio_filename)):
            load_filename = 'data/' + audio_filename
        else:
            load_filename = 'data3/' + audio_filename

        #trim white space at start
        #move start time to where first sound spike is located
        #   if I move to first sound spike I don't need to trim or vice versa...
        song_data, sr = librosa.load(load_filename, duration=30, sr=22050) #load only 60 seconds
        # M = librosa.feature.melspectrogram(y=song_data, sr=sr,n_fft=4096, hop_length=1024,n_mels=128,fmax=11025)
        #M = librosa.feature.mfcc(y=song_data, sr=sr, n_mfcc=40)
        S, phase = librosa.magphase(librosa.stft(song_data))

        plt.clf()
        plt.figure(figsize=(1,1), dpi=138)
        plt.subplot(1,1,1)
        # librosa.display.specshow(librosa.logamplitude(M,ref_power=np.max),sr=sr, hop_length=1024,\
        #                          fmax=11025,cmap='gray')
        librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), cmap='gray')
        if not os.path.isdir(img_path):
            print('making filepath:{}'.format(img_path))
            os.makedirs(img_path)
        count += 1
        print(count)
        plt.savefig(img_filename)
    return None

def first_stab():
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
    return

if __name__ == '__main__':

    args = sys.argv[1:]

    test_size = 0.3

    # img_path = 'img_data2/' #for testing at increased size
    # mp3_path = 'data/'
    '''
        done: 1.read in sample list
        done: 2. shuffle it up
        3. process file as I want with librosa
        4. write spectrogram for that file in proper train/validate label directory
        5. ready to train and test a model
    '''
    #get files from master audio directory for entire dataset testing
    #only_mp3_files = [f for f in listdir('data/') if isfile(join('data/', f)) and f.endswith('.mp3')
    #df_mp3 = pd.DataFrame(only_mp3_files)

    if not args:
        #use master db csv and assume all audio files exist
        # df = pd.read_csv('song_data.csv')
        # df.pop('file_label')
        # df.pop('url')
        # df.columns = ['file','label']
######################################################################
        # read in the 1000ish files for quick testing
        df = pd.read_csv('sample_1000.list', header=None, sep='/')
        df.columns = ['p1','p2','old_split', 'label', 'file']
        df.pop('p1')
        df.pop('p2')
        for index, row in df.iterrows():
            filename = row.file
            filename = filename.split('.')[0]
            filename = filename.split('_')
            filename = filename[1:]
            filename = '_'.join(filename)
            filename = 'xc_audio_' + filename
            df.iloc[index]['file'] = filename

    ########################################################

        X, X_test, y, y_test = sms.train_test_split(df.file, df.label, random_state=random_seed, test_size=test_size)

        df_train = pd.DataFrame(X)
        df_train.columns = ['x_value']
        df_train['label'] = y
        df_train.to_csv('1train_data.csv')

        df_test = pd.DataFrame(X_test)
        df_test.columns = ['x_value']
        df_test['label'] = y_test
        df_test.to_csv('1test_data.csv')
        make_spectrogram(X,y,'train')
        make_spectrogram_from_master(X_test,y_test,'validation')

    else:
        in_file = args[0]

        '''
        open the file
        make into same as before with file, label
        if test:
            make_test
        else:
            make validation
        '''
        type_data = in_file.split('.')[-1]

        #load in the data
        df_in = pd.read_csv(in_file)
        X = df_in['x_value'].tolist()
        y = df_in['label'].tolist()

        if type_data == 'train':
            make_spectrogram_from_master(X,y,'train')
        elif type_data == 'test':
            make_spectrogram_from_master(X,y,'validation')
        else:
            print('input file error: {}'.format(in_file))

    #need to loop through files
    # make_spectrogram_from_master(X,y,'train')
    # make_spectrogram_from_master(X_test,y_test,'validation')

    # make_spectrogram(X,y,'train')
    # make_spectrogram(X_test, y_test, 'validation')

    # for filename in input_mp3_files:
    #
    #     # print(filename)
    #
    #     '''
    #     make the new img_filename
    #     species_label (from csv DB) + unique_id + .png
    #     common_name, species_name: get from database (or csv file in this case)
    #     unique_id: strip from mp3 filename
    #     '''
    #     search_tag = filename.split('.')[0]
    #     name_parts = search_tag.split('_')
    #     unique_id = name_parts[2] + '_' + name_parts[3]
    #     label = df_songs[df_songs.audio_id == search_tag]
    #     label = label.species_label.item()
    #
    #     # print('label: {} search_tag: {} unique_id:{}'.format(label, search_tag, unique_id))
    #     img_filename = '{}_{}.png'.format(label, unique_id)
    #     # print('filename: {}_{}.png'.format(label, unique_id))
    #     print(img_filename)
    #
    #
    #
    #     '''
    #     code for class or function to create the image from first 30 seconds of mp3
    #     '''
    #     y, sr = librosa.load(mp3_path + filename, duration=30, sr=22050) #load only 30 seconds
    #
    #     #S = librosa.stft(y)
    #     M = librosa.feature.melspectrogram(y=y, sr=sr,n_fft=4096, hop_length=1024,n_mels=128,fmax=11025)
    #     plt.clf()
    #     plt.figure(figsize=(1,1), dpi=138)
    #     plt.subplot(1,1,1)
    #     librosa.display.specshow(librosa.logamplitude(M,ref_power=np.max),sr=sr, hop_length=1024,\
    #                              fmax=11025,cmap='gray')
    #
    #     plt.savefig(img_path + img_filename)
