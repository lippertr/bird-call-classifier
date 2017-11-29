# coding: utf-8
get_ipython().magic('run cnn_birds.py')
model.summary()
model.load_weights('models/imgdata_33k_big2dcnn_stft2017112622285420171127053953.weights')
get_ipython().magic('pinfo model.predict')
import pandas as pd
df_preds = pd.read_csv('models/imgdata_33k_big2dcnn_stft_predictions.csv')
df_preds.head()
df_preds[0]
df_preds.head(1)
get_ipython().magic('ls ')
get_ipython().magic('clear ')
df_preds.describe()
df_preds.info()
model.predict_classes
model.predict_classes()
get_ipython().magic('pinfo model.predict_classes')
X_test_gen.classes
get_ipython().magic('pinfo X_test_gen')
with open('img_data/validation/european-goldfinch-carduelis-carduelis/xc_audio_101121_880.png', 'rb') as f:
    i1 = f.read()
    
type(i1)
model.predict(i1)
y, sr = librosa.load('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png')
import librosa
y, sr = librosa.load('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png')
y, sr = librosa.load('./img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png')
i1_label = './img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png'
y, sr = librosa.load('./data/xc_audio_100965_560.png')
y, sr = librosa.load('./data/xc_audio_100965_560.mp3')
model.predict(y)
p_gen = ImageDataGenerator(rescale=1./255)
p_gen.train_datagen.flow_from_directory('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',
                    class_mode='categorical',
                    target_size=(xpixels,ypixels),
                    color_mode='grayscale',
                    shuffle=True)
                    
p_gen1 = p_gen.flow_from_directory('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',
                    class_mode='categorical',
                    target_size=(xpixels,ypixels),
                    color_mode='grayscale',
                    shuffle=True)
                    
p_gen1 = p_gen.flow_from_directory('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',
                    class_mode='categorical',
                    target_size=(xpixels,ypixels),
                    color_mode='grayscale',
                    shuffle=True)
                    
import cv2
import opencv3
from PIL import Img
from PIL import Image
img = Image.open('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png')
img
get_ipython().magic('pinfo Image.open')
img
img = Image.open('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',mode='gray')
img = Image.open('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',cmap='gray')
img = Image.open('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',gray=100%)
img = Image.open('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png',gray='100%')
get_ipython().magic('whos ')
img.size
img.mode
img.format
img = Image.open('img_data/validation/european-greenfinch-chloris-chloris/xc_audio_100965_560.png').convert('L')
img.size
img.mode
import cv2
import cv3
import cv
import numpy as np
i1 = np.array(img)
i1
i1 = i1/255
i1
i1.shape
i1 = i1.reshape(138,138,1)
i1.shape
model.predict(i1)
i1 = i1.reshape(138,138,1,1)
model.predict(i1)
i1 = i1.reshape(,138,138,1)
i1 = i1.reshape(None,138,138,1)
i1 = i1.reshape(0,138,138,1)
i1 = i1.reshape(1,138,138,1)
model.predict(i1)
a1 = model.predict(i1)
a1.max()
a1.find(a1.max())
a1
a1.max()
a1[a1.max()]
a1[10]
len(a1)
a1[0][10]
a1[a1.max()]
a1.max()
a1
a1[0][16]
i1_label
european-greenfinch-chloris-chloris': 16
img = image.load_img(img_path, target_size=(138,138))
from keras.preprocessing import image
get_ipython().magic('pinfo image.load_img')
img = image.load_img(img_path, target_size=(138,138))
get_ipython().magic('history ')
img = image.load_img(img_path, target_size=(138,138))
img = image.load_img('img_data/validation/wood-warbler-phylloscopus-sibilatrix/xc_audio_101864_655.png', target_size=(138,138))
img.shape
img.getcolors
img.mode
img.show()
img.size
img.resize(138,138,1)
img.size[0]
img.resize(img.size[0],img.size[1],1)
img = image.load_img('img_data/validation/wood-warbler-phylloscopus-sibilatrix/xc_audio_101864_655.png', target_size=(138,138)).convert('L')
img.shape
image.size
img.size
img.getcolors
img.mode
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
x
x = x/255
x
get_ipython().magic('pinfo model.predict_classes')
get_ipython().magic('pinfo model.predict')
model.predict(x)
p1 = model.predict(x)
p1.argmax()
class_dict = {'american-robin-turdus-migratorius': 0,
 'barn-swallow-hirundo-rustica': 1,
 'bewicks-wren-thryomanes-bewickii': 2,
 'black-headed-gull-chroicocephalus-ridibundus': 3,
 'blackish-tapaculo-scytalopus-latrans': 4,
 'bluethroat-luscinia-svecica': 5,
 'brown-crested-flycatcher-myiarchus-tyrannulus': 6,
 'common-blackbird-turdus-merula': 7,
 'common-chaffinch-fringilla-coelebs': 8,
 'common-cuckoo-cuculus-canorus': 9,
 'common-reed-bunting-emberiza-schoeniclus': 10,
 'common-starling-sturnus-vulgaris': 11,
 'eurasian-bullfinch-pyrrhula-pyrrhula': 12,
 'eurasian-skylark-alauda-arvensis': 13,
 'eurasian-tree-sparrow-passer-montanus': 14,
 'european-goldfinch-carduelis-carduelis': 15,
 'european-greenfinch-chloris-chloris': 16,
 'fieldfare-turdus-pilaris': 17,
 'fox-sparrow-passerella-iliaca': 18,
 'great-spotted-woodpecker-dendrocopos-major': 19,
 'great-tit-parus-major': 20,
 'grey-breasted-wood-wren-henicorhina-leucophrys': 21,
 'house-sparrow-passer-domesticus': 22,
 'house-wren-troglodytes-aedon': 23,
 'lesser-whitethroat-sylvia-curruca': 24,
 'northern-raven-corvus-corax': 25,
 'red-crossbill-loxia-curvirostra': 26,
 'red-winged-blackbird-agelaius-phoeniceus': 27,
 'redwing-turdus-iliacus': 28,
 'rufous-browed-peppershrike-cyclarhis-gujanensis': 29,
 'rufous-collared-sparrow-zonotrichia-capensis': 30,
 'sedge-warbler-acrocephalus-schoenobaenus': 31,
 'song-sparrow-melospiza-melodia': 32,
 'song-thrush-turdus-philomelos': 33,
 'spotted-towhee-pipilo-maculatus': 34,
 'swainsons-thrush-catharus-ustulatus': 35,
 'tree-pipit-anthus-trivialis': 36,
 'white-wagtail-motacilla-alba': 37,
 'willow-warbler-phylloscopus-trochilus': 38,
 'wood-warbler-phylloscopus-sibilatrix': 39}
index_lookup = {v: k for k, v in class_dict.items()}
index-Lookup = 2
index_lookup[2]
get_ipython().magic('history ')
X_test_gen.index_generator
X_test_gen.index_generator()
X_test_gen.index_generator.mro()
X_test_gen.index_generator.mro
X_test_gen.index_generator.gi_running
X_test_gen.index_generator.?
get_ipython().magic('pinfo X_test_gen.index_generator')
cls
X_test_gen.classes
y_test = X_test_gen.classes
X_pred = model.predict_generator(X_test_gen)
X_pred = model.predict_generator(X_test_gen, steps=10)
X_pred.shape
y_test.shape
X_test_gen.class()
X_pred = model.predict_generator(X_test_gen, verbose=1)
X_pred = model.predict_generator(X_test_gen, steps=10, verbose=1)
X_pred = model.predict_generator(X_test_gen, steps=10, verbose=2)
y_test
X_pred.shape
X_pred[0]
X_pred[0].argmax()
get_ipython().magic('whos ')
index_lookup['15']
index_lookup.keys
index_lookup[15]
X_pred[1].argmax()
X_pred[12].argmax()
len(X_test_gen)
get_ipython().magic('whos ')
y_test.shape
X_pred = model.predict_generator(X_test_gen, steps=y_test.shape[0],batch_size=1, verbose=1)
X_pred = model.predict_generator(X_test_gen, steps=y_test.shape[0],max_queue_size=1, verbose=1)
X_pred
x_pred.shape
~x_pred.shape
X_pred.shape
del X_pred
model.predict_generator(X_test_gen, steps=y_test.shape[0],max_queue_size=1, verbose=1)
model.predict_generator(X_test_gen, steps=1,max_queue_size=1, verbose=1)
X_pred = model.predict_generator(X_test_gen, steps=1,max_queue_size=1, verbose=1)
X_pred.shape
X_test_gen.batch_size
X_test_gen.batch_size = 1
X_test_gen.batch_size
X_pred = model.predict_generator(X_test_gen, steps=1,max_queue_size=1, verbose=1)
X_pred.shape
x_pred[0]
X_pred[0]
X_pred[0].argmax()
X_test_gen.classes
x_test_gen.classes[14]
X_test_gen.classes[14]
X_pred = model.predict_generator(X_test_gen, steps=1,max_queue_size=1, verbose=1)
X_pred = model.predict_generator(X_test_gen, steps=X_test_gen.shape[0],max_queue_size=1, verbose=1)
histor
kA
get_ipython().magic('history ')
X_pred
X_pred.shape
x_pred[0].argmax()
x_pred[0].shape
X_pred[0].shape(0)
X_pred[0].argmax()
X_pred[0].argmax()
X_pred[0].argmax()
y_test[26]
X_pred[1].argmax()
y_test[8]
X_pred[44].argmax()
X_pred[23].argmax()
y_test[25]
y_test[19]
X_pred[19].argmax()
X_pred[38].argmax()
X_pred = model.predict_generator(X_test_gen, steps=X_test_gen.shape[0],max_queue_size=1, verbose=1)
X_test_gen.filenames
X_test_gen.filenames
get_ipython().magic('history ')
y_test
X_pred = model.predict_generator(X_test_gen, steps=y_test.shape[0],max_queue_size=1, verbose=1)
X_pred.shape
X_pred.shape(0)/y_test.shape(0)
X_pred.shape(0)
X_pred.shape
y_test.shape
X_pred.shape[0]/y_test.shape[0]
get_ipython().magic('whos ')
get_ipython().magic('pprint index_lookup')
get_ipython().magic('pprint')
get_ipython().magic('pprint index_lookup')
get_ipython().magic('pprint index_lookup')
index_lookup
X_pred
get_ipython().magic('history ')
get_ipython().magic('save prediction_ideas.history ~0/')
