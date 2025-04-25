import os
import json

WIDGETS_DIR = "widgets"
PREVIEWS_DIR = "docs/previews"
OUTPUT_JSON = "docs/js/widgets.json"

def generate_widget_list():
    widgets = []

    files = [
        (file, os.path.getmtime(os.path.join(WIDGETS_DIR, file)))
        for file in os.listdir(WIDGETS_DIR)
        if file.endswith(".kwgt")
    ]

    files.sort(key=lambda x: x[1], reverse=True)

    for file, _ in files:
        widget_name = file.replace(".kwgt", "")
        link = f"https://github.com/AumGupta/KWGT-Widgets/tree/main/widgets/{file}"
        light_image = f"{widget_name}.kwgt.png"
        dark_image = f"{widget_name}Dark.kwgt.png"
        if not os.path.exists(os.path.join(PREVIEWS_DIR, dark_image)):
            dark_image = light_image
        widgets.append({
            "name": widget_name.replace("_", " "),
            "link": link,
            "lightImage": light_image,
            "darkImage": dark_image,
            "size": "1x1"
        })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(widgets, f, indent=4)

    print("widgets.json updated.")

if __name__ == "__main__":
    generate_widget_list()
