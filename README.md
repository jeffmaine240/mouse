
# 🖱️ Auto Mouse Activity Script

This script simulates periodic mouse activity (movement and scrolling) to keep your computer active. It's useful for preventing screen lock or idle status during long work sessions.

---

##  Step 1: Download the Project

Download this folder to your machine and open a terminal or PowerShell window in the project directory.

---

##  Step 2: Create a Virtual Environment

### 🪟 On Windows (PowerShell)

```powershell
python -m venv env\mouse
env\mouse\Scripts\Activate.ps1
```

> **Note:** If you see a security error when activating the virtual environment on **Windows**, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

```
###  On macOS 

Create and activate the virtual environment:

```bash
python3 -m venv env/mouse
source env/mouse/bin/activate
```
###  Step 3: Install Dependencies

After activating the virtual environment, run:

```bash
pip install -r requirements.txt
```
This will install necessary packages

---

###  Step 4: Run the Script

```bash
python mouse_scroll.py
```

The script will:

- Move the mouse to the center of the screen  
- Scroll up and down to simulate activity  
- Repeat at a fixed interval (e.g. every 15 minutes)

###  How to Stop the Script

Press `Ctrl + C` in the terminal or PowerShell window to stop it.

---

### Customization

You can adjust the behavior of the script by modifying the following line inside `mouse_scroll.py`:

```python
stay_active(interval_minutes=15, max_runtime_minutes=480)
```