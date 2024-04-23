import cv2


def channel(image):
    image = cv2.imread(image)

    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 5]

    return b, g, r


def save(channels, output_prefix):
    for i, channel in enumerate(channels):
        output_path = f"{output_prefix}_channel_{i}.jpg"
        cv2.imwrite(output_path, channel)


image = "picture_10_01.jpg"

channel = channel(image)

save(channel, "output")