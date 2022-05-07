import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    """
    tkinter example app with OOP
    """

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=100)
        container.grid_columnconfigure(0, weight=300)

        self.frames = {}

        for frame_class in (StartPage, PageOne, PageTwo):

            frame = frame_class(container, self)

            self.frames[frame_class] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """
        Put specific frame on top
        """

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    """
    Starting frame for app
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="grey")
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.title("Sistema Mercado")
        label.pack(pady=10, padx=10)

        button_page1 = tk.Button(
            self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne)
        )
        button_page1.pack()

        button_page2 = tk.Button(
            self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo)
        )
        button_page2.pack()


class PageOne(tk.Frame):
    """
    First page of program
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="light blue")
        label = tk.Label(self, text="Page one", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button_home = tk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button_home.pack()

        button_home = tk.Button(
            self, text="Go to page2", command=lambda: controller.show_frame(PageTwo)
        )
        button_home.pack()


class PageTwo(tk.Frame):
    """
    First page of program
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="light green")
        label = tk.Label(self, text="Page two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button_home = tk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button_home.pack()

        button_home = tk.Button(
            self, text="Go to page1", command=lambda: controller.show_frame(PageOne)
        )
        button_home.pack()


app = SeaofBTCapp()
app.mainloop()
