import os
import shutil
import pandas as pd

# Путь к вашему CSV файлу с аннотациями
csv_file_path = 'path_to_your_updated_csv_file.csv'

# Директория, где находятся ваши изображения
images_directory = 'HAM10000_images_part_2'

# Директория, куда будут перемещены отсортированные изображения
sorted_images_directory = 'sorted_images'

# Чтение CSV файла
df = pd.read_csv(csv_file_path)

# Создание папок для каждого класса, если они еще не созданы
for label in df['labelfile'].unique():
    class_dir = os.path.join(sorted_images_directory, label)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

# Перемещение изображений в соответствующие папки
for index, row in df.iterrows():
    # Составление полного пути к исходному изображению
    src_path = os.path.join(images_directory, row['imagefile'])

    # Составление пути к папке назначения на основе класса изображения
    dst_path = os.path.join(sorted_images_directory, row['labelfile'], row['imagefile'])

    # Перемещение файла, если он существует
    if os.path.isfile(src_path):
        shutil.move(src_path, dst_path)
    else:
        print(f"Файл {src_path} не найден.")

print("Изображения успешно отсортированы.")
