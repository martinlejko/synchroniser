# Synchroniser

## Description
The program synchronizes two folders, ensuring that the replica folder maintains an identical copy of the source folder. Synchronization occurs periodically and logs file operations to both a file and the console. Users can specify folder paths, synchronization intervals, and log file paths via command-line arguments. 

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:martinlejko/synchroniser.git
   ```

2. Install Poetry (if not already installed):
    ```bash
    pip install poetry
    ```
4. Navigate to the project directory and install dependencies using Poetry
and  enter the virtual environment created by Poetry: 
    ```bash
    cd syncer
    poetry install
    poetry shell
    ```
Now, everything should be set up and ready to use within the virtual environment created by Poetry.

## Usage

- The `main.py` script in `synchroniser/src/` directory is marked as executable, allowing you to run it directly from the command line.
- For help and parameters, execute the following command:
    ```bash
    ./synchroniser/src/main.py -h
    ```

    This will display usage information:
    ```bash
    usage: main.py [-h] src_dir replica_dir period log_file
    ```

