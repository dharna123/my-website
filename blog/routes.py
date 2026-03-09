from . import blog

@blog.route("/")
def home():
    return "My Blog"