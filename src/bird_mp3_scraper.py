#!/usr/bin/env python
import pandas as pd
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

"""
A class to process html sites for bird data.
Specifically set up to work on the https://xeno-canto.org site.
No reason this couldn't be generalized to scrape sound files from
any site.

"""

class bird_scraper():
    def __init__(self):
        return

    def get_sound_urls(self, num=40, save_to_file=False):
        '''
        get_sound_urls(self, num=40, save_to_file=False)

        A function to load the species data from the xeno-canto.org website

        Inputs:
        num: how many species urls to get
        save_to_file: save the num of species urls to file True/False
            defaults to False

        These are the base urls for an entire species that then will have links
            to pages with links to mp3 bird song files.

        Return: defaultdict of species base url pages

        '''
        # df = pd.read_csv('xc_species.csv', sep='\t') #previously obtained listing of all species on site
        # df.columns = ['common_name', 'scientific_name', 'Status','num_fg','num_bg']
        # df.pop('Status') #since nan and worthless
        # df.sort_values('num_fg',ascending=False, inplace=True)
        #
        # #only keep top 'num''
        # df_top = df.head(num)
        # if(save_top == True):
        #     df.to_csv('xc_sorted_top_species_list.csv', index=False)

        '''
        done--for each species url
        find how many pages
        creage list of pages urls
        go to each page and make list of mp3 urls with some meta metadata
        save to csv file
        download mp3 file and save
        '''
        df_top = pd.read_csv('xc_top_40.csv')
        base_url = 'http://www.xeno-canto.org/species/'

        #make species dict with top url for further processing
        species_pages = defaultdict()
        for i, row in df_top.iterrows():
            url_values = {}
            # scientific_name = dscientific_name
            url_values['top_url'] = base_url + row.scientific_name.replace(' ', '-')
            url_values['num_pages'] = row.num_pages
            species_pages[row.common_name] = url_values

        return species_pages


    def get_listings(urls):
        """
        get_listings(urls)

        Inputs: list of urls to get raw html with embedded mp3 file locations
        Returns: dictionary of species and value is list of urls for mp3 files

        Warning: this doesn't work as advertised and I created a list from grep'ing
            raw page html for the tag and then making list of song urls with unique_id.
        """

        for url in urls:
            #open the page and get the sound recording url and metadata
            url_raw = raw_input(url)
            r  = requests.get(url_raw)
            data = r.text
            soup = BeautifulSoup(data)

            for link in soup.find_all('a'):
                print(link.get('href'))
                #doesn't work so... have to implement later no time now

        pass #to remind me to really implement

    def get_song_sources(self, species):
        '''
        takes a dictionary of common_names in with values of dictionary of top_url,
        max_pages
        '''

        for k,v in main_urls.items():
            filename = k.replace(' ','_')
            filename = filename.replace("'", '-')
            with open(filename + '.txt', 'w+') as f:
                for i in range(1, v['num_pages']+1):
                    url_name = v['top_url'] + '?pg=' + str(i)
                    print('Getting html source for: {}'.format(url_name))
                    r = requests.get(url_name)
                    f.write(r.text)
                    #f.write(url_name)#only for testing purposes
                    f.write('\n')

                #save the song_page_url_source appending for each page
                #do new file for each common name
                #then I'll grep them and make into a list of usable urls for mp3s

    def get_song_mp3s():
        #for each url in our list get the mp3 downloaded
        df = pd.read_csv('song_data.csv')

        for i,song_data in df.iterrows():
            filename = song_data.audio_id+'.mp3'
            # url = 'https://www.bird-sounds.net/sounds/' + filename
            print("making file: {}  from: {}".format(filename, song_data.url))

            f = open('data/'+filename,'wb')  #create file locally
            f.write(requests.get(song_data.url).content)  #write content to this file
            f.close()

        return None
if __name__ == '__main__':

    scraper = bird_scraper()

    #get_sound_urls()
    # main_urls = defaultdict()
    # main_urls = get_sound_urls()
    # get_song_source(main_urls)

    # get_song_mp3s()  #used this line validation_steps
