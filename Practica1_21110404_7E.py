# Importamos las bibliotecas necesarias
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Definimos los directorios de entrenamiento y validación
train_dir = 'data/train'
validation_dir = 'data/validation'

# Creamos un generador de imágenes de entrenamiento y otro de validación con aumentación de datos
train_datagen = ImageDataGenerator(
    rescale=1./255,             # Reescalamos los píxeles a valores entre 0 y 1
    rotation_range=40,          # Rango de rotación aleatorio
    width_shift_range=0.2,      # Desplazamiento horizontal aleatorio
    height_shift_range=0.2,     # Desplazamiento vertical aleatorio
    shear_range=0.2,            # Deformación aleatoria
    zoom_range=0.2,             # Zoom aleatorio
    horizontal_flip=True,       # Volteo horizontal aleatorio
    fill_mode='nearest'         # Modo de relleno
)

validation_datagen = ImageDataGenerator(rescale=1./255)  # Solo reescalamos las imágenes de validación

# Creamos los generadores de datos de entrenamiento y validación
train_generator = train_datagen.flow_from_directory(
    train_dir,                 # Directorio de imágenes de entrenamiento
    target_size=(150, 150),    # Tamaño de las imágenes (ancho, alto)
    batch_size=20,             # Tamaño del lote
    class_mode='binary'        # Modo de clasificación binaria
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,            # Directorio de imágenes de validación
    target_size=(150, 150),    # Tamaño de las imágenes (ancho, alto)
    batch_size=20,             # Tamaño del lote
    class_mode='binary'        # Modo de clasificación binaria
)

# Creamos el modelo de red neuronal convolucional
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilamos el modelo
model.compile(
    loss='binary_crossentropy',   # Función de pérdida para clasificación binaria
    optimizer='adam',             # Optimizador Adam
    metrics=['accuracy']          # Métrica de precisión
)

# Entrenamos el modelo
history = model.fit(
    train_generator,
    steps_per_epoch=100,          # Número de pasos por época
    epochs=100,                   # Número de épocas de entrenamiento
    validation_data=validation_generator,
    validation_steps=50           # Número de pasos de validación
)

# Guardamos el modelo
model.save('object_detection_model.h5')
