# Inflation Degradation Calculator

A simple graphical tool to calculate the future value of a given amount in today’s money after accounting for inflation degradation.\
Build native installers for Windows and macOS, or run directly with Python.

---

## Features

- Enter current amount (R) + inflation rate (%) + years → Get adjusted value in today’s money
- Shows up to three 5-year interval values and percentage loss in a neat table
- Cross-platform GUI built with Tkinter
- Native packaging: `.exe` for Windows, `.app`/`.dmg` for macOS
- Automated builds via GitHub Actions

## Prerequisites

- **Windows/macOS/Linux**: Python 3.7 or higher
- **Tkinter** (usually bundled with Python)
- **PyInstaller** (for packaging)
- **Inno Setup** (Windows installer, optional)
- **create-dmg** (macOS DMG creation, optional, requires Node.js)

## Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/YourUserName/InflationCalculator.git
   cd InflationCalculator
   ```

2. **Install Python dependencies**:

   ```bash
   pip install pyinstaller
   ```

3. **Run directly with Python**:

   ```bash
   python inflation_gui_calculator.py
   ```

## Usage

- Launch the app
- Enter the **Current Amount (R)**, **Inflation Rate (%),** and **Number of Years**
- Click **Calculate**
- View the main adjusted value and a table of 5-year interval values with % loss

## Building Native Executables

### Windows `.exe` with PyInstaller

1. Ensure `inflation_icon.ico` is in the project root
2. Run:
   ```bash
   pyinstaller --onefile --windowed --icon=inflation_icon.ico inflation_gui_calculator.py
   ```
3. The executable appears in `dist/inflation_gui_calculator.exe`

#### Creating an Installer with Inno Setup (optional)

1. Install [Inno Setup](https://jrsoftware.org/isdl.php) on Windows
2. Use the provided `installer.iss` script:
   ```ini
   [Setup]
   AppName=Inflation Calculator
   AppVersion=1.0
   DefaultDirName={autopf}\Inflation Calculator
   DefaultGroupName=Inflation Calculator
   OutputBaseFilename=InflationCalculatorSetup
   Compression=lzma
   SolidCompression=yes

   [Files]
   Source: "dist\\inflation_gui_calculator.exe"; DestDir: "{app}"; Flags: ignoreversion
   Source: "inflation_icon.ico";                 DestDir: "{app}"; Flags: ignoreversion

   [Icons]
   Name: "{group}\\Inflation Calculator"; Filename: "{app}\\inflation_gui_calculator.exe"; IconFilename: "{app}\\inflation_icon.ico"
   Name: "{commondesktop}\\Inflation Calculator"; Filename: "{app}\\inflation_gui_calculator.exe"; WorkingDir: "{app}"

   [Run]
   Filename: "{app}\\inflation_gui_calculator.exe"; Description: "Launch Inflation Calculator"; Flags: nowait postinstall skipifsilent
   ```
3. Compile `installer.iss` in Inno Setup IDE → Produces `InflationCalculatorSetup.exe`

### macOS `.app` and `.dmg`

1. Convert your PNG/ICO to `inflation_icon.icns` (online converter or macOS `iconutil`)
2. Run PyInstaller on macOS:
   ```bash
   pyinstaller --onefile --windowed \
     --icon=inflation_icon.icns \
     inflation_gui_calculator.py
   ```
3. Create a DMG using `create-dmg` (requires Node.js):
   ```bash
   create-dmg \
     --volname "Inflation Calculator" \
     --volicon inflation_icon.icns \
     --background background.png \
     --window-size 600 400 \
     --icon-size 100 \
     --icon "dist/inflation_gui_calculator.app" 200 200 \
     --app-drop-link 400 200 \
     dist/inflation_gui_calculator.app \
     InflationCalculator.dmg
   ```

## Continuous Integration (GitHub Actions)

A workflow (`.github/workflows/build.yml`) automates building:

- Windows `.exe`
- macOS `.app`

Artifacts are uploaded under the **Actions** tab or attached to releases.

## License

MIT License © 2025 YourName

---

*Feel free to open an issue or submit a pull request for enhancements!*

