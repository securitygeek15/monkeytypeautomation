# monkeytypeautomation

A simple Python script that **automates typing on [Monkeytype](https://monkeytype.com)** using Selenium.  
It opens the site, accepts cookies, retrieves words, and simulates **human-like typing** with random delays.  

---

## Features
- Uses Selenium with Microsoft Edge WebDriver.
- Automatically accepts cookies (if prompted).
- Collects all words from the test page.
- Types words with **randomized delays** for realistic typing behavior.
- Works out-of-the-box, no config files needed.

---

## Quick Start
```bash
# clone the repository
git clone https://github.com/securitygeek15/monkeytypeautomation.git
cd monkeytypeautomation

# install dependencies
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
pip install selenium
```

---

## Usage
1. **Download Edge WebDriver**:  
   - Go to: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Make sure its version matches your installed Edge browser.  
   - Add the driver to your PATH or keep it in the same folder as the script.

2. **Run the script**:
```bash
python run_monkeytype.py
```

The script will:
- Open Monkeytype
- Accept cookies
- Retrieve words
- Type them automatically

---

## Code Overview
Main functions in the script:
- `open_monkeytype()` → opens Monkeytype in Edge.
- `accept_cookies()` → accepts cookie popup if present.
- `get_words()` → grabs words from the page.
- `type_words()` → types each word with random delays.
- `main()` → main automation flow.

---

## Example Output
```
[INFO] Cookies accepted.
[INFO] Automation complete.
```
