from flask import request, Flask, Response, render_template, jsonify, abort,\
    redirect, url_for, send_file, session, g
from db import create_table_if_not_exists, get_all_palestinian_articles, SCHEMA

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route('/')
def home_page():
    create_table_if_not_exists()
    articles = get_all_palestinian_articles()
    # convert list of tuples into list of dictionary
    articles_info = []
    for a in articles:
        info = {field: a[i] for i, field in enumerate(SCHEMA)}
        if int(info["bias"]) < 1:
            info["color"] = "success"
        elif int(info["bias"]) < 10:
            info["color"] = "warning"
        else:
            info["color"] = "danger"   
        if info["topic"] == "Palestine":      
            articles_info.append(info)
    return render_template("index.html", articles_info=articles_info)

if __name__ == "__main__":
    app.run(debug=True)
