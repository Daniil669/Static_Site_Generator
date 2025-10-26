import os
from copying_static import copy_from_static_to_public
from page_generator import generate_page

template_path: str = "./template.html"
dir_path_public: str = "./public"
dir_path_content: str = "./content"
dir_path_static: str = "./static"


def main() -> None:
    try:

        copy_from_static_to_public(dir_path_static, dir_path_public)
        generate_page(dir_path_content, template_path, dir_path_public)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()