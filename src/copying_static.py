import os, shutil


def copying(source_path: str, destination_path: str) -> bool:
    contents: list[str] = os.listdir(source_path)
    # print(f"contents: {contents}")
    for item in contents:
        source_item_path: str = os.path.join(source_path, item)
        # print(f"source item path: {source_item_path}")
        if os.path.isfile(source_item_path):  
            shutil.copy(source_item_path, destination_path)
        else:
            dest_item_path: str = os.path.join(destination_path, item)
            # print(f"destinatino item path: {dest_item_path}")
            os.mkdir(path=dest_item_path, mode=0o755)
            copying(source_item_path, dest_item_path)

    return True


def copy_from_static_to_public(source_path: str, destination_path: str) -> None:

    if os.path.exists(destination_path):
        if os.path.isfile(destination_path):
            raise Exception("The path contains file, not derictory")
        if os.listdir(destination_path):
            print("Deleting public directory")
            shutil.rmtree(destination_path)
            os.mkdir(path=destination_path, mode=0o755)
    else:
        os.mkdir(path=destination_path, mode=0o755)

    if os.path.exists(source_path):
        if os.path.isfile(source_path):
            raise Exception("The source path should contain directory, not a file")
        if not os.listdir(source_path):
            raise Exception("The source directory is empty")
        
        print("Copying started")
        if copying(source_path, destination_path):
            print("Copying finished")
        else:
            print("Something went wrong during copying process")

    else:
        raise Exception("The source directory of the provided path doesn't exits")



    
