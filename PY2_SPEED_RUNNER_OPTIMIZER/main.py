import argparse
import json
import os

from src.processor import baseline_process, multiprocessing_process
from src.decorators import time_it


@time_it
def run_baseline(folder):
    return baseline_process(folder)


@time_it
def run_optimized(folder):
    return multiprocessing_process(folder)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="bulk_data")
    parser.add_argument("--output", default="output")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    # Run both modes
    files_count, baseline_time = run_baseline(args.input)
    _, optimized_time = run_optimized(args.input)

    speedup = baseline_time / optimized_time if optimized_time else None

    results = {
        "filesProcessed": files_count,
        "baselineSeconds": baseline_time,
        "optimizedSeconds": optimized_time,
        "speedupX": speedup,
        "methodUsed": "multiprocessing"
    }

    with open(os.path.join(args.output, "performance_results.json"), "w") as f:
        json.dump(results, f, indent=4)

    print("✅ Performance results saved!")


if __name__ == "__main__":
    main()