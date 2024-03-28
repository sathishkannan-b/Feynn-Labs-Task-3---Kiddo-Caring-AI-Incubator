#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

class AIIncubatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kiddo Caring AI Incubator")
        
        self.health_data_label = tk.Label(master, text="Health Data:")
        self.health_data_label.pack()

        self.health_data_text = tk.Text(master, height=5, width=50)
        self.health_data_text.pack()

        self.update_health_data_button = tk.Button(master, text="Update Health Data", command=self.update_health_data)
        self.update_health_data_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.incubator = AIIncubator()

    def update_health_data(self):
        self.incubator.update_health_data()
        health_data = self.incubator.get_health_data()
        self.health_data_text.delete(1.0, tk.END)
        for key, value in health_data.items():
            self.health_data_text.insert(tk.END, f"{key}: {value}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = AIIncubatorApp(root)
    root.mainloop()

