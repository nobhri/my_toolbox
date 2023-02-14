import markdown
from bs4 import BeautifulSoup

with open("./sample.md", mode="r", encoding="utf-8") as f:
    markdown_text = f.read()
    html = markdown.markdown(
        markdown_text, extensions=["extra", "markdown_checklist.extension"]
    )
font_link = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@600&family=Literata:opsz@7..72&display=swap" rel="stylesheet">\n'''
style_file_link = '<link href="style.css" rel="stylesheet">\n'
html = font_link + style_file_link + html
soup = BeautifulSoup(html, 'html.parser') # initialize BeautifulSoup
html = soup.prettify()

with open("./sample.html", mode="w", encoding="utf-8") as f:
    f.write(html)
