import requests
from jinja2 import Template
import json


def load_jokes(number=10):
    payload = {'num': number}
    return requests.get('http://www.umori.li/api/random', params=payload).json()


def load_template(location="assets/template.html"):
    with open(location, 'r', encoding='utf-8') as f:
        html_template = f.read()
        return Template(html_template)


def write_html(jokes_json, html_template, name="index.html"):
    with open(name, 'w', encoding='utf-8-sig') as f:
        f.write(html_template.render(json_jokes=jokes_json,
                                     favicon='<link rel="shortcut icon" href="assets/img/favicon.ico">'))


def main():
    jokes = load_jokes()
    jokes_json = json.dumps(jokes, ensure_ascii=False, indent=2)
    html_template = load_template()

    write_html(jokes_json, html_template)

if __name__ == "__main__":
    main()

