import os
import re
import sys

README_PATH = "README.md"
WIDGETS_DIR = "widgets"
PREVIEWS_DIR = "docs/previews"

def get_widget_count():
    """Counts the number of .kwgt files in the widgets directory."""
    return len([file for file in os.listdir(WIDGETS_DIR) if file.endswith(".kwgt")])

def update_widget_count():
    """Updates the widget count badge in the README."""
    if not os.path.exists(README_PATH):
        return
    
    widget_count = get_widget_count()
    new_badge = f"![Widget Count](https://img.shields.io/badge/widget%20Count-{widget_count}-blue?style=social&link=https%3A%2F%2Fgithub.com%2FAumGupta%2FKWGT-Widgets%2Ftree%2Fmain%2Fwidgets)"

    with open(README_PATH, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        updated_lines = [new_badge + "\n" if line.startswith("![Widget Count]") else line for line in lines]

        if lines != updated_lines:
            f.seek(0)
            f.writelines(updated_lines)
            f.truncate()
            print(f"Updated widget count badge to {widget_count}")
        else:
            print("Widget count badge is already up to date.")

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

    for file in sorted(os.listdir(WIDGETS_DIR)):
        if file.endswith(".kwgt"):
            widget_name = file.replace(".kwgt", "").replace('_', ' ')  # Normalize name

            if widget_name in existing_widgets:
                continue  # Skip if already in README

            dark_preview = f"{file.replace('.kwgt', '')}Dark.kwgt.png"
            light_preview = f"{file.replace('.kwgt', '')}.kwgt.png"

            dark_exists = dark_preview in os.listdir(PREVIEWS_DIR)
            light_exists = light_preview in os.listdir(PREVIEWS_DIR)

            widgets.append((widget_name, dark_preview if dark_exists else None, light_preview if light_exists else None))

    return widgets

def append_to_readme(widgets):
    """Appends new widgets to the README file."""
    if not widgets:
        print("No new widgets found.")
        return False

    with open(README_PATH, "a", encoding="utf-8") as f:
        for widget_name, dark_preview, light_preview in widgets:
            f.write(f"\n- ### [{widget_name}](widgets/{widget_name.replace(' ', '_')}.kwgt)\n")

            if dark_preview and light_preview:
                # If both previews exist, use table format
                f.write(f"  > | <img src='docs/previews/{light_preview}' alt='Light Preview' style='width:200px;'/> | <img src='docs/previews/{dark_preview}' alt='Dark Preview' style='width:200px;'/> |\n")
                f.write("  > |-------|------|\n")
                f.write("  > | Light | Dark |\n")
            elif light_preview:
                # Only Light Mode available
                f.write(f"  > <img src='docs/previews/{light_preview}' alt='Light Preview' style='width:200px;'/>\n")
            elif dark_preview:
                # Only Dark Mode available
                f.write(f"  > <img src='docs/previews/{dark_preview}' alt='Dark Preview' style='width:200px;'/>\n")

            f.write("  >\n  > A clean widget with dynamic themes.\n  > \n")
            f.write("  > **Key Feature:** Automatically adapts to system theme.\n")

    return True

if __name__ == "__main__":
    update_widget_count()
    new_widgets = get_widget_details()
    if append_to_readme(new_widgets):
        print(f"README updated with {len(new_widgets)} new widgets.")
        sys.exit(0)
    else:
        print("No updates made.")
        sys.exit(1)
