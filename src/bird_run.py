from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.sequence import pad_sequences
xpixels=138
ypixels=138

#get input genorator to images
#you can also use ImageDataGenerator to augment images but not sure how to add images
#   together after several differerent types of augmentation

train_datagen = ImageDataGenerator(rescale=1./255)
train_validation_datagen = ImageDataGenerator(rescale=1./255)
X_train_gen = train_datagen.flow_from_directory('img_data/train',
                class_mode='categorical',
                target_size=(xpixels,ypixels),
                color_mode='grayscale',
                shuffle=True)

X_test_gen = train_validation_datagen.flow_from_directory('img_data/validation/',
                class_mode='categorical',
                target_size=(xpixels,ypixels),
                color_mode='grayscale',
                shuffle=True)

model = bird_model(X_train_gen.num_class)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit_generator(
    X_train_gen,
    verbose=1,
    steps_per_epoch=300, #300 should typically be equal to the number of unique samples of your dataset divided by the batch size
    epochs=60,  #50,
    callbacks=[tensorbd],
    validation_data=X_test_gen,
    validation_steps=100) # validation_steps should be equal to
                         # the number of unique samples of your
                         # VALIDATION dataset divided by the batch size.

#saving weights and model both just to be pedantic
#weight_file = data_run_name + t_stamp + '.weights'
#model.save_weights(weight_file)

#model_file = data_run_name + t_stamp + '_model.hdf5'
#model.save(model_file)

'''
remember this is an example of how to save and load the model from the keras
documentation
'''

#use the code below to save and restore without retraining and wasting time
'''
from keras.models import load_model

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')
'''
