


I made a simple automated search bot built using Python and Selenium. It takes user input from the terminal and performs a web search in a Chrome browser.

## Features

- Prompts the user for search input.
- Automatically launches Chrome using Selenium.
- Performs a Google search with the given query.
- Opens the top result in a new browser tab (optional extension possible).
- Uses 'chromedriver' for automation.

## Technologies Used

- Python 
- [Selenium](https://www.selenium.dev/)
- ChromeDriver

## Requirements

- Google Chrome browser
- Compatible version of ChromeDriver (ensure it matches your Chrome version)
- Python packages:
  
  pip install selenium


## 📁 Project Structure


search_bot/
│

├── main.py                 # Main script for running the bot

├── chromedriver-win64/    # ChromeDriver folder (optional if installed globally)

│   └── chromedriver.exe

└── README.md               # Project documentation

## 📦 Setup Instructions

1. **Clone the repository:**

   
   git clone [https://github.com/IcarusKiyopon/search_bot.git](https://github.com/IcarusKiyopon/InstagramScraper)

   cd search_bot
   

3. **Install dependencies:**

   
   pip install selenium
   

4. **Download ChromeDriver:**

   * [Download here](https://sites.google.com/chromium.org/driver/)
   * Place the `chromedriver.exe` in the `chromedriver-win64` folder, or ensure it's in your system PATH.

5. **Run the bot:**

   
   python main.py
   

## 🙋‍♂️ Author

Made with ❤️ by [Icarus](https://github.com/IcarusKiyopon)
(me)
## 📄 License

This project is licensed under the MIT License.



