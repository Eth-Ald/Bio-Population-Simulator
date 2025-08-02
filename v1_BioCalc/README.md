# Bio-Population-Simulator v1

**Version:** 1.0  
**Language:** Python 3  
**Status:** Feature complete (v1)  
**Author:** Ethan Aldridge

---

## Overview

The main goal of this project is to simulate and visualize population dynamics of biological cells over time, with exponential growth and periodic decay. This tool was developed to serve as a foundation for more advanced modeling and analysis, and to provide a structured environment for practicing Python development, user input handling, data visualization, and file-based persistence.

---

## Features

- Run simulations using custom parameters:
  - Initial population
  - Growth rate
  - Total number of time steps
  - Decay interval and decay percentage
- Realtime graph plotting using Matplotlib
- Save simulation results to disk as JSON
- File overwrite protection with user prompts
- Load and replot previous simulation runs
- Menu based user interface
- Compatible with both X11 and Wayland Linux environments

---

## Requirements

- Python 3.10+
- `matplotlib` (Qt5Agg backend preferred)

To install dependencies:
```bash
pip install matplotlib

```
## Running the Program
Execute the script with Python:
```bash
python3 v1_BioCalc.py
```
On startup the menu will prompt:
```csharp
[1] Run new simulation
[2] Load saved simulation
[3] Exit
```
Choose an option and follow the instructions from the terminal.
Saved simulations are stored in the saved_runs/ directory.

## Project Structure
```text
cell-growth-simulator/
|--- growth_simulator.py        # Main Python script
|--- saved_runs/                # Automatically created to store saved data
|___ README.md                  # Project documentation
```

## Design & Challenges

### Scope Management for Version 1

**Reflection:**
There were many potential features (sorting, config files, batch simulations), but including them all in this version risked scope creep.

### Input Validation

**Challenge:**
Making sure the program only accepts numeric input for each parameter.

**Solution:**
Wrapped input parsing into a try/except block and returned 'None' on 'ValueError'.

**Reasoning:**
This guards against common input errors. Noted a more advanced input system with type checkings loops or CLI flags to be added in future versions.

### Parameter Handling with Tuple Unpacking

**Challenge:**
Managing all user defined parameters without cluttering function calls.

**Solution:**
Grouped all parameters into a tuple and used unpacking (*inputs) when passing them to functions.

**Reasoning:**
This keeps things clean and flexible with clearly named local variables. It also makes it easier to expand the number of parameters later.

### Automatic Save Directory Creation

**Challenge:**
Ensuring the target directory for saved data exists.

**Solution:**
Used 'os.makedirs(save_dir, exist_ok=True)' to automatically create the folder if missing.

### File Saving & Overwriting

**Challenge:**
Initially, the save function risked overwriting existing files without warning:
```python
file_path = os.path.join(save_dir, f"{filename}.json")
with open(file_path, "w") as f:
    json.dump(run_data, f, indent=4)
```
**Improvement:**
This was replaced with a loop that ensures safe user confirmed filenames:
```python
while True:
    filename = input("Enter a name for this run: ").strip()
    file_path = os.path.join(save_dir, f"{filename}.json")

    if os.path.exists(file_path):
        choice = input(f"File exists. Overwrite? (y/n): ").lower()
        if choice != "y":
            continue
    break
```

### Plot Display Flow: Blocking or Not Blocking

**Challenge:**
Initially, the plot was displayed using a non blocking call in favor of better flow:

```python
plt.show(block=False)
```
This was implemented to keep the terminal accessible while the graph window stayed open. However, this introduced instability from certain backend compatibility issues (e.g. Qt5Agg on Wayland)

**Solution:**
plt.show was reverted back to the default blocking behaviour and the terminal prompts the user to close the graph window to proceed.

### Sorting System for Saved Data

**Consideration:**
For future compatibility with a large number of saved simulation runs a sorting system was considered to allow ordering saved runs by metadata such as final population size, number of time steps, and creation date.

**Decision:**
Postponed this feature for a future version. In this version, saved files are listed in alphabetical order by default. However, the save format was designed with extendibility in mind with the strcuture of JSON files allowing for easy addition of a "final_population" or "timestamp" key in future without breaking compatibility.

**Reasoning:**
Adding a sorting system at this stage would not provide significant benefit for the initial version as large datasets aren't likely and would only increase complexity.

### Wayland Compatibility & Qt Warnings

**Challenge:**
While testing in a Wayland based Linux environment, a Qt5Agg warning was printed in the terminal:
qt.qpa.wayland: Wayland does not support QWindow::requestActivate()

This message comes from the Matplotlib backend Qt5Agg when attempting to focus the plot window. It does not effect functionality but clutters the terminal.

**Solution:**
When a Wayland OS environment is detected to be running the script, a notice is printed stating some window focus features may be unavailable and the raw Qt warning is suppressed.

```python
if os.environ.get("XDG_SESSION_TYPE") == "wayland":
    print("(Notice: Running under Wayland. Some window focus features may be unavailable.)")

os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"
```
This does not mute critical errors.

## Author Notes
This version was developed as a personal task for learning scientific programming and modular python development. The goal was to build a stable, extendible foundation for future simulation tools and data analysis.
Feedback & Suggestions are very welcome.
