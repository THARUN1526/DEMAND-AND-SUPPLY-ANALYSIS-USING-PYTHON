#Now let’s visualize the supply ratio

fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], 
                         y=data['Supply Ratio'], mode='markers'))
fig.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active Per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
)
fig.show()