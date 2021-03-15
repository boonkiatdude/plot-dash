import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_auth


USERNAME_PASSWORD_PAIRS = [
    ['username', 'password'],
    ['Jamesbond', '007']
]


app = dash.Dash()
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)


app.layout = html.Div(
    [
        dcc.RangeSlider(
            id='my-slider',
            min=-5, max=6,
            step=1, value=[-2, 1],
            marks={i:str(i) for i in range(-5, 7)}
        ),
        html.H1(id='product')
    ]
)

@app.callback(
    Output('product', 'children'),
    [Input('my-slider', 'value')]
)
def update_number(number):
    return number[0] * number[1]

    
if __name__ == '__main__':
    app.run_server()