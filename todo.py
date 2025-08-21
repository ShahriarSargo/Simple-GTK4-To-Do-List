import gi
import os
import datetime

# I know this code is bad. No need to tell me.

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Pango

TASK_FILE = "tasks.txt"

class TodoApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.example.todo")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.window = Gtk.ApplicationWindow(application=self)
        self.window.set_title("To-Do List")
        self.window.set_default_size(500, 400)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox.set_margin_top(10)
        self.vbox.set_margin_bottom(10)
        self.vbox.set_margin_start(10)
        self.vbox.set_margin_end(10)
        self.window.set_child(self.vbox)

        # header bar for add button
        header = Gtk.Box(spacing=10)
        add_button = Gtk.Button.new_from_icon_name("list-add")
        add_button.connect("clicked", self.show_add_dialog)
        header.append(add_button)
        self.vbox.append(header)

        # list box for taks
        self.listbox = Gtk.ListBox()
        self.vbox.append(self.listbox)

        self.load_tasks()
        self.window.present()

    def show_add_dialog(self, button):
        dialog = Gtk.Dialog(transient_for=self.window, modal=True)
        dialog.set_title("New Task")

        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        content_box.set_margin_top(15)
        content_box.set_margin_bottom(15)
        content_box.set_margin_start(15)
        content_box.set_margin_end(15)

        entry = Gtk.Entry()
        entry.set_placeholder_text("Enter task description")
        entry.set_hexpand(True)
        content_box.append(entry)

        btn_box = Gtk.Box(spacing=10)
        ok_btn = Gtk.Button.new_with_label("Add")
        cancel_btn = Gtk.Button.new_with_label("Cancel")
        btn_box.append(ok_btn)
        btn_box.append(cancel_btn)
        content_box.append(btn_box)

        dialog.set_child(content_box)

        def add_clicked(btn):
            text = entry.get_text().strip()
            if text:
                self.add_task(text)
            dialog.destroy()

        def cancel_clicked(btn):
            dialog.destroy()

        ok_btn.connect("clicked", add_clicked)
        cancel_btn.connect("clicked", cancel_clicked)

        dialog.show()

    def add_task(self, text, done=False, created_at=None):
        if not created_at:
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(spacing=5)

        # Checkbox
        check = Gtk.CheckButton()
        check.set_active(done)
        check.connect("toggled", self.on_task_toggled, row)
        hbox.append(check)

        # Task label with creation date
        label = Gtk.Label(label=f"{text} ({created_at})", xalign=0)
        label.set_hexpand(True)
        if done:
            attr_list = Pango.AttrList()
            attr_list.insert(Pango.attr_strikethrough_new(True))
            label.set_attributes(attr_list)

        row.task_label = label
        row.task_check = check
        row.task_text = text
        row.task_done = done
        row.task_created = created_at
        hbox.append(label)

        # mark as done
        done_btn = Gtk.Button.new_from_icon_name("emblem-ok-symbolic")
        done_btn.connect("clicked", lambda b: check.set_active(True))
        hbox.append(done_btn)

        # deleting item
        delete_btn = Gtk.Button.new_from_icon_name("user-trash-symbolic")
        delete_btn.connect("clicked", self.delete_task_row, row)
        hbox.append(delete_btn)

        row.set_child(hbox)
        self.listbox.append(row)
        self.save_tasks()

    def on_task_toggled(self, check, row):
        label = row.task_label
        done = check.get_active()
        row.task_done = done
        if done:
            attr_list = Pango.AttrList()
            attr_list.insert(Pango.attr_strikethrough_new(True))
            label.set_attributes(attr_list)
        else:
            label.set_attributes(None)
        self.save_tasks()

    def delete_task_row(self, button, row):
        self.listbox.remove(row)
        self.save_tasks()

    def save_tasks(self):
        tasks = []
        child = self.listbox.get_first_child()
        while child:
            tasks.append(f"{child.task_done}|{child.task_text}|{child.task_created}")
            child = child.get_next_sibling()
        with open(TASK_FILE, "w") as f:
            f.write("\n".join(tasks))

    def load_tasks(self):
        if not os.path.exists(TASK_FILE):
            return
        with open(TASK_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 3:
                    done_str, text, created = parts
                elif len(parts) == 2:
                    done_str, text = parts
                    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                else:
                    continue
                self.add_task(text, done_str == "True", created)

app = TodoApp()
app.run()

# Apni ei code ti mere dite paren amar kono apotti nei.
# moyla ala der ke moyla niye jawar jonno w manush taka dey.
# ar apni amar moyla free te niye nicchen! Dhonnogood.
