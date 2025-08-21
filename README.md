---

# To-Do List App 📝

A simple, cross-platform To-Do List application built with Python and GTK 4. Allows you to manage tasks, mark them as done, and store task creation dates.

---

## Features ✨

* **Add new tasks** with a descriptive name.
* **Mark tasks as done**, which moves them to a "Done" category.
* **Delete tasks** individually.
* **Persistent storage** — tasks are saved automatically in `tasks.txt`.
* **Cross-platform GUI** using Python and GTK 4.

---

## Installation 🛠️

### Dependencies (Linux)

To run the application, ensure the following dependencies are installed:

#### Debian / Ubuntu

sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-4.0

#### Fedora / RHEL / CentOS

sudo dnf install python3-gobject gtk4

#### Arch Linux / CachyOS / Manjaro / EndeavourOS / Garuda

sudo pacman -Syu --needed python-gobject gtk4

#### 1. After installing dependencies, Download the binary from releases, extract if needed, and run the executable
Installing on **Windows:**
   1. Install Python 3.x from python.org
   2. Install GTK 4 runtime via MSYS2 (for PyGObject).
   3. Run the app:
      python todo.py

---

## Usage 🚀

1. **Add a task:** Click the **+** button → enter the task name → click **Add**.

2. **Mark as done:** Click the **✓** button next to a task → it moves to "Done".

3. **Delete a task:** Click the **🗑️** button to remove a task.

*All tasks are saved automatically in `tasks.txt`.*

---

## File Storage 📂

* **tasks.txt** stores tasks with their status and creation time:

* False|Buy groceries|2025-08-21 12:00:00
* True|Finish homework|2025-08-21 12:30:00

---

## Screenshots 📸

To add screenshots to your GitHub repository:

1. **Create a folder** named `screenshots` in the root directory of your repository.

2. **Add your images** (e.g., `screenshot1.png`, `screenshot2.png`) to this folder.

3. **Reference images in README.md** using Markdown syntax:


![Add Task](screenshots/screenshot1.png)
![Mark as Done](screenshots/screenshot2.png)


*Ensure the image files are committed to your repository so they are accessible.*

---

## Testing Environment 🧪

*This application has been tested on Linux systems only.*

---

© Shahriar Sargo

---
