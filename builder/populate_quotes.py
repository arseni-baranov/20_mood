import requests
from jinja2 import Template
import json


def load_jokes(number=10):
    payload = {'num': number}
    return requests.get('http://www.umori.li/api/random', params=payload).json()


def load_template(location="builder/template.html"):
    with open(location, 'r', encoding='utf-8') as f:
        html_template = f.read()
        return Template(html_template)


def write_jokes(js_template, jokes_json, name="static/js/main.js"):
    with open(name, 'w', encoding='utf-8-sig') as f:
        f.write(js_template.render(jokes_json=jokes_json))


def write_html(html_template, name="build/index.html"):
    with open(name, 'w', encoding='utf-8-sig') as f:
        f.write(html_template.render(favicon='<link rel="shortcut icon" href="../static/img/favicon.ico">'))


def main():
    jokes = load_jokes()
    jokes_json = json.dumps(jokes, ensure_ascii=False, indent=2)
    html_template = load_template()
    js_template = load_template("builder/jokes_template.js")

    write_jokes(js_template, jokes_json)
    write_html(html_template)

if __name__ == "__main__":
    main()

