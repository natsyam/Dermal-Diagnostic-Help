from imgaug import augmenters as iaa
import imageio.v2 as imageio
import os


# Определение последовательности аугментаций
seq = iaa.Sequential([
    iaa.Fliplr(0.5),  # горизонтальные отражения с вероятностью 50%
    iaa.Flipud(0.2),  # вертикальные отражения с вероятностью 20%
    iaa.Affine(
        rotate=(-10, 10),  # случайный поворот на угол от -10 до 10 градусов
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},  # случайное масштабирование по осям X и Y
        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},  # случайный сдвиг по осям X и Y
    ),
    iaa.Multiply((0.8, 1.2), per_channel=0.2),  # случайное изменение яркости изображений
    iaa.GaussianBlur(sigma=(0, 1.0)),  # применение гауссова размытия с сигмой от 0 до 1.0
    iaa.LinearContrast((0.8, 1.2)),  # изменение контраста изображения
    iaa.Crop(percent=(0, 0.1)),  # случайная обрезка частей изображения до 10% от исходных размеров
    iaa.PerspectiveTransform(scale=(0.01, 0.1)),  # случайное применение перспективных трансформаций
], random_order=True)  # применять трансформации в случайном порядке


# Путь к изображениям редких классов
rare_class_images_path = 'sorted_images/akiec'

# Цикл по изображениям редкого класса для их аугментации
for image_file in os.listdir(rare_class_images_path):
    image_path = os.path.join(rare_class_images_path, image_file)
    image = imageio.imread(image_path)
    augmented_images = seq(images=[image] * 3)  # генерация 10 аугментированных копий

    # сохранение аугментированных изображений
    for i, aug_image in enumerate(augmented_images):
        augmented_image_path = os.path.join(rare_class_images_path, f"aug_{i}_{image_file}")
        imageio.imwrite(augmented_image_path, aug_image)
