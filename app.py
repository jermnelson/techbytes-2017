from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
pages = FlatPages(app)
presentation = sorted(pages, key=lambda p: p.meta['order'])

@app.route("/")
def index():
    return render_template("techbytes-2017/index.html",
        active='home',
        presentation=presentation)

@app.route("/<path:path>/")
def page(path):
    prev_page, next_page = None, None
    page = pages.get_or_404(path)
    if page.meta.get('order')-1 > -1:
        prev_page = presentation[page.meta.get('order')-1]
    if page.meta.get('order') + 1 < len(presentation):
        next_page = presentation[page.meta.get('order')+1]
    return render_template("techbytes-2017/page.html",
        page=page,
        active='pages',
        presentation=presentation,
        previous_page=prev_page,
        next_page=next_page)

@app.route("/about")
def about():
    return render_template("techbytes-2017/about.html",
        active="about",
        presentation=presentation)

@app.route("/contact")
def contact():
    return render_template("techbytes-2017/contact.html",
        active="contact",
        presentation=presentation)
