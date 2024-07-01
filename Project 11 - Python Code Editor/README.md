# Python Code Editor & Executor

This is a web-based Python code editor built using PyWebIO. The editor allows users to write and execute Python code in a web interface. It also offers customization options for themes and fonts to enhance the coding experience.

## Features

-   **Code Execution**: Write and execute Python code directly in the browser.
-   **Customization**: Choose from a variety of themes and font families.
-   **Error Handling**: Displays standard output and error messages.
-   **History Management**: Retains the history of executed code snippets.
-   **Clear Output**: Option to clear the output area.

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**

    
    `git clone https://github.com/JawadSher/Python-Projects-Beginner-to-Advance/tree/main/Project%2011%20-%20Python%20Code%20Editor` 
    
2.  **Navigate to the project directory:**
    
    
    `cd your-repo-name` 
    
3.  **Install the required packages:**
    
    
    `pip install pywebio` 
    
4.  **Start the server:**
    
    
    `python main.py` 
    
5.  Open your browser and navigate to `http://localhost:8080` to access the editor.
    

## Usage

1.  **Customization:**
    
    -   Select your preferred theme from the dropdown menu.
    -   Choose a font family.
    -   Specify the font size (default is 18px).
2.  **Code Editor:**
    
    -   Write your Python code in the provided text area.
    -   Click the "Run" button to execute the code.
3.  **Output:**
    
    -   View the standard output and error messages in the output section.
    -   Use the "Clear" button to clear the output area.

## Code Explanation

### Imports and Dependencies

python

Copy code

```
from pywebio.input import textarea, select, input, NUMBER
from pywebio.output import put_html, put_text, use_scope, put_error, put_code, put_button, clear
from pywebio import start_server
import io
import sys
``` 

These are the necessary imports from the PyWebIO library and the standard `io` and `sys` modules for input/output redirection. The `pywebio.input` and `pywebio.output` modules are used for creating the user interface elements and displaying output respectively. The `start_server` function is used to run the web server.

### Function: `execute_code`


```
def execute_code(code):
    o_stdout = sys.stdout
    o_stderr = sys.stderr
  
    redirected_stdout = sys.stdout = io.StringIO()
    redirected_stderr = sys.stderr = io.StringIO()

    try:
        exec_global = {}
        exec(code, exec_global)
        return redirected_stdout.getvalue(), redirected_stderr.getvalue()
    except Exception as e:
        return "", f"Error Executing Code: {e}"
    finally:
        sys.stdout = o_stdout
        sys.stderr = o_stderr
   ``` 

This function captures the standard output and error messages when executing Python code. It works as follows:

1.  **Redirect stdout and stderr**: `sys.stdout` and `sys.stderr` are redirected to `io.StringIO()` objects to capture the output and error messages.
2.  **Execute Code**: The `exec` function executes the provided Python code within an isolated dictionary `exec_global` to avoid polluting the global namespace.
3.  **Return Output and Errors**: Captured output and error messages are returned as strings.
4.  **Restore stdout and stderr**: Finally, `sys.stdout` and `sys.stderr` are restored to their original values to avoid affecting other parts of the program.

### Function: `customization`



```
def customization():
    theme_options = [
        "default dark+",
        "default light+",
        "quiet light",
        "solarized dark",
        "solarized light",
        "monokai",
        "dark (Visual Studio)",
        "light (Visual Studio)",
        "dark+ (Contrast)",
        "kimbie dark",
        "darcula",
    ]
  
    font_options = [
        "Ubuntu Mono",
        "Fira Code",
        "monospace",
        "Consolas",
        "Roboto Mono",
        "Inconsolata",
        "Source Code Pro",
        "Courier New",
        "Hack",
        "Cascadia Code"
    ]

    theme = select("Select Theme", options=theme_options)
    font = select("Select Font Family", options=font_options)
    font_num = input('Select Font Size', type=NUMBER, placeholder='Default 18px')

    return theme, font, font_num
   ``` 

This function provides customization options for selecting a theme, font family, and font size:

1.  **Theme Options**: A list of available themes is provided in `theme_options`.
2.  **Font Options**: A list of available font families is provided in `font_options`.
3.  **User Input**: The `select` function is used to create dropdown menus for theme and font family selection, and the `input` function is used for font size input.
4.  **Return Values**: The selected theme, font family, and font size are returned.

### Function: `main`


```
def main():
    put_html("""
        <style>
            .app-title {
                font-size: 36px; 
                font-weight: bold;
                color: #247ba0; 
                text-align: center; 
                margin-bottom: 20px; 
            }
        </style>
        <h1 class="app-title">Python Code Editor</h1>
    """)

    theme_name, font_family, font_size = customization()

    put_html(f"""
        <style>
            .CodeMirror {{
                font-size: {font_size}px !important;
                font-family: '{font_family}', monospace;
                line-height: 1.5;
                background-color: var(--vscode-{theme_name.replace(' ', '').lower()}-background);
                color: var(--vscode-{theme_name.replace(' ', '').lower()}-foreground);
            }}
        </style>
    """)

    c_history = {}

    while True:
        code = textarea('Enter Python code', code={
            'rows': 20,
            'required': True,
            'mode': 'python',
            'theme': f'{theme_name}',
            'placeholder': 'Type your Python code here'
        })
    
        if code.strip():
            if code not in c_history:
                c_history[code] = (None, None)
                stdout, stderr = execute_code(code)
                c_history[code] = (stdout, stderr)
            else:
                stdout, stderr = c_history[code]
            
            with use_scope('output', clear=True):
                put_html("<b>Source Code:</b>")
                put_code(code, language='python')
                if stdout:
                    put_html("<b>Standard Output:</b>")
                    put_text(stdout)
                if stderr:
                    put_html("<b>Standard Error:</b>")
                    put_error(stderr)
                
                if stdout or stderr:
                    put_button('Clear', onclick=lambda: clear(scope='output'))
        else:
            put_html("<b>Error:</b> Please enter some Python code.")
   ``` 

This is the main function that runs the PyWebIO application. It sets up the HTML and CSS for the interface, collects customization options, and processes the user's Python code:

1.  **Title Styling**: The `put_html` function is used to style the title of the application.
2.  **Customization**: The `customization` function is called to get the user's theme, font family, and font size preferences.
3.  **Apply Customization**: The selected theme, font family, and font size are applied to the code editor using inline CSS.
4.  **Code Execution Loop**: A loop is used to continuously accept and execute code from the user.
    -   **Textarea**: The `textarea` function creates an input area for the user to write Python code.
    -   **Code History**: A dictionary `c_history` is used to store the history of executed code snippets and their outputs.
    -   **Execute Code**: The `execute_code` function is called to run the user's code and capture the output and errors.
    -   **Display Output**: The output and error messages are displayed using the `put_html`, `put_text`, `put_error`, and `put_code` functions.
    -   **Clear Output**: A "Clear" button is provided to clear the output area.
