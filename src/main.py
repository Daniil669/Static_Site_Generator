import sys
from copying_static import copy_from_static_to_public
from page_generator import generate_pages_recursive

template_path: str = "./template.html"
dir_path_public: str = "./docs"
dir_path_content: str = "./content"
dir_path_static: str = "./static"


def main() -> None:
    try:
        basepath = "/"
        if len(sys.argv) > 1:
            basepath = sys.argv[1]
        
        copy_from_static_to_public(dir_path_static, dir_path_public)

        print("Generating content...")
        generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()