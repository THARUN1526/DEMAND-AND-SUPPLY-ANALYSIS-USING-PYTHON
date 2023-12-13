#let’s analyze the relationship between the number of drivers active per hour and the number of riders active per hour


demand = data["Riders Active Per Hour"]
supply = data["Drivers Active Per Hour"]

figure = px.scatter(data, x = "Drivers Active Per Hour",
                    y = "Riders Active Per Hour", trendline="ols", 
                    title="Demand and Supply Analysis")
figure.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)",
)
figure.show()