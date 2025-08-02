"""
Bio Cell Growth Simulation
Description: 
    Simulates the growth of a population of cells over time with periodic delay based on
    user-defined parameters. 
    Output in the form of a json file can be saved & loaded via the menu loop.
"""
import matplotlib.pyplot as plt
import os
import json

#Wayland debug
os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false"
if os.environ.get("XDG_SESSION_TYPE") == "wayland":
    print("(Notice: Running under Wayland. Some window focus features may be unavailable.)")


# -- Functions

def run_simulation(initial_population, growth_rate, time_steps, decay_interval, decay_percent):
    #Run the simulation over defined time steps with growth and decay events.
    time_data = []
    population_data = []
    population = initial_population
    for step in range(1, time_steps + 1):
        #Apply Growth
        population *= (1 + growth_rate)
        #Apply Decay
        if step % decay_interval == 0:
            population *= (1 - decay_percent)
        
        #Store change from this step
        time_data.append(step)
        population_data.append(population)
       #print(f"Step {step}: Population = {population:.2f}")
    return time_data, population_data

def plot_results(time_data, population_data):
    #Plot population/time
    plt.plot(time_data, population_data, marker='o')

    #Labels & Titles
    plt.title("Simulated Cell Population Growth")
    plt.xlabel("Time Steps")
    plt.ylabel("Population")
    plt.grid(True)

    #Show plotting window.
    plt.show() #Considered block=False but decided against for stability.

def get_user_input():
    #Prompt the user for parameters and return them as a tuple.
    try:
        initial_population = int(input("Initial Population "))
        growth = float(input("Growth rate (e.g. 0.2 for 20%): "))
        steps = int(input("Total time steps: "))
        decay_step = int(input("Decay interval (e.g. every 10 steps): "))
        decay_percent = float(input("Decay percent (e.g. 0.3 for 30%): "))
    except ValueError:
        print("Input valid values for all parameters.")
        return None
    return initial_population, growth, steps, decay_step, decay_percent

def save_simulation(inputs, time_data, population_data):
    #Unpack parameters from inputs.
    initial_population, growth_rate, time_steps, decay_interval, decay_percent = inputs
    save_dir = "saved_runs" #Creates save directory if it doesn't exist.
    os.makedirs(save_dir, exist_ok=True)

    while True:
        filename = input("Enter a name for this run (no spaces, no extension): ").strip()
        if not filename:
            print("Save cancelled: no name given.")
            continue
        
        file_path = os.path.join(save_dir, f"{filename}.json")

        #Check if file already exists.
        if os.path.exists(file_path):
            choice = input(f"A file named '{filename}.json' already exists. Overwrite? (y/n): ").strip().lower()
            if choice != 'y':
               print("Please enter a different name.")
               continue #Return to prompt
        break #Valid name or overwrite approved.

    #Create dictionary of data
    run_data = {
        "name": filename,
        "initial_population": initial_population,
        "growth_rate": growth_rate,
        "time_steps": time_steps,
        "decay_interval": decay_interval,
        "decay_percent": decay_percent,
        "time_data": time_data,
        "population_data": population_data
    }
    #Create file path & save as JSON
    with open(file_path, "w") as f:
        json.dump(run_data, f, indent=4)
    print(f"Run saved as {file_path}")

def load_saved_simulation():
    #List saved simulation files, allow user to select and plot one.
    save_dir = "saved_runs"
    if not os.path.exists(save_dir):
        print("No saved data found.")
        return
    files = [f for f in os.listdir(save_dir) if f.endswith(".json")]
    if not files:
        print("No saved runs found.")
        return
    print("\nAvailable Saved Runs:")
    for i, file in enumerate(files, 1):
        print(f"[{i}] {file}")

    try:
        choice = int(input("Select a run to load (number): "))
        if 1 <= choice <= len(files):
            file_path = os.path.join(save_dir, files [choice - 1])
            with open(file_path, "r") as f:
                data = json.load(f)
            print(f"Loaded '{files[choice - 1]}' successfully.")
            plot_results(data["time_data"], data["population_data"])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


#Main Block

if __name__ == "__main__":
    plt.switch_backend('Qt5Agg')

    while True:
        print("\n--- Cell Population Simulator ---")
        print("[1] Run new simulation")
        print("[2] Load saved simulation")
        print("[3] Exit")

        choice = input("Enter selection: ").strip()
        if choice == "1":
            inputs = get_user_input()
            if inputs:
                print(f"Running simulation with: {inputs}")
                time_data, population_data = run_simulation(*inputs)
                plot_results(time_data, population_data)
                print("(Close the graph window to proceed.)")
                save_simulation(inputs, time_data, population_data)

        elif choice == "2":
            load_saved_simulation()
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

