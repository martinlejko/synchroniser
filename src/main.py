from argparser import ArgParser

def main():
    print("Hello, World!")
    args = ArgParser()
    print("Source Directory:", args.src_dir)
    print("Replica Directory:", args.replica_dir)
    print("Period:", args.period)
    print("Text File:", args.txt_file)

    

if __name__ == "__main__":
    main()