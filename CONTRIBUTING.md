# Contributing to KWGT Widgets

Thank you for your interest in contributing to the KWGT Widgets project! Below are the steps and guidelines to help you get started.

---

## How to Contribute

1. **Fork the Repository**  
   - Click on the `Fork` button at the top-right of the repository page.
   
2. **Clone Your Fork**  
   - Clone your fork to your local machine:
     ```bash
     git clone https://github.com/AumGupta/KWGT-Widgets.git
     ```
   
3. **Create a Branch**  
   - Create a branch for your changes:
     ```bash
     git checkout -b feature/your-feature-name
     ```

4. **Make Changes**  
   - Make your changes to the widgets.  
   - Ensure that widgets are **unlocked** before adding them to the repository.  
   - If you create a new widget, include a `.png` preview in the `previews/` folder.

> [!CAUTION]
> Strictly adhere by the [Guidelines](#guidelines) given at the end of this file.

5. **Test Your Changes**  
   - Verify that your widget works correctly in the KWGT app.

6. **Commit and Push**  
   - Commit your changes:
     ```bash
     git add .
     git commit -m "Add: description of changes"
     ```
   - Push your branch:
     ```bash
     git push origin feature/your-feature-name
     ```

7. **Submit a Pull Request**  
   - Go to the main repository and click the `Pull Request` tab.  
   - Submit your pull request for review. Provide a clear description of the changes you've made.

---

## Suggestions for Contributors

- Propose new widget ideas in the [Issues](../../issues) section.
- Enhance existing widgets by adding features or improving designs.
- Update the documentation to improve clarity or fix errors.

---

## Guidelines

- Strictly follow the below **naming convention**:
  - For **Widgets**:
    - Capitalize each word.
    - Separate them using underscore.
    - E.g. `My_First_Widget.kwgt`.
  - For **Previews**:
    - Use the exact same name for Light theme.
    - Add `Dark` prefix for Dark theme.
    - For example:
    - Light: `My_First_Widget.kwgt.png`
    - Dark: `My_First_WidgetDark.kwgt.png`
- Follow the existing folder structure (`widgets/`, `docs/previews/`, `fonts/`).
- Keep your commits focused on a single widget or fix.
