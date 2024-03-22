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
    cd synchroniser
    poetry install
    poetry shell
    ```
Now, everything should be set up and ready to use within the virtual environment created by Poetry.

## Usage
- After activating the Poetry shell, you can simply execute synchroniser to run the application, as it has been set up as the executable in the pyproject.toml configuration. There's no need to specify the full path; just type synchroniser and you're good to go
- For help and parameters, execute the following command:
    ```bash
    synchroniser -h
    ```

    This will display usage information:
    ```bash
    usage: synchroniser [-h] src_dir replica_dir period log_file
    ```

