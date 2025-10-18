import os
import xml.etree.ElementTree as ET

# jeśli skrypt jest w katalogu głównym projektu:
base_dir = "DATA"  

sets = ["train", "val"]

for set_name in sets:
    images_path = os.path.join(base_dir, "images", set_name)
    labels_path = os.path.join(base_dir, "labels", set_name)
    yolo_labels_path = os.path.join(base_dir, "labels", set_name + "_yolo")
    os.makedirs(yolo_labels_path, exist_ok=True)

    for xml_file in os.listdir(labels_path):
        if not xml_file.endswith(".xml") and not xml_file.endswith(".html"):
            continue
        tree = ET.parse(os.path.join(labels_path, xml_file))
        root = tree.getroot()

        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        yolo_lines = []
        for obj in root.findall('object'):
            class_id = 0
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            x_center = ((xmin + xmax) / 2) / w
            y_center = ((ymin + ymax) / 2) / h
            width = (xmax - xmin) / w
            height = (ymax - ymin) / h

            yolo_lines.append(f"{class_id} {x_center} {y_center} {width} {height}")

        yolo_file = os.path.join(yolo_labels_path, xml_file.replace(".xml", ".txt").replace(".html", ".txt"))
        with open(yolo_file, "w") as f:
            f.write("\n".join(yolo_lines))
