# A population describes a group of creatures which specifies neural networks.
# An environment describes the datasets and the creatures to develop
from tensorflow.keras.datasets import boston_housing
import numpy as np, tensorflow as tf
import time
class Environment():
    def __init__(self,population):
        self.prepare_dataset()
        self.population=population
    def prepare_dataset(self):
        (train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
        self.train_data = train_data
        self.train_targets = train_targets
        self.test_data = test_data
        self.test_targets = test_targets

        self.mean = train_data.mean(axis = 0)
        self.train_data -= self.mean # shift
        self.std = train_data.std(axis = 0)
        self.train_data /=self.std # rescale

        self.test_data -= self.mean
        self.test_data /= self.std
    def developCreature(self,creature):
        creature.develop(self.train_data.shape[1])
        K = 4
        num_val_samples = len(self.train_data) // K
        num_epochs = 8
        all_mae_histories = []


        T1 = time.time()

        for i in range(K):
            print('processing fold', i)
            
            # Prepare the validation data: data from partition i
            a, b = i * num_val_samples, (i + 1) * num_val_samples
            val_data = self.train_data[a : b]
            val_targets = self.train_targets[a : b]
            
            # Prepare the training data: data from all other partitions
            partial_train_data = np.concatenate([self.train_data[:a], self.train_data[b:]], axis=0)
            partial_train_targets = np.concatenate([self.train_targets[:a], self.train_targets[b:]], axis=0)

            # Build the Keras model (already compiled)
            model = creature.model
            
            # Train the model (in silent mode, verbose=0)
            history = model.fit(partial_train_data, partial_train_targets,
                                validation_data=(val_data, val_targets),
                                epochs=num_epochs, batch_size=1, verbose=0, 
                                callbacks=[CustomCallback()])

            mae_history = history.history['val_mae']
            all_mae_histories.append(mae_history)

        T2 = time.time()
        print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
        return {
            'cr':creature,
            'mae':all_mae_histories,
            'runtime':(T2 - T1)*1000,
        }

class CustomCallback(tf.keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs=None):
        c = ['\b|', '\b/', '\b-', '\b\\'] 
        print(c[epoch % 4], end='')
    def on_epoch_end(self, epoch, logs=None):
        print('\b', end='')