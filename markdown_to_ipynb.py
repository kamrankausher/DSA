import os
import sys
import json
import glob

def parse_markdown_to_notebook(md_content):
    """
    Parses markdown content and converts it into Jupyter Notebook JSON format.
    Python code blocks (```python) are converted into executable code cells.
    All other content (text, tables, diagrams, headers) becomes markdown cells.
    """
    cells = []
    lines = md_content.splitlines()
    
    current_cell_type = "markdown"
    current_source = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect start of a Python code block
        if line.strip().startswith("```python"):
            # Save the preceding markdown cell if it has content
            if current_source:
                # Trim leading/trailing empty lines for cleanliness
                while current_source and current_source[0].strip() == "":
                    current_source.pop(0)
                while current_source and current_source[-1].strip() == "":
                    current_source.pop()
                    
                if current_source:
                    formatted_source = [l + "\n" for l in current_source[:-1]] + [current_source[-1]] if len(current_source) > 1 else current_source
                    cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": formatted_source
                    })
            
            # Switch to code cell mode
            current_cell_type = "code"
            current_source = []
            i += 1
            continue
            
        # Detect end of a code block
        elif line.strip().startswith("```") and current_cell_type == "code":
            # Save the code cell
            if current_source:
                while current_source and current_source[0].strip() == "":
                    current_source.pop(0)
                while current_source and current_source[-1].strip() == "":
                    current_source.pop()
                    
                if current_source:
                    formatted_source = [l + "\n" for l in current_source[:-1]] + [current_source[-1]] if len(current_source) > 1 else current_source
                    cells.append({
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": formatted_source
                    })
            
            # Switch back to markdown mode
            current_cell_type = "markdown"
            current_source = []
            i += 1
            continue
            
        current_source.append(line)
        i += 1
        
    # Save any remaining content in the last cell
    if current_source:
        while current_source and current_source[0].strip() == "":
            current_source.pop(0)
        while current_source and current_source[-1].strip() == "":
            current_source.pop()
            
        if current_source:
            formatted_source = [l + "\n" for l in current_source[:-1]] + [current_source[-1]] if len(current_source) > 1 else current_source
            cell = {
                "cell_type": current_cell_type,
                "metadata": {},
                "source": formatted_source
            }
            if current_cell_type == "code":
                cell["execution_count"] = None
                cell["outputs"] = []
            cells.append(cell)
            
    # Assemble the final Jupyter Notebook JSON structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    return notebook

def convert_file(md_path):
    """Converts a single markdown file to an ipynb notebook."""
    if not os.path.exists(md_path):
        print(f"Error: File '{md_path}' does not exist.")
        return False
        
    print(f"Converting '{md_path}'...")
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    notebook_json = parse_markdown_to_notebook(md_content)
    
    ipynb_path = md_path.rsplit('.', 1)[0] + '.ipynb'
    with open(ipynb_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_json, f, indent=1, ensure_ascii=False)
        
    print(f"Success! Saved notebook to '{ipynb_path}'\n")
    return True

def convert_all():
    """Converts all markdown files in the current directory (excluding README and generator prompts)."""
    md_files = glob.glob("*.md")
    converted_count = 0
    
    for file in md_files:
        # Ignore readme, prompts, and documentation files
        name_lower = file.lower()
        if "readme" in name_lower or "prompt" in name_lower or "guide" in name_lower:
            continue
            
        if convert_file(file):
            converted_count += 1
            
    if converted_count == 0:
        print("No markdown files found to convert. Add some *.md files (e.g., '01_complexity_analysis.md') and run again!")
    else:
        print(f"Completed! Converted {converted_count} markdown files to Jupyter Notebooks.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # User specified a specific file to convert
        convert_file(sys.argv[1])
    else:
        # Auto-convert all valid md files in the current folder
        convert_all()
