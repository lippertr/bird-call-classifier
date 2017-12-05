# Bird Classifier by Call or Song

It's widely agreed there are between 9,000-10,000 bird species. Some sources double that number (sources).

When outdoors a birder seems more likely to hear a bird than see it. This results in difficulty identifying bird species in rural and urban centers alike since we visual location can be difficult at times. However, by using a bird's call or song we can identify the species and decide if we wish pursue visual identification. If the sound can be used to classify a bird species, researchers and amateur birders alike can have a better idea of what species are present and ideally map their location.

Automated classification allows for hobbyists to easily retrieve information on the bird species heard. Additionally, automated recordings could be stored and compared to future sound events determining if species depopulation has occurred.

## Table of Contents

- [Future Plans](#future-plans)
- [Acknowledgements](#acknowledgements)


## Overview Pipeline
Data in cloud
Gather html data for bird species
Scrape for species pages
Access species pages and scrape for mp3 urls
Download mp3 urls into master audio store
Process audio with selected features to output a sonogram
Process sonogram with CNN to classify bird song or calls



## Data Sources
- http://www.xeno-canto.org/
- https://www.mbr-pwrc.usgs.gov/id/calllist.html
- https://nationalzoo.si.edu/scbi/migratorybirds/education/nasongkey.pl
- https://www.bird-sounds.net/
- http://www.birds.cornell.edu/Page.aspx%3Fpid%3D1059
- http://ebird.org/content/ebird/
- https://secure.birds.cornell.edu/cassso/login?service=https%3A%2F%2Fmacaulaylibrary.org%2Fauth%2Fclo%2Fcallback%3Furl%3Dhttps%253A%252F%252Fmacaulaylibrary.org%252Fsignin

white paper:
https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43905.pdf

## Data
- 40 classes of bird species. :bird:
- 33,567 seperate audio files.
- 85G of audio data.
- Used 70/30% split for 40 classes and 22K samples in train set.
- 13K sample validation set.


## Features
Features existing or synthesized for modeling.

## Convolutional Neural Network

Describe the model

## Problems (maybe as seperate or grouped topics)
Challanges faced and solutions used

## Final Model Architecture

The good stuff on how this problem was solved using the CNN

## Results

What I found

## Future Plans

A website and a smartphone app would be ideal since this would give a wide range of access to the data and provide a means to increase the data samples per species.

## Acknowledgements
TBD

## License
TBD
