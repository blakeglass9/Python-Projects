import tkinter as tk
import webbrowser

class WebPageGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Page Generator")
        self.geometry("500x150")

        # Create label
        self.label = tk.Label(self, text="Enter custom text or click the Default HTML page button")
        self.label.pack(pady=10)

        # Create text entry field
        self.text_entry = tk.Entry(self, width=60)
        self.text_entry.pack(pady=5)

        # Create buttons
        self.default_button = tk.Button(self, text="Default HTML Page", command=self.defaultHTML)
        self.default_button.pack(side="left", padx=50, pady=20)

        self.submit_button = tk.Button(self, text="Submit Custom Text", command=self.submitCustomText)
        self.submit_button.pack(side="right", padx=50, pady=20)

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.createHTMLPage(htmlText)

    def submitCustomText(self):
        htmlText = self.text_entry.get()
        if htmlText.strip():
            self.createHTMLPage(htmlText)
        else:
            self.defaultHTML()

    def createHTMLPage(self, htmlText):
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    app = WebPageGenerator()
    app.mainloop()
