#Call food data from second source
food_grid =("Food-Grid view.csv")
food_grid_df = pd.read_csv(food_grid)
#clear unecessary columns
Food_Grid_df=food_grid_df.drop(columns=["image", "class", "subclass", "description", "ingredients", "effect"]).dropna()
Food_Grid_df
​
​
#Manipulate Data to suit our needs 
FoodGrid_df = Food_Grid_df[["hp", "name"]]
Food_Grid_df.reset_index(drop=True, inplace=True)
FoodGrid_df=FoodGrid_df.sort_values(by="hp", ascending=False)
FoodGrid_df=FoodGrid_df.set_index("name")
FoodGrid_df
​
​
#Show info in graph form
fig, ax = plt.subplots()
FoodGrid_df.plot(kind="bar", figsize=(10,6), ax=ax, color='green',
                  title="Which recipe gives the most Hearts",
                  xlabel="Recipe",
                  ylabel="Hearts Gained");
fig.tight_layout();
plt.savefig("../BotW/images/Recipe_bar.png")