import os
import webbrowser

class NoLinkReference(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"NoLinkReference: {self.message}"

def has_ext(fname):
    root, ext = os.path.splitext(fname)
    return ext != ''  # True if extension, else False

base_urls = {
    "CF": "https://codeforces.com/",
    "CSES": "https://cses.fi/problemset/task/",
    "USACO": "https://usaco.org/index.php?page=viewproblem2&"
}

for i in range(3):
    fn = input("\nFilename (FOLDER/problem_name): ")
    if not has_ext(fn):
        fn+=".py"
    fn = fn.replace(" ", "_")
    try:
        with open(fn, "r") as f:
            contents = f.readline().strip()  # Stripping extra spaces/newlines
            if not contents.startswith("#"):
                raise NoLinkReference(f"First line of file isn't a comment: \"{contents}\"")
            contents = contents[1:]
            problem_name = os.path.splitext(os.path.basename(fn))[0]
            category = os.path.basename(os.path.dirname(f.name))
        # Construct the URL
        category = category.upper()
        if category in base_urls:
            url = base_urls[category] + contents
            print(f"\nOpening \"{problem_name}\": {url}\n")
            webbrowser.open(url)  # Opens the URL in the default web browser
            quit()
        else:
            raise ValueError(f"Unknown category: {category}")
    except Exception as e:
        print(f"\nAn error occured: {e}")