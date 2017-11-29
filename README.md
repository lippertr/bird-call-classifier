** This is a work in progress for a class **

# Bird Classifier by Call or Song

It's widely agreed there are between 9,000-10,000 bird species. Some sources double that number (sources).

When outdoors a person is more likely to hear a bird than see it. This results in difficulty identifying bird species in rural and urban centers alike. If the sound can be used to classify a bird species, researchers to hobbyists can have a better idea of what species are present and ideally map their location.

Automated classification allows for hobbyists to easily retrieve information on the bird species being heard. Additionally, automated recordings can be mined to determine species and bird populations.

## Table of Contents

[Schedule](#schedule)


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
- 40 classes of bird species.
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

## Future

What I would do if I had more time

## Schedule
| Task        | Status           | Priority  | Time Used | Total Time
| -------------:|:-------------:| -----:|-----:|-----:|
| Munge Data                | **In Progress** | MVP     | 18   | 30 |
| Create ML Architecture    | **In Progress** | MVP     | 7   | 4 |
| Min CNN working w/ output | Not Started   | MVP     | 0   |8 |
| Architect DB schema       | Not Started     | Optional| 0   | 4 |
| Create DB                 | Not Started     | Optional| 0   | 4 |
| Train Model               | Not Started     | MVP     | 0   |40 |
| Create Presentation       | Not Started     | MVP     | 0   |8 |
| Update Documentation      | In Progress     | MVP     | 10  |6 |
| Finish Project Schedule   | In Progress     | MVP     | 10  | 4 |
| Update Project Schedule   | In Progress     | MVP     | 6  |5 |
| Output visualizations     | Not Started     | Optional| 0   | 3 |
| Meetings                  | Ongoing         | MVP     | 4   | 25 |
|-------------------        |----------       |-----    |--   |--|
| librosa                   | Complete        | MVP     | 9   | 3 |
| yaafe                     | Complete        | MVP     | 8   | 3 |
| pyAudioAnalysis           | Complete        | MVP     | 4   | 3 |
| abio                      | Complete        | MVP     | 4   | 3 |
| Review other Projects     | Complete        | Optional| 4   |4  |
| Create Git Repo           | Complete        | MVP     | 0.5 | 0.5 |
| Gather Data               | Complete        | MVP     | 22  |20 |
| s3 bucket for data        | Complete        | MVP     | 1 | 1 |
| Submit Proposal           | Complete        | MVP     | 2   | 3 |
|                           |                 | Totals: | x   |  100 (remaining not all tasked)|


## Acknowledgements
TBD

## License
TBD
