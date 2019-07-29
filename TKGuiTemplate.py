import tkinter as tk
from tkinter import filedialog as fd    # for get End of (Pipe or Textfield)
from PIL import Image

# template for simple GUI using TK.
# by Don the Cat  (Git)


class TemplateTKGui:
    def __init__(self, title="Title! Yeah Buddy"):
        self.root = tk.Tk()
        self.root.title(title)

        #   init frame
        self.frame_top = tk.Frame(self.root)

        self.frame_mid = tk.Frame(self.root)
        self.frame_sub_textInput = tk.Frame(self.frame_mid)
        self.frame_sub_textInput_buttons = tk.Frame(self.frame_mid)
        self.frame_sub_outputText = tk.Frame(self.frame_mid)

        self.frame_bot = tk.Frame(self.root)    # currently not used.

        #   super grid layout frame
        self.frame_top.grid(row=0)

        self.frame_mid.grid(row=1)
        self.frame_sub_textInput.grid(row=0, column=0)
        self.frame_sub_textInput_buttons.grid(row=1, column=0,
                                              sticky='w')  # sticky = stick to... 'w' west oder 'e' east
        self.frame_sub_outputText.grid(row=0, column=1)

        self.frame_bot.grid(row=2)


        # info text
        info_text = "any info text"
        self.widget_info = tk.Label(self.frame_top, justify=tk.LEFT, text=info_text)

        #   image
        image_path = "theCatDon.png"
        resizeW = 50
        resizeH = 50
        self.img = Image.open(image_path)
        self.img = self.img.resize((resizeW, resizeH), Image.ANTIALIAS)
        image_path_resized = "tmp_img_resize.png"
        self.img.save(image_path_resized, "png")
        self.img = tk.PhotoImage(file=image_path_resized)

        self.widget_img = tk.Label(self.frame_top, image=self.img)

        # layout info and img grid
        self.widget_info.grid(row=0, column=0)  # row = 0 is top grid
        self.widget_img.grid(row=0, column=1)

        #   text input
        self.widget_text_input = tk.Text(self.frame_sub_textInput)
        self.widget_text_input.config(width=80)
        self.widget_text_input.grid(row=0, column=0)

        #   text button
        self.button_text_input = tk.Button(self.frame_sub_textInput_buttons, text="Enter", command=lambda: self.evt_button_enter_in_text_input())
        self.button_clear_text = tk.Button(self.frame_sub_textInput_buttons, text="Clear", command=lambda: self.evt_button_clear_text_input())
        self.button_text_input.grid(row=0, column=0, padx=3)
        self.button_clear_text.grid(row=0, column=1, padx=3)

        #   text output
        self.widget_text_output = tk.Text(self.frame_sub_outputText)
        self.widget_text_output.config(width=20)
        self.widget_text_output.grid(row=0, column=0)

    def evt_button_clear_text_input(self):
        self.widget_text_input.delete("1.0", fd.END)

    def evt_button_enter_in_text_input(self):
        text_input = self.widget_text_input.get("1.0", "end-1c")
        self.evt_button_clear_text_input()

        self.evaluate_input(text_input)

    def evaluate_input(self, text=""):
        self.widget_text_output.delete("1.0", "end")

        if text.__len__() is 0:
            self.widget_text_output.insert("1.0", "empty text bruh")
            return 0
        self.widget_text_output.insert("1.0", "wow!")
        return 0

    def start(self):
        self.root.mainloop()
        return ""


def main():
    pg = TemplateTKGui()
    pg.start()


if __name__ == '__main__':
    main()

