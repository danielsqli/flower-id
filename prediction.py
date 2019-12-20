from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import tensorflow as tf

cwd = os.getcwd()
model = tf.keras.models.load_model("model.h5")
label_dir = os.path.join(cwd, 'nonResized\\train')
input_dir = os.path.join(cwd, 'input')


def predict(model, label_dir, input_dir):
    labels = [i for i in os.listdir(label_dir)]
    input_gen = ImageDataGenerator(rescale=1. / 255)
    input_data_gen = input_gen.flow_from_directory(batch_size=1,
                                                   directory=input_dir,
                                                   target_size=(200, 200),
                                                   class_mode='categorical',
                                                   shuffle=False)

    predictions = [labels[j] for j in model.predict_generator(input_data_gen).argmax(axis=-1)]
    print(predictions)
    print(input_data_gen.filenames)


predict(model,label_dir, input_dir)
