import datetime
import io
import json
import os

from feedgen.feed import FeedGenerator
from flask import Flask, render_template, request, redirect, Response, send_file, abort, send_from_directory

app = Flask(__name__)

try:
    app.config['GA_TRACKING_ID'] = os.environ['GA_TRACKING_ID'] 
except:
    print('Tracking ID not set')


@app.route('/')
def index():
    age = int((datetime.date.today() - datetime.date(1995, 4, 22)).days / 365)
    return render_template('home.html', age=age)


@app.route('/tech')
def tech():
    return render_template('tech.html')


@app.route('/resume')
def resume():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/'
    return send_from_directory(filepath, 'Resume.pdf')


@app.route('/books')
def books():
    data = get_static_json("static/books/books.json")['books']
    data.sort(key=order_books_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [book for book in data if tag.lower() in [book_tag.lower()
                                                         for book_tag in book['tags']]]

    return render_template('books.html', books=data, tag=tag)


@app.route('/projects')
def projects():
    data = get_static_json("static/projects/projects.json")['projects']
    data.sort(key=order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower()
                                                               for project_tag in project['tags']]]

    return render_template('projects.html', projects=data, tag=tag)


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


def order_books_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


@app.route('/books/<title>')
def book(title):
    books = get_static_json("static/books/books.json")['books']

    in_book = next((p for p in books if p['link'] == title), None)

    if in_book is None:
        return render_template('404.html'), 404
    else:
        selected = in_book

    # load html if the json file doesn't contain a description
    if 'description' not in selected:
        path = "books"
        selected['description'] = io.open(get_static_file(
            'static/%s/%s/%s.html' % (path, selected['link'], selected['link'])), "r", encoding="utf-8").read()
    return render_template('book.html', book=selected)


@app.route('/projects/<title>')
def project(title):
    projects = get_static_json("static/projects/projects.json")['projects']

    in_project = next((p for p in projects if p['link'] == title), None)

    if in_project is None:
        return render_template('404.html'), 404
    else:
        selected = in_project

    # load html if the json file doesn't contain a description
    if 'description' not in selected:
        path = "projects"
        selected['description'] = io.open(get_static_file(
            'static/%s/%s/%s.html' % (path, selected['link'], selected['link'])), "r", encoding="utf-8").read()
    return render_template('project.html', project=selected)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))


if __name__ == "__main__":
    print("running py app")
    app.run(host="0.0.0.0", port=8080)
