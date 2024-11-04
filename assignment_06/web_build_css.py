# Importing OS and Regular Expression Modules
import os # The OS module gives the user functions allowing for us to interact with the operating system. -TF
import re # The RE module gives the user functions allowing for regular expression support. The functions in this module let you check if a particular string matches a given regular expression. - TF

# This entire coding assignment is to reduce redundancy and not repeat code over and over again. - TF
# Slugify function.
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html' (if statement) - TF
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html" # regular expression to format title - TF

# General Navigation Function.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    for title in titles: # for loop to iterate over each title - TF
        filename = slugify(title) # using a method (slugify) to create a filename - TF
        active_class = ' class="active"' if title == active_title else "" # if statement for active title - TF
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n' # f-string to format navigation link - TF
    return nav_links.strip()

# Create HTML function. This entire function creates the website - TF
def create_html_file(title, titles, output_dir="build_04"): # Edit this to rename the new builds. - TF
    """Generate and write HTML content based on the page title."""
    filename = slugify(title) # using slugify method to format filename - TF
    nav = generate_nav(titles, active_title=title) # using generate_nav method to create navigation - TF

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """ # f-string to format the HTML content - TF

    output_path = os.path.join(output_dir, filename) # Using os module to handle file path - TF
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists, and coding for a directory to be created (output_dir) - TF


    with open(output_path, 'w') as file: # with open() as file to manage file writing - TF
        file.write(html_content) # file.write to write HTML content to file - TF

    print(f"Created {filename} in the '{output_dir}' directory.") # f-string to print confirmation - TF


# Create CSS file function. This function makes the website look better by adding colors, font styles, etc. - TF
def create_css_file(output_dir="build"): # Editing this will change the name of the new build that used CSS. - TF
    """Generate and write the style.css file based on a dictionary of styles."""
    styles = {
        "font-family": "Calibri",             # font family
        "body-background": "#7BAFD4",     # Background color for .content
        "nav-background": "#13294B",          # Background color for nav
        "nav-a-color": "#4B9CD3",              # Text color for nav links
        "nav-a-active-color": "#ffffff"
    } # Dictionary containing CSS styles - TF

    css_content = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """ # f-string to format the CSS content - TF

    css_path = os.path.join(output_dir, "style.css") # Using os module to handle file path - TF
    with open(css_path, 'w') as file: # with open() as file to manage file writing - TF
        file.write(css_content) # file.write to write CSS content to file - TF

    print(f"Created style.css in the '{output_dir}' directory.") # f-string to print confirmation - TF

# Main function. 
def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
# I chose to base my titles on sports I like to do! - TF
    titles = ["Home", "Snowboarding", "Rock Climbing", "Surfing"] # Editing this changes the titles of the categories on the website. - TF

    # Create HTML files for each title
    for title in titles: # for loop to create HTML files for each title - TF
        create_html_file(title, titles) # Using create_html_file method to generate HTML for each title - TF

    # Create the style.css file
        create_css_file() # You have to line this up with the code above or else it will not work also calling the create_css_file method to generate CSS. - TF
    # uncomment the create_css_file() function if you add the function.

if __name__ == "__main__":
    main() # calling main function - TF
