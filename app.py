import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher
from tkinter import messagebox
import requests
import json
import pyfiglet

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        self.button1 = tk.Button(self.frame, text="From Whole Server", command=self.open_gui1)
        self.button1.pack()
        
        self.button2 = tk.Button(self.frame, text="One-To-One", command=self.open_gui2)
        self.button2.pack()
        
    def open_gui1(self):
        self.frame.pack_forget()  # Hide the main menu
        gui1 = Gui1(self.master)
        
    def open_gui2(self):
        self.frame.pack_forget()  # Hide the main menu
        gui2 = Gui2(self.master)

class Gui1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        

        def check_plagiarism():
            text_to_check = text_entry.get("1.0", "end-1c")
            
            burp0_url = "https://papersowl.com:443/plagiarism-checker-send-data"
            burp0_cookies = {"PHPSESSID": "qjc72e3vvacbtn4jd1af1k5qn1", "first_interaction_user": "%7B%22referrer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22internal_url%22%3A%22%5C%2Ffree-plagiarism-checker%22%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_content%22%3Anull%2C%22utm_term%22%3Anull%2C%22gclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22adgroupid%22%3Anull%2C%22targetid%22%3Anull%2C%22appsflyer_id%22%3Anull%2C%22appsflyer_cuid%22%3Anull%2C%22cta_btn%22%3Anull%7D", "first_interaction_order": "%7B%22referrer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22internal_url%22%3A%22%5C%2Ffree-plagiarism-checker%22%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_content%22%3Anull%2C%22utm_term%22%3Anull%2C%22gclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22adgroupid%22%3Anull%2C%22targetid%22%3Anull%2C%22appsflyer_id%22%3Anull%2C%22appsflyer_cuid%22%3Anull%2C%22cta_btn%22%3Anull%7D", "affiliate_user": "a%3A3%3A%7Bs%3A9%3A%22affiliate%22%3Bs%3A9%3A%22papersowl%22%3Bs%3A6%3A%22medium%22%3Bs%3A9%3A%22papersowl%22%3Bs%3A8%3A%22campaign%22%3Bs%3A9%3A%22papersowl%22%3B%7D", "sbjs_migrations": "1418474375998%3D1", "sbjs_current_add": "fd%3D2022-05-24%2019%3A01%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F", "sbjs_first_add": "fd%3D2022-05-24%2019%3A01%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F", "sbjs_current": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29", "sbjs_first": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29", "sbjs_udata": "vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%206.3%3B%20Win64%3B%20x64%3B%20rv%3A100.0%29%20Gecko%2F20100101%20Firefox%2F100.0", "sbjs_session": "pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker", "_ga_788D7MTZB4": "GS1.1.1653411683.1.0.1653411683.0", "_ga": "GA1.1.1828699233.1653411683", "trustedsite_visit": "1", "trustedsite_tm_float_seen": "1", "AppleBannercookie_hide_header_banner": "1", "COOKIE_PLAGIARISM_CHECKER_TERMS": "1", "plagiarism_checker_progress_state": "1"}
            burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "*/*", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://papersowl.com/free-plagiarism-checker", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://papersowl.com", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers", "Connection": "close"}
            burp0_data = {"is_free": "false", "plagchecker_locale": "en", "product_paper_type": "1", "title": '', "text": text_to_check}

            r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
            result = json.loads(r.text)

            messagebox.showinfo("Plagiarism Check Result", f"Word count: {result['words_count']}\nSoSorry Index: {100 - float(result['percent'])}\nMatches: {result['matches']}")
            
        root = tk.Tk()
        root.title("SoSorry From Whole Server")

        # Add SoSorry banner
        banner = pyfiglet.figlet_format("SoSorry")
        banner_label = tk.Label(root, text=banner, font=("Courier", 12))
        banner_label.pack()

        # Text entry
        text_entry = tk.Text(root, height=10, width=50)
        text_entry.pack()

        # Button to check plagiarism
        check_button = tk.Button(root, text="Check Plagiarism", command=check_plagiarism)
        check_button.pack()

        root.mainloop()

class Gui2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        # Add GUI 2 components here
        def load_file(entry, text_widget):
            file_path = entry.get()
            if not file_path:
                file_path = filedialog.askopenfilename()
            if file_path:
                entry.delete(0, tk.END)
                entry.insert(tk.END, file_path)
                with open(file_path, 'r') as file:
                    text = file.read()
                    text_widget.delete(1.0, tk.END)
                    text_widget.insert(tk.END, text)

        def compare_text():
            text1 = text_box1.get(1.0, tk.END)
            text2 = text_box2.get(1.0, tk.END)
            similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
            similarity_percent = int(similarity_ratio * 100)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Similarity: {similarity_percent}%")

        root = tk.Tk()
        root.title("SoSorry One-To-One")

        frame1 = tk.Frame(root)
        frame1.pack(pady=10)

        entry1 = tk.Entry(frame1, width=50)
        entry1.grid(row=0, column=0, padx=(20, 0))
        load_button1 = tk.Button(frame1, text="Load File 1", command=lambda: load_file(entry1, text_box1))
        load_button1.grid(row=0, column=1, padx=(10, 20))

        text_box1 = tk.Text(frame1, width=50, height=10)
        text_box1.grid(row=1, column=0, columnspan=2, padx=(20, 0), pady=(10, 0))

        frame2 = tk.Frame(root)
        frame2.pack(pady=10)

        entry2 = tk.Entry(frame2, width=50)
        entry2.grid(row=0, column=0, padx=(20, 0))
        load_button2 = tk.Button(frame2, text="Load File 2", command=lambda: load_file(entry2, text_box2))
        load_button2.grid(row=0, column=1, padx=(10, 20))

        text_box2 = tk.Text(frame2, width=50, height=10)
        text_box2.grid(row=1, column=0, columnspan=2, padx=(20, 0), pady=(10, 0))

        compare_button = tk.Button(root, text="Compare", command=compare_text)
        compare_button.pack(pady=10)

        result_text = tk.Text(root, width=50, height=5)
        result_text.pack(pady=10)

        root.mainloop()

def main():
    root = tk.Tk()
    root.title("SoSorry")
    main_menu = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
