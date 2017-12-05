# Bird Classifier by Call or Song

It's widely agreed there are between 9,000-10,000 bird species. Some sources double that number (sources).

When outdoors a birder seems more likely to hear a bird than see it. This results in difficulty identifying bird species in rural and urban centers alike since we visual location can be difficult at times. However, by using a bird's call or song we can identify the species and decide if we wish pursue visual identification. If the sound can be used to classify a bird species, researchers and amateur birders alike can have a better idea of what species are present and ideally map their location.

Automated classification allows for hobbyists to easily retrieve information on the bird species heard. Additionally, automated recordings could be stored and compared to future sound events determining if species depopulation has occurred.

## Table of Contents

- [Overview Pipeline](#overview-data-flow)
- [Data Sources](#data-sources)
- [Data](#data)
- [Features](#features)
- [Convolutional Neural Network](#convolutional-neural-network)
- [Final Model Architectue](#final-model-architecture)
- [Results](#results)
- [Future Plans](#future-plans)
- [Acknowledgements](#acknowledgements)


## Overview Data Flow
Data gathered from xeno-centro website.
40 top species determined with landingpages for obtaining mp3 urls
Mp3s scraped and stored on AWS S3
Librosa used to transform the sound into a spectrogram.
Process sonogram with CNN to classify bird song or calls.

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
- 40 classes of bird species.
- 33,567 seperate audio files.
- 85G of audio data.
- Used 60/40% split for 40 classes and 20K samples in train set.
- 13K sample validation set.


## Features
Features used in final model were STFT.

## Convolutional Neural Network

A muli layer CNN with PReLU activation and 1 Dense layer with 1 output sigmoid layer. Input was 138x138x1 grayscal spectrogram.

## Problems (maybe as separate or grouped topics)
Challenges faced and solutions used

## Final Model Architecture

Final model was a CNN implemented with Keras

## Results

Using a sample set of 33,567 split 60/40 to give test set: 20K, validation set: 13K
Accuracy: 63.5%

## Future Plans

A website and a smartphone app would be ideal since this would give a wide range of access to the data and provide a means to increase the data samples per species.

## Acknowledgements
1. https://www.safaribooksonline.com/library/view/hands-on-machine-learning/9781491962282/ch11.html -- prelu diagram
2. https://www.allaboutbirds.org/guide/Barn_Swallow/id
3. https://eastsideaudubon.org/corvid-crier-stories-2014-12/bird-of-the-month-red-crossbill-loxia-curvirostra
4. https://www.amnh.org/about-the-museum/press-center/new-study-doubles-the-estimate-of-bird-species-in-the-world
5. http://kentorchards.org.uk/?wildlife=greater-spotted-woodpecker
6. https://www.allaboutbirds.org/guide/PHOTO/LARGE/fox_sparrow_garytyson.jpg
7. http://cdn.audubon.org/cdn/farfuture/lXuJTdJNEgTYmGhH73SLss1cbfWAN5A-h3XPET8YOzY/mtime:1422549944/sites/default/files/House_Sparrow_s52-12-123_l_1.jpg
8. https://www.allaboutbirds.org/guide/PHOTO/LARGE/barn_swallow_1.jpg
9. https://www.youtube.com/watch?v=PmMYVeE9QJw
10. https://www.youtube.com/watch?v=m1k3N0VaqGc
11. http://www.audubon.org/field-guide/bird/great-horned-owl
12. Presentation template by SlidesCarnival
13. http://www.singing-wings-aviary.com/wp-content/uploads/2015/02/European-Goldfinch-Photos.jpg
13. http://orientalbirdimages.org/images/data/lesser_whitethroat__0002562lr.jpg
15. http://www.whenlifeisgood.com/birding-by-ear-how-to-identify-birds-by-their-sounds/
