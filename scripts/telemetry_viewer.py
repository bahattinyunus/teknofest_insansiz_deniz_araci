import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_telemetry(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    print(f"--- Analyzing Telemetry: {file_path} ---")
    df = pd.read_csv(file_path)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Velocity and Heading
    ax1.plot(df['timestamp'], df['velocity'], label='Velocity (m/s)', color='blue')
    ax1.set_ylabel('Velocity', color='blue')
    ax1.legend(loc='upper left')

    ax1_2 = ax1.twinx()
    ax1_2.plot(df['timestamp'], df['heading'], label='Heading (deg)', color='red', linestyle='--')
    ax1_2.set_ylabel('Heading', color='red')
    ax1_2.legend(loc='upper right')

    # Battery Status
    ax2.plot(df['timestamp'], df['voltage'], label='Voltage (V)', color='green')
    ax2.set_ylabel('Voltage', color='green')
    ax2.set_xlabel('Timestamp')
    ax2.legend(loc='upper left')

    ax2_2 = ax2.twinx()
    ax2_2.plot(df['timestamp'], df['current'], label='Current (A)', color='orange')
    ax2_2.set_ylabel('Current', color='orange')
    ax2_2.legend(loc='upper right')

    plt.title('USV Telemetry Analysis')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    output_img = file_path.replace('.csv', '.png')
    plt.savefig(output_img)
    print(f"Visualization saved to: {output_img}")
    plt.show()

if __name__ == "__main__":
    telemetry_file = os.path.join("docs", "reports", "sim_telemetry_001.csv")
    visualize_telemetry(telemetry_file)
