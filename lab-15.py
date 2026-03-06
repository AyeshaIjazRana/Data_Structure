# Exception handling (most important for a good programmer) (it means "Try this code, but if something goes wrong, don't crash—do this instead.)

# Task 1: The Coffee Shop Menu (Dictionary)
# You are writing the software for a local cafe&#39;s cash register. You need a way to look up the price of a
# drink instantly. Dictionaries are perfect for this because every drink name (Key) maps to a specific
# price (Value).
# 1.A customer orders a &quot;Latte&quot;. Look up the price using the key &quot;Latte&quot; and print it out.
# 2.The cafe is introducing a new drink! Add a &quot;Mocha&quot; to the dictionary with a price of 4.25.
# 3.Due to inflation, the price of &quot;Black Coffee&quot; just went up. Update its price to 2.75.
# 4.Print the entire cafe_menu to make sure your updates worked.

cafe_menu={
    "Black Coffee": 2.50,
    "Latte":3.75,
    "Tea":2.00
}
print("Price of Latte:",cafe_menu["Latte"])
cafe_menu["Mocha"]=4.25
cafe_menu["Black Coffee"]=2.75
print(cafe_menu)

# Task 2: The Video Game High Score (Tuple)
# You are building a retro arcade game. When a player sets a high score, that record should be
# permanent—no other code (or cheater!) should be able to accidentally change it. Tuples are the
# perfect choice because they are locked and unchangeable.
# 1.Unpack the high_score_record into three separate variables named player, score, and level.
# 2.Print a congratulatory message using those new variables (e.g., &quot;Player ABC reached level 12
# with 99500 points!&quot;).
# 3.Just to prove our data is safe from hackers, write a comment (#) explaining what would
# happen if you tried to run high_score_record[1] = 999999

high_score_record=("ABC",99500,12)
player,score,level=high_score_record
print("Player",player,"reached level",level,"with",score,"points.")

# Task: The Movie Watchlist (Set)
# You are making an app that lets users track movies they want to watch. Users often accidentally
# click the &quot;Add to Watchlist&quot; button multiple times. Sets are the perfect tool here because they
# automatically ignore duplicates!
# 1.Convert the messy movie_clicks list into a set called watchlist to automatically delete the duplicate. Print the set.
# 2.The user just clicked to add &quot;Toy Story&quot;. Add it to your watchlist set.
# 3.The user finally watched &quot;The Matrix&quot;. Remove it from the set.
# 4.Print the final watchlist to see the updated movies.

movie_clicks=["The Matrix","Inception","Dune","Inception","Avatar"]
watchlist=set(movie_clicks)
print("Watchlist:",watchlist)
watchlist.add("Toy Story")
watchlist.remove("The Matrix")
print("Updated Watchlist:",watchlist)