import requests
import json
import tkinter as tk
from tkinter import ttk, scrolledtext

def get_news():
    country = country_var.get().strip().lower()
    if len(country) != 2:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid 2-letter country code.\n")
        return

    api_key = "ac7eb036beaf48568b608d73286d2cc9"
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    
    if r.status_code != 200:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Failed to retrieve news. Please check your internet connection or API key.\n")
        return
    
    news = json.loads(r.text)
    
    result_text.delete(1.0, tk.END)
    for article in news.get("articles", []):
        title = article.get("title", "No Title")
        description = article.get("description", "No Description")
        result_text.insert(tk.END, f"Title: {title}\nDescription: {description}\n")
        result_text.insert(tk.END, "-" * 80 + "\n")

# Create the main window
root = tk.Tk()
root.title("Daily News App")

# Create a label and entry for the country code
ttk.Label(root, text="Enter 2-letter country code:").grid(column=0, row=0, padx=10, pady=10)
country_var = tk.StringVar()
country_entry = ttk.Entry(root, width=5, textvariable=country_var)
country_entry.grid(column=1, row=0, padx=10, pady=10)

# Create a button to fetch the news
fetch_button = ttk.Button(root, text="Fetch News", command=get_news)
fetch_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

# Create a scrolled text box to display the results
result_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
result_text.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
