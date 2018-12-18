#just the bird_model def for calling
from keras.models import Sequential
from keras.layers import Input, concatenate, Dense, Dropout, Embedding, Flatten, Activation, Conv2D, MaxPooling2D, PReLU
from keras import regularizers
from keras.layers.normalization import BatchNormalization
import tensorflow as tf

xpixels = 138
ypixels = 138

"""
Model simpler and faster but now quite as accurate. The preprocessing is now
the focus. With a cleaner input this model should increase accuracy.

Overfitting was a major problem so added L1 and L2 after recording results and
using the best combination with best hyperparameter values.

Dropout also helped immensely. I have read not to use in CNN much but my experience
has been different. The model is much better with it.

With 18 epochs:
model.evaluate_generator(X_test_gen, steps=40)
[3.426939141750336, 0.61171875]

So 61% and ran faster than original
"""
def bird_model(num_classes):
    #build the model
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(xpixels, ypixels, 1)))
    model.add(PReLU(alpha_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(64, kernel_size=(3, 3), input_shape=(xpixels, ypixels, 1)))
    model.add(PReLU(alpha_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01)))

    model.add(Conv2D(64, kernel_size=(3, 3), input_shape=(xpixels, ypixels, 1)))
    model.add(PReLU(alpha_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    model.add(Conv2D(128, kernel_size=(3, 3), input_shape=(xpixels, ypixels, 1)))
    model.add(PReLU(alpha_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01)))

    model.add(Conv2D(128, kernel_size=(3, 3), input_shape=(xpixels, ypixels, 1)))
    model.add(PReLU(alpha_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    #MLP
    model.add(Flatten())
    model.add(Dense(128))
    model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model

"""
TODO insert accuracy

The newer bird_model is not as accurate but doesn't seem to overfit and is many optimizers
faster.

Numbers for this model:

"""
def bird_model_orig(num_classes):


        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(xpixels, ypixels, 1)))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(Conv2D(64, kernel_size=(3, 3)))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128, kernel_size=(3, 3)))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128, kernel_size=(3, 3)))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.25))
        ####
        # adding layers
        ####
        model.add(Conv2D(128, kernel_size=(3, 3)))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.25))

        model.add(Conv2D(128, kernel_size=(3, 3)))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.25))
         #######
        # end added layers
        #######

        #MLP
        model.add(Flatten())
        model.add(Dense(128))
        model.add(PReLU(alpha_regularizer=regularizers.l2(0.01)))
        model.add(Dropout(0.5))

        model.add(Dense(num_classes))
        model.add(Activation('softmax'))

        return model
