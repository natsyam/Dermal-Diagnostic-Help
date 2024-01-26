from ultralytics import YOLO

model = YOLO("best.pt")


def predict(img):
    results = model(img)
    for result in results:
        probs = result.probs
        names = result.names

    probs_data = probs.data

    # Форматируем вывод
    formatted_output = ", ".join(
        [f"{names[i]} {probs_data[i]:.2f}" for i in range(len(probs_data))]
    )

    return formatted_output
