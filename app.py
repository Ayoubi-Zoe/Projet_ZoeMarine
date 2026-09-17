from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Projet Zoé & Marine"),

    dcc.Location(id="url"),

    html.Nav([
        dcc.Link("Page Zoé", href="/zoe"),
        html.Span(" | "),
        dcc.Link("Page Marine", href="/marine")
    ]),

    html.Hr(),

    html.Div(id="contenu-page")
])


@app.callback(
    Output("contenu-page", "children"),
    Input("url", "pathname")
)
def afficher_page(pathname):
    if pathname == "/marine":
        return html.Div([
            html.H2("Page de Marine"),
            html.P("Marine ajoutera son contenu ici.")
        ])

    return html.Div([
        html.H2("Page de Zoé"),
        html.P("Contenu de la page de Zoé.")
    ])


if __name__ == "__main__":
    app.run(debug=True)