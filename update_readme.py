import os
import re
import sys

README_PATH = "README.md"
WIDGETS_DIR = "widgets"
PREVIEWS_DIR = "previews"

def get_existing_widgets():
    """Extracts existing widget names from README to avoid duplicates."""
    if not os.path.exists(README_PATH):
        return set()
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    return set(re.findall(r"- ### \[(.*?)\]", content))

def get_widget_details():
    """Scans the widgets directory and finds matching previews."""
    widgets = []
    existing_widgets = get_existing_widgets()
    print(existing_widgets)

    for file in sorted(os.listdir(WIDGETS_DIR)):
        if file.endswith(".kwgt"):
            widget_name = file.replace(".kwgt", "")
            if widget_name in existing_widgets:
                continue  # Skip if already in README
            
            dark_preview = f"{widget_name}_Dark.kwgt.png"
            light_preview = f"{widget_name}_Light.kwgt.png"
            
            if dark_preview in os.listdir(PREVIEWS_DIR) and light_preview in os.listdir(PREVIEWS_DIR):
                widgets.append(widget_name)

    return widgets

def append_to_readme(widgets):
    """Appends new widgets to the README file."""
    if not widgets:
        print("No new widgets found.")
        return False

    with open(README_PATH, "a", encoding="utf-8") as f:
        for widget in widgets:
            f.write(f"\n- ### [{widget}](widgets/{widget}.kwgt)\n")
            f.write(f"  \n  > <img src=\"previews/{widget}_Dark.kwgt.png\" alt=\"Preview\" style=\"width:200px;\"/> \n")
            f.write(f"  >\n  > **Dark Mode**\n  >\n")
            f.write(f"  > <img src=\"previews/{widget}_Light.kwgt.png\" alt=\"Preview\" style=\"width:200px;\"/> \n")
            f.write(f"  >\n  > **Light Mode**\n  >\n")
            f.write(f"  > A clean widget with dynamic themes.\n  > \n")
            f.write(f"  > **Key Feature:** Automatically adapts to system theme.\n")

    return True

if __name__ == "__main__":
    new_widgets = get_widget_details()
    if append_to_readme(new_widgets):
        print("README updated with new widgets.")
        sys.exit(0)
    else:
        print("No updates made.")
        sys.exit(1)
