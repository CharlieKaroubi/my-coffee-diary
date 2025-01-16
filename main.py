from website import create_app

app = create_app()

@app.template_filter('name')
def name(s):
    parts = s.split('#')
    return parts[0]

@app.template_filter('url')
def url(s):
    parts = s.split('#')
    return parts[1]

@app.template_filter('rating')
def rating(s):
    parts = s.split('#')
    return parts[2]

# Only if we run main file run server
if __name__ == '__main__':
    app.run(debug=True)
