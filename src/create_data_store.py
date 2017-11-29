#!/usr/bin/env python
# import requests
import re, sys
import pandas as pd

"""
Read in the raw html info that was scraped in order to create a data set of
labels as well as urls where the mp3 are located.

This output data store will be referenced for all file names in the audio data dir
as well as when creating images of sonagrams

It will be the master data store of meta data allowing the creation of mp3 data again
if desired or expanded in future with additional classes of birds.
"""


if __name__ == '__main__':

    f = open('raw_target_data_url.txt', 'r')
    raw_data = f.read()
    f.close()
    data_rows = raw_data.split('\n')

    #file_label, species_label, audio_id, url
    #make a list of dictionaries with those keys and turn into a dataframe then csv it to file
    df_list = []
    counter = len(data_rows)

    count = 0
    while (count<counter-1):

        row_dict = {}
        start = data_rows[count].split(':')
        file_label = start[0]
        row_label = file_label
        # print('counter:{} count:{}'.format(counter,count))
        species_label = start[2].split('/')
        species_label = species_label[-1].split("'")
        species_label = species_label[0].lower()
        # print(file_label)
        while (file_label == row_label):
            count += 1
            # if(count==counter):
            #     sys.exit(0)
            #get the next row and process
            row = data_rows[count]
            labels = row.split(':')
            row_label = labels[0]

            #we need to be sure have a url row
            if(file_label == row_label):
                # print(row)
                audio_id = row.split("div id='")
                if(len(audio_id)<2):
                    continue
                audio_id = audio_id[1].split("'")
                audio_id = audio_id[0]
                # print(audio_id)
                url = row.split("data-xc-filepath='")
                url = url[1].split("'")
                url = url[0]
                #print('dictionary\nfile_label:{}\nspecies_label:{}\n \
                #audio_label:{}\nurl:{}\n'.format(file_label, species_label, audio_id, url))
                data_dict = {}
                data_dict['file_label'] = file_label
                data_dict['species_label'] = species_label
                data_dict['audio_id'] = audio_id
                data_dict['url'] = url
                print(data_dict)
                df_list.append(data_dict)


    df = pd.DataFrame.from_dict(df_list)
    df.to_csv('song_bird_database.csv') #rename this so I don't trash each time
