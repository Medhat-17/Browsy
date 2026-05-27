from renderer.html.parser import parse_html

def render(html):
    dom = parse_html(html)

    print("\n" + "="*60)
    print(dom)
    print("="*60)