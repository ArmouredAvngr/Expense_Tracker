# Personal Budget & Expense Tracker

A lightweight, cross-platform Python command-line utility that tracks your spending in real time, warns you if you exceed your budget, and exports every session's transactions to an Excel-ready `Expenses.csv` file in your `Documents` folder.

## 💰 Features
* **Real-Time Budget Tracking:** Automatically deducts each expense from your starting budget and alerts you if your balance drops below zero.
* **Fresh Session Logging:** Automatically resets `Expenses.csv` at the start of each run so every session generates a clean, dedicated expense report (`Category`, `Expense`, `Remaining Budget`).
* **Cross-Platform Compatibility:** Uses `os.path.expanduser` and `os.path.join` to locate any user's `Documents` folder automatically across Windows, macOS, and Linux.
* **Zero External Dependencies:** Built using only Python's standard `os` and `csv` modules.

## 🚀 How to Use

### Option 1: Windows Executable (No Python Required)
1. Go to the **Releases** section on the right side of this page.
2. Download the latest **`Expenses_Tracker.exe`** under **Assets**.
3. Double-click the file, enter your budget, and start logging expenses. *(Note: If Windows SmartScreen appears, click **More info → Run anyway**).*

### Option 2: Run via Python (Windows / macOS / Linux)
1. Download `Expenses_Tracker.py`.
2. Run the script in your terminal:
   ```bash
   python Expenses_Tracker.py
   ```
3. Open **`Expenses.csv`** inside your `Documents` folder using Excel, Google Sheets, or any text editor to view your session's saved report.
