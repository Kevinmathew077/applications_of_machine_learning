import numpy as np
import pandas as pd
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

root_directory = os.getcwd()

working_directory = f"{root_directory}/working/frames/"
json_directory = f"{root_directory}/working/json/"
face_directory = f"{root_directory}/working/faces/"

# Load FER2013 dataset
data = pd.read_csv(
    f'{root_directory}/utils/prebuilts/model.h5')

# Split data into training and validation sets
train_data = data[data['Usage'] == 'Training']
val_data = data[data['Usage'] == 'PublicTest']

# Preprocess images and labels
X_train = np.array([np.fromstring(image, dtype=int, sep=' ').reshape(
    (48, 48, 1)) for image in train_data['pixels']])
X_val = np.array([np.fromstring(image, dtype=int, sep=' ').reshape(
    (48, 48, 1)) for image in val_data['pixels']])
y_train = train_data['emotion'].values
y_val = val_data['emotion'].values

# Normalize images
X_train = X_train.astype('float32') / 255.0
X_val = X_val.astype('float32') / 255.0

# Convert labels to one-hot vectors
num_classes = len(np.unique(y_train))
y_train = np.eye(num_classes)[y_train]
y_val = np.eye(num_classes)[y_val]

# Define model architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compile model
# was lr = 0.0001
model.compile(optimizer=Adam(lr=0.01),
              loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, batch_size=32,
          epochs=50, validation_data=(X_val, y_val))

# Save model
model.save(f'{root_directory}/utils/prebuilt/FERmodel.h5')
