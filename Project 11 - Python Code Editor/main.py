from pywebio.input import textarea, select, input, NUMBER
from pywebio.output import put_html, put_table, put_text, use_scope, put_error, put_code, put_button, clear
from pywebio import start_server
import io
import sys
from pywebio import session

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

def customization():
  # Real-world VS Code themes
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
  
    # Font families
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

    

def main():
    put_html("""
        <style>
            .app-title {
                font-size: 36px; /* Adjust font size as desired */
                font-weight: bold;
                color: #247ba0; /* Set your preferred color */
                text-align: center; /* Center alignment */
                margin-bottom: 20px; /* Add some margin below */
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

# Start the server
start_server(main, port=8080)