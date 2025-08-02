# cell-growth-simulator

A python based simulation of cell growth with decay.

The main goal of this project is to visualise simulated population dynamics of biological cells over time. It also serves as a foundation for developing more advanced modeling and analysis tools, while providing a practical environment to establish and improve proficiency in python, data visualisation and related technologies for scientific computing.

This repository contains a collection of standalone editions of the project

## Project Versions

| Version  |         Folder         | Description                                                              |
|----------|------------------------|--------------------------------------------------------------------------|
|   'v1'   |  'v1_BioCalc'          | Simple simulation with input handling, graph, & save/load functions.     |
|   'v2'   |  'v2_BioCalc'          | Planned                                                                  |
|   'v3    |  'v3_BioCalc'          | Planned                                                                  |

## Version Goals

### Version 1 - Baseline Simulation Tool (Complete)
- Simulates biological cell-growth exponentially with user defined parameters. 
- Applies periodic decay events. 
- Visualises growth vs time using Matplotlib. 
- Built with modularity in mind for future development.
- Terminal-based menu.
- Save run data to .JSON file with filename input and overwrite protection.
- Load and replot saved simulation data.
- Surface level wayland debugging.
- Clean modular function design.

  ---

### Version 2 - More complex simulation and analysis (Planned)
  #Designed to transition to a more practical and versatile scientific tool.
- Higher detail of simulation model using larger & more realistic datasets.
- Implementation of NumPy and Pandas for performant analysis.
- Simple GUI.
- Export plots as PNG.
- Metadata display.
- Sorting system for saved runs based on parameters or outcomes to make large datasets more accessible.
- Support for user configuration.

### Version 3 - Planned

---

## Technologies Used
- Python 3.11+
- Matplotlib (Qt5Agg backend)
- JSON
- Built and tested on Arch Linux (Wayland)
- CLI interface
  
---

##Repository Structure

```
v1_BioCalc/
|--- saved_runs/        # Saved JSON simulation files
|--- v1_BioCalc.py      # Main program script
|___ README.md          # Project documentation










    
