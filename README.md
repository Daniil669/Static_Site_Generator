# Static Site Generator

A simple **Static Site Generator (SSG)** built in **Python**, designed to convert Markdown (`.md`) files into fully rendered HTML pages using custom templates and assets.  
All scripts are tested with the **unittest** module for reliability and maintainability.

🔗 **Live Demo:** [Static Site Generator on GitHub Pages](https://daniil669.github.io/Static_Site_Generator/)

---

## Features

- Converts `.md` files from the `content/` folder into `.html`
- Injects generated HTML into templates located in the project root
- Copies styles and images from the `static/` folder into the `docs/` directory
- Generates production-ready HTML files inside `docs/`
- Includes unit tests for all Python logic
- Uses shell scripts to manage development, testing, and deployment

---

## How It Works

1. Place your Markdown (`.md`) files in the `content/` folder.  
2. Run one of the shell scripts depending on your goal:

| Script | Purpose |
|--------|----------|
| `main.sh` | Run generator + start local HTTP server for development |
| `build.sh` | Generate and prepare final HTML files for deployment |
| `test.sh` | Execute unit tests for Python scripts |

3. The generator parses Markdown, converts it to HTML, and injects it into the HTML template.  
4. Static assets from the `static/` folder are copied to the `docs/` directory.

---

## Testing

All modules are covered with **unit tests** written using Python’s built-in `unittest` framework.

Run tests manually:
```bash
./test.sh
```

---

## Deployment

After running `build.sh`, push your changes to GitHub. 
To deploy your site, go to setting inside your repo, nevigate to pages, choose main branch and directory /docs and save.

Example:
```bash
./build.sh
git add .
git commit -m "Build site"
git push origin main
```

---

## Live Example

👉 [Visit the Live Demo](https://daniil669.github.io/Static_Site_Generator/)

---
