import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.

Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!

Markdown includes syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
'''


app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label':'New York City', 'value':'NYC'},
            {'label':'San Francisco', 'value':'SF'}
        ],
        value='SF'
    ),
    html.P(html.Label('Slider')),
    dcc.Slider(min=-10, max=10, step=0.5, value=0, marks={i:i for i in range(-10, 10)}),
    html.P(html.Label('Some radio items')),
    dcc.RadioItems(
        options=[
            {'label':'New York City', 'value':'NYC'},
            {'label':'San Francisco', 'value':'SF'}
        ],
        value='SF'
    ),
    dcc.Markdown(markdown_text)
])


if __name__ == '__main__':
    app.run_server()