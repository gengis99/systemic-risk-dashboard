import dash
from dash import dcc, html
import plotly.graph_objects as go
import networkx as nx
import pandas as pd
import plotly.io as pio
from dash import callback_context

# Dati di esempio SRISK (sostituire con i tuoi dati reali)
df_srisk = pd.DataFrame({
    'Banca': ['Intesa Sanpaolo', 'Unicredit', 'Banco BPM', 'BPER Banca', 'Mediobanca', 'FinecoBank'],
    'SRISK': [85926, 68178, 14698, 11429, 3804, 561]
})

# Creazione matrice di correlazione tra banche (per esempio)
banks = df_srisk['Banca'].tolist()
corr_matrix = pd.DataFrame([
    [1, 0.85, 0.75, 0.7, 0.6, 0.55],
    [0.85, 1, 0.72, 0.68, 0.65, 0.53],
    [0.75, 0.72, 1, 0.76, 0.7, 0.5],
    [0.7, 0.68, 0.76, 1, 0.74, 0.51],
    [0.6, 0.65, 0.7, 0.74, 1, 0.48],
    [0.55, 0.53, 0.5, 0.51, 0.48, 1]
], columns=banks, index=banks)

# === Creazione dell'app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sistema Bancario Italiano - Dashboard di Rischio Sistemico", style={'textAlign': 'center'}),

    dcc.Tabs([
        dcc.Tab(label='SRISK', children=[
            html.H2("Rischio Sistemico per Banca (SRISK)"),
            # Dropdown per selezionare la banca
            dcc.Dropdown(
                id='banca-dropdown',
                options=[
                    {'label': banca, 'value': banca} for banca in df_srisk['Banca']
                ],
                value='Intesa Sanpaolo',  # Valore di default
                style={'width': '50%'}
            ),
            dcc.Graph(id='srisk-graph'),
            # Bottone per esportare in CSV
            html.Button("Esporta SRISK in CSV", id="export-csv-button"),
            dcc.Download(id="download-srisk-csv")
        ]),

        dcc.Tab(label='Network Interbancario', children=[
            html.H2("Network Interbancario"),
            # Slider per la selezione della soglia di correlazione
            dcc.Slider(
                id='threshold-slider',
                min=0,
                max=1,
                step=0.05,
                value=0.7,
                marks={i/10: str(i/10) for i in range(0, 11)},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            dcc.Graph(id='network-graph'),
            # Bottone per esportare la rete come PNG
            html.Button("Esporta Network come PNG", id="export-png-button"),
            dcc.Download(id="download-network-png")
        ]),
    ])
])

# Funzione per aggiornare il grafico SRISK in base alla banca selezionata
@app.callback(
    dash.dependencies.Output('srisk-graph', 'figure'),
    [dash.dependencies.Input('banca-dropdown', 'value')]
)
def update_srisk(banca_selezionata):
    df_banca = df_srisk[df_srisk['Banca'] == banca_selezionata]
    fig = go.Figure(
        data=[go.Bar(
            x=df_banca['Banca'],
            y=df_banca['SRISK'],
            marker=dict(color='red')
        )],
        layout=go.Layout(
            title=f"SRISK di {banca_selezionata} (€ milioni)",
            xaxis=dict(title='Banca'),
            yaxis=dict(title='SRISK (€ milioni)')
        )
    )
    return fig

# Funzione per aggiornare la rete interbancaria dinamica in base alla soglia del slider
@app.callback(
    dash.dependencies.Output('network-graph', 'figure'),
    [dash.dependencies.Input('threshold-slider', 'value')]
)
def update_network(threshold):
    # Ricrea il grafo con la nuova soglia di correlazione
    G = nx.Graph()
    G.add_nodes_from(banks)
    for i in banks:
        for j in banks:
            if i != j and corr_matrix.loc[i, j] >= threshold:
                G.add_edge(i, j, weight=corr_matrix.loc[i, j])

    # Genera il layout della rete
    pos = nx.spring_layout(G, seed=42)  # layout statico
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_y.append(y0)
        edge_y.append(y1)

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    # Crea il grafico della rete
    fig = go.Figure()

    # Aggiungi gli archi (edges)
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='gray'),
        hoverinfo='none',
        mode='lines'
    ))

    # Aggiungi i nodi (nodes)
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(size=20, color='blue'),
        text=[node for node in G.nodes()]
    ))

    fig.update_layout(title='Network Interbancario', showlegend=False, hovermode='closest')

    return fig

# Funzione per esportare i dati SRISK in CSV
@app.callback(
    dash.dependencies.Output('download-srisk-csv', 'data'),
    [dash.dependencies.Input('export-csv-button', 'n_clicks')],
    prevent_initial_call=True
)
def export_srisk(n_clicks):
    if n_clicks is None:
        return None
    return dcc.send_data_frame(df_srisk.to_csv, "srisk_data.csv")

# Funzione per esportare la rete come immagine PNG
@app.callback(
    dash.dependencies.Output('download-network-png', 'data'),
    [dash.dependencies.Input('export-png-button', 'n_clicks')],
    prevent_initial_call=True
)
def export_network(n_clicks):
    if n_clicks is None:
        return None
    fig = go.Figure()  # Usa lo stesso codice che già hai per creare il grafico della rete
    # Aggiungi la logica per generare il grafico della rete
    return dcc.send_file(pio.write_image(fig, 'network_graph.png'))


if __name__ == '__main__':
    app.run(debug=True, port=8051)
