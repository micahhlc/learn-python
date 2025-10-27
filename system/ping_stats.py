#!/usr/bin/env python3

import subprocess
import re
import sys
import numpy as np
import argparse

def run_stability_test(target: str, count: int):
    """
    Pings a target and calculates detailed latency statistics, including percentiles.
    """
    print("--- Starting Network Stability Test (Python Version) ---")
    print(f"Target:   {target}")
    print(f"Pinging:  {count} times")
    print("Progress: ", end='', flush=True) # end='' and flush=True keep dots on the same line

    # The command to run. '-c' is for count on macOS/Linux.
    ping_command = ["ping", "-c", str(count), target]
    latencies = []
    
    try:
        # Start the ping process
        # stdout=subprocess.PIPE allows us to capture the output.
        # text=True decodes the output as text.
        process = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Process the output line-by-line in real-time
        for line in process.stdout:
            # We print the original line so the user sees the ping output live
            print(line, end='')

            # Use a regular expression to find the time in lines like:
            # 64 bytes from 142.250.183.36: icmp_seq=1 ttl=118 time=8.43 ms
            match = re.search(r"time=([\d.]+)", line)
            if match:
                # If we find a match, extract the time (group 1), convert to float, and store it.
                latency = float(match.group(1))
                latencies.append(latency)
                # Print a progress dot for each successful ping
                # Note: The dots will appear after the full ping output is printed in this version.
        
        process.wait() # Wait for the ping process to finish

    except FileNotFoundError:
        print("\nError: 'ping' command not found. Is it installed and in your system's PATH?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    if not latencies:
        print("\n--- No successful pings were recorded. Cannot calculate statistics. ---", file=sys.stderr)
        sys.exit(1)

    # --- Statistical Analysis using NumPy ---
    # Convert our list of latencies to a NumPy array for efficient calculations.
    latencies_np = np.array(latencies)

    # Standard stats
    min_val = np.min(latencies_np)
    max_val = np.max(latencies_np)
    avg_val = np.mean(latencies_np)
    std_dev = np.std(latencies_np)

    # Percentiles
    p50 = np.percentile(latencies_np, 50)
    p90 = np.percentile(latencies_np, 90)
    p95 = np.percentile(latencies_np, 95)
    p99 = np.percentile(latencies_np, 99)

    # --- Print The Report ---
    print("\n\n--- Standard Ping Summary ---")
    print(f"round-trip min/avg/max/stddev = {min_val:.3f}/{avg_val:.3f}/{max_val:.3f}/{std_dev:.3f} ms")
    
    print("\n--- Enhanced Stability Analysis (Percentiles) ---")
    print(f"Median Latency (p50):      {p50:>8.3f} ms   (50% of pings were faster than this)")
    print(f"90th Percentile (p90):     {p90:>8.3f} ms   (90% of pings were faster than this)")
    print(f"95th Percentile (p95):     {p95:>8.3f} ms   (95% of pings were faster than this)")
    print(f"99th Percentile (p99):     {p99:>8.3f} ms   (Ignoring the worst 1% of pings)")

    print("\n--- Bell Curve Analysis (Sigma Perspective) ---")
    print(f"Based on Avg: {avg_val:.3f} ms and StdDev: {std_dev:.3f} ms")
    
    # Calculate actual percentage of data within the sigma ranges
    within_1_sigma = np.sum((latencies_np >= avg_val - std_dev) & (latencies_np <= avg_val + std_dev)) / len(latencies_np) * 100
    within_2_sigma = np.sum((latencies_np >= avg_val - 2*std_dev) & (latencies_np <= avg_val + 2*std_dev)) / len(latencies_np) * 100
    within_3_sigma = np.sum((latencies_np >= avg_val - 3*std_dev) & (latencies_np <= avg_val + 3*std_dev)) / len(latencies_np) * 100

    print(f"Range for 2-sigma (±2σ):   {max(0, avg_val - 2*std_dev):>6.2f} ms to {avg_val + 2*std_dev:6.2f} ms")
    print(f"  - In theory, this covers 95% of data. Your actual coverage: {within_2_sigma:.1f}%")

    print(f"Range for 3-sigma (±3σ):   {max(0, avg_val - 3*std_dev):>6.2f} ms to {avg_val + 3*std_dev:6.2f} ms")
    print(f"  - In theory, this covers 99.7% of data. Your actual coverage: {within_3_sigma:.1f}%")
    
    print("-------------------------------------------------")


if __name__ == "__main__":
    # This block runs when the script is executed directly.
    # It sets up command-line argument parsing.
    parser = argparse.ArgumentParser(
        description="A script to measure network stability by calculating latency percentiles.",
        formatter_class=argparse.RawTextHelpFormatter # For better help text formatting
    )
    parser.add_argument("target", help="The hostname or IP address to ping.")
    parser.add_argument("count", type=int, help="The number of times to ping.")
    
    args = parser.parse_args()

    if args.count < 10:
        print("Error: Ping count must be at least 10 for meaningful statistics.", file=sys.stderr)
        sys.exit(1)

    run_stability_test(args.target, args.count)
