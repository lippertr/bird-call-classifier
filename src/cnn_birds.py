#!/usr/bin/env python

from __future__ import print_function

import keras
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, concatenate
from keras.layers import Dense, Dropout, Embedding, Flatten, Activation
from keras.layers.normalization import BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
from keras.layers import PReLU
from keras import regularizers
from keras.preprocessing import image
import numpy as np

"""
The model class for a convelutional neural network using keras
"""
class model_sonograms():
    def __init__(self, input_data_path='./', xpixels=138, ypixels=138):
        self.xpixels = xpixels
        self.ypixels = ypixels
        self.input_data_path = input_data_path
        self.X_test_gen = None
        self.X_train_gen = None
        self._t_stamp = self._get_time_str()
        self.model = None

        return

    def load_samples(self, rescale=1./255):
        """
        Loads the sample data test and validation into keras ImageDataGenerators
        Input: input_data_dir - the director where the sample image files are located
               The directory structur must adhere to the ImageDataGenerator rules see
               Keras documentation for details since at this time the structure is handy
               but completely inflexible.
               Basic structure:
               input_data_dir/
                            ├── train
                            │   ├── label1
                            │   │   ├── image_file_1
                            │   │   └── image_file_N
                            │   ├── label2
                            │   │   ├── image_file_1
                            │   │   └── image_file_N
                            │   └── label3
                            │       ├── image_file_1
                            │       └── image_file_N
                            └── validation
                                    ├── label1
                                    │   ├── image_file_1
                                    │   └── image_file_N
                                    ├── label2
                                    │   ├── image_file_1
                                    │   └── image_file_N
                                    └── label3
                                        ├── image_file_1
                                        └── image_file_N
        Return: Training image generator, Test image generator
        """
        train_datagen = ImageDataGenerator(rescale=1./255)
        train_validation_datagen = ImageDataGenerator(rescale=1./255)
        self.X_train_gen = train_datagen.flow_from_directory(self.input_data_path + 'train/',
                        class_mode='categorical',
                        target_size=(self.xpixels,self.ypixels),
                        color_mode='grayscale',
                        shuffle=True)
        self.X_test_gen = train_validation_datagen.flow_from_directory(self.input_data_path + 'validation/',
                        class_mode='categorical',
                        target_size=(self.xpixels,self.ypixels),
                        color_mode='grayscale',
                        shuffle=True)

        return self.X_train_gen, self.X_test_gen

    def make_model(self):
        """
        Makes the model
        Input: the number of classes in the samples that will be used for training/validation
        Return: the model
        """
        self.model = Sequential()
        #input layer
        self.model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(self.xpixels, self.ypixels, 1)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))

        #layers
        self.model.add(Conv2D(64, kernel_size=(3, 3)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        # self.model.add(Dropout(0.25))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))


        self.model.add(Conv2D(128, kernel_size=(3, 3)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(128, kernel_size=(3, 3)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        # self.model.add(BatchNormalization())
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(128, kernel_size=(3, 3)))
        # self.model.add(BatchNormalization())
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(128, kernel_size=(3, 3)))
        self.model.add(BatchNormalization())
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        #MLP
        self.model.add(Flatten())
        self.model.add(Dense(128))
        self.model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        self.model.add(Dropout(0.5))


        #output layer
        self.model.add(Dense(self.X_test_gen.num_class)) #could also use X_test_gen num_classes are equal
        self.model.add(Activation('softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return self.model

    def fit(self, steps_per_epoch=5, epochs=20):
        """
        Uses the fit_generator method to fit the model to the loaded input images
        """
        self.model.fit_generator(
            self.X_train_gen,
            verbose=1,
            steps_per_epoch=steps_per_epoch, #300 should typically be equal to the number of unique samples of your dataset divided by the batch size
            epochs=epochs,  #50,
            callbacks=[tensorbd],
            validation_data=self.X_test_gen,
            validation_steps=10) # validation_steps should be equal to
                                 # the number of unique samples of your
                                 # VALIDATION dataset divided by the batch size.

        return None

    def save(self, save_name, weights=True, hdf5_model=True):
        #saving weights and model both just to be pedantic
        weight_file = save_name + self._t_stamp + '.weights'
        self.model.save_weights(weight_file)

        model_file = save_name + self._t_stamp + '_model.hdf5'
        self.model.save(model_file)

        '''
        need a load:
        model.load_weights(filepath, by_name=False)
        '''
        return None

    def _get_time_str(self):
        """
        Utility function to return timestamp string to append to log and
        weight output files
        """
        from datetime import datetime
        self._t_stamp = datetime.now()
        self._t_stamp = str(self._t_stamp)
        self._t_stamp = self._t_stamp.replace('-','')
        self._t_stamp = self._t_stamp.replace(' ', '')
        self._t_stamp = self._t_stamp.replace(':', '')

        #don't need fractional seconds for this
        return self._t_stamp.split('.')[0]

    def predict_item(self, image_filename):
        """
        takes one input image and returns the class label
        """

        img = image.load_img(image_filename, target_size=(138,138)).convert('L')
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img/255
        p1 = self.model.predict(img).argmax()

        '''
        predict_generator should work but no one on the planet can seem to get the true labels out so???
            How is that good?
        '''
        #reverse the class dictionary to lookup on assigned index
        index_lookup = {v: k for k, v in self.X_test_gen.class_indices.items()}
        # X_pred = self.model.predict_generator(self.X_test_gen, steps=10, verbose=1)
        # for i in range(X_pred.shape[0]):
        #     print( index_lookup[X_pred[i].argmax()])


        return index_lookup[p1]


if __name__ == '__main__':

    input_image_path = '../data/xeno-canto/img_data/'
    bird_model = model_sonograms(input_data_path=input_image_path)
    bird_model.load_samples()
    bird_model.make_model()

    #use tensorboard to see output and tweak
    save_name_prefix = 'imgdata1k_changed_layers1_stft'
    tensorbd = TensorBoard('logs/' + save_name_prefix)

    # bird_model.fit(epochs=100)
    bird_model.fit(steps_per_epoch=20, epochs=50)

    bird_model.save(save_name_prefix, weights=True, hdf5_model=True)

    #make predictions
    #hardcoded for test purposes
    image_filename = '../data/xeno-canto/img_data/validation/european-greenfinch-chloris-chloris/xc_audio_171039_120.png'
    predict_class = bird_model.predict_item(image_filename)

    # for all of validation set
    # for a one off entered in to show misclassification


    #using my validation items make a prediction with the labels and return
    # do for all then do for one
