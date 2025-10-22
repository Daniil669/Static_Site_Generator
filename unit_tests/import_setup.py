import sys, dotenv, os

def add_src_to_path():
    dotenv.load_dotenv()

    sys.path.append(os.getenv("MODULES_PATH"))