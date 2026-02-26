# Speed Runner Optimizer

## GitHub Repository

https://github.com/Manojkumarjujjavarapu/T5W2/tree/main/PY2_SPEED_RUNNER_OPTIMIZER

## Overview

This project processes a large number of CSV files from a folder and compares execution time between baseline (single process) and optimized (multiprocessing) execution. The goal is to demonstrate performance improvement using parallel processing.

## How to Run — Baseline Mode

python3 main.py --mode baseline --input bulk_data --output output

## How to Run — Optimized Mode

python3 main.py --mode optimized --input bulk_data --output output

## Output Generated

output/performance_results.json

## Why Multiprocessing

Multiprocessing was chosen because the file processing involves CPU-bound operations. Multiprocessing enables true parallel execution across multiple CPU cores by bypassing Python’s Global Interpreter Lock (GIL), resulting in faster performance compared to sequential processing.
