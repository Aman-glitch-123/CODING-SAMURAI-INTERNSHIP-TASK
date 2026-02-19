import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        result_label.config(
            text=f"Temperature: {temp}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Condition: {condition}"
        )
    else:
        result_label.config(text="City not found!")

root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")

tk.Label(root, text="Enter City", font=("Arial", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack()

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
