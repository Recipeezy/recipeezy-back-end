# Endpoints

## Heroku Endpoints

Get Requests that are currently available

https://recipeezy-app.herokuapp.com/users/

https://recipeezy-app.herokuapp.com/ingredients/

https://recipeezy-app.herokuapp.com/ingredients/1/  <-- the '1' designates which ingredient

https://recipeezy-app.herokuapp.com/pantry/ <-- will grab the pantry for who you are logged in as

https://recipeezy-app.herokuapp.com/recipes/ <-- this will show all recipes and their associated details

https://recipeezy-app.herokuapp.com/recipes/1/ <-- the '1' designates which recipe you want in specific. Shows all it's details

https://recipeezy-app.herokuapp.com/shopping_list/ <-- this works in a similar manner as pantry. Purely a container to hold ingredient objects

### POST requests

https://recipeezy-app.herokuapp.com/ingredients/ 

```JSON
# input
{
  "name": "Ham"
}
# output
# 201
{
  "name": "Ham"
}
```

### PATCH requests

https://recipeezy-app.herokuapp.com/ingredients/1/ <-- make sure you designate which ingredient object we are going to PATCH

```JSON
# input
{
  "name": "Hammy"       <-- desired output
}
# output
# 200
{
  "name": "Hammy"
}
```

### DELETE requests

https://recipeezy-app.herokuapp.com/ingredients/1/ <-- make sure you designate which ingredient object we are going to DELETE

```JSON
# output
# 204 NO content
```

Now when you do a get request of all ingredients the ingredient we selected will be gone

## mealdb endpoints

Let's make a GET request for a meal id that we have. 

https://www.themealdb.com/api/json/v2/9973533/lookup.php?i=52995

a few things to keep in mind for this in particular. "52995" is the meal id that we are searching for. 

The "v2" and the "9973533" are particular to us. This is matching the API key that was purchased so that we can do more advanced filters later.

I'll only show this full output once for the sake of space.

```JSON
# GET output
{
  "meals": [
    {
      "idMeal": "52995",
      "strMeal": "BBQ Pork Sloppy Joes",
      "strDrinkAlternate": null,
      "strCategory": "Pork",
      "strArea": "American",
      "strInstructions": "1\r\n\r\nPreheat oven to 450 degrees. Wash and dry all produce. Cut sweet potatoes into ½-inch-thick wedges. Toss on a baking sheet with a drizzle of oil, salt, and pepper. Roast until browned and tender, 20-25 minutes.\r\n\r\n2\r\n\r\nMeanwhile, halve and peel onion. Slice as thinly as possible until you have ¼ cup (½ cup for 4 servings); finely chop remaining onion. Peel and finely chop garlic. Halve lime; squeeze juice into a small bowl. Halve buns. Add 1 TBSP butter (2 TBSP for 4) to a separate small microwave-safe bowl; microwave until melted, 30 seconds. Brush onto cut sides of buns.\r\n\r\n3\r\n\r\nTo bowl with lime juice, add sliced onion, ¼ tsp sugar (½ tsp for 4 servings), and a pinch of salt. Stir to combine; set aside to quick-pickle.\r\n\r\n4\r\n\r\nHeat a drizzle of oil in a large pan over medium-high heat. Add chopped onion and season with salt and pepper. Cook, stirring, until softened, 4-5 minutes. Add garlic and cook until fragrant, 30 seconds more. Add pork and season with salt and pepper. Cook, breaking up meat into pieces, until browned and cooked through, 4-6 minutes.\r\n\r\n5\r\n\r\nWhile pork cooks, in a third small bowl, combine BBQ sauce, pickling liquid from onion, 3 TBSP ketchup (6 TBSP for 4 servings), ½ tsp sugar (1 tsp for 4), and ¼ cup water (⅓ cup for 4). Once pork is cooked through, add BBQ sauce mixture to pan. Cook, stirring, until sauce is thickened, 2-3 minutes. Taste and season with salt and pepper.\r\n\r\n6\r\n\r\nMeanwhile, toast buns in oven or toaster oven until golden, 3-5 minutes. Divide toasted buns between plates and fill with as much BBQ pork as you’d like. Top with pickled onion and hot sauce. Serve with sweet potato wedges on the side.",
      "strMealThumb": "https:\/\/www.themealdb.com\/images\/media\/meals\/atd5sh1583188467.jpg",
      "strTags": null,
      "strYoutube": "",
      "strIngredient1": "Potatoes",
      "strIngredient2": "Red Onions",
      "strIngredient3": "Garlic",
      "strIngredient4": "Lime",
      "strIngredient5": "Bread",
      "strIngredient6": "Pork",
      "strIngredient7": "Barbeque Sauce",
      "strIngredient8": "Hotsauce",
      "strIngredient9": "Tomato Ketchup",
      "strIngredient10": "Sugar",
      "strIngredient11": "Vegetable Oil",
      "strIngredient12": "Salt",
      "strIngredient13": "Pepper",
      "strIngredient14": "",
      "strIngredient15": "",
      "strIngredient16": "",
      "strIngredient17": "",
      "strIngredient18": "",
      "strIngredient19": "",
      "strIngredient20": "",
      "strMeasure1": "2",
      "strMeasure2": "1",
      "strMeasure3": "2 cloves",
      "strMeasure4": "1",
      "strMeasure5": "2",
      "strMeasure6": "1 lb",
      "strMeasure7": " ",
      "strMeasure8": " ",
      "strMeasure9": " ",
      "strMeasure10": " ",
      "strMeasure11": " ",
      "strMeasure12": " ",
      "strMeasure13": " ",
      "strMeasure14": " ",
      "strMeasure15": " ",
      "strMeasure16": " ",
      "strMeasure17": " ",
      "strMeasure18": " ",
      "strMeasure19": " ",
      "strMeasure20": " ",
      "strSource": "",
      "strImageSource": null,
      "strCreativeCommonsConfirmed": null,
      "dateModified": null
    }
  ]
}
```

Now let's back up a bit, we see what we would have if we had the meal id but how did we get the meal id.

Doing a GET request with a filter looks just a little different from the meal id lookup.

https://www.themealdb.com/api/json/v2/9973533/filter.php?i=chicken

In order to change what type of lookup we were doing we need to change "lookup" to "filter" in this endpoint but we also need to change what we are searching with. So for this example we are going to try searching chicken, so instead of have the meal id of "52995" we will have "chicken". This get request will ouput a bunch of meals with the ingredient chicken in it. 

```JSON
# GET output
{
  "meals": [
    {
      "strMeal": "Brown Stew Chicken",
      "strMealThumb": "https:\/\/www.themealdb.com\/images\/media\/meals\/sypxpx1515365095.jpg",
      "idMeal": "52940"
    },
    {
      "strMeal": "Chicken & mushroom Hotpot",
      "strMealThumb": "https:\/\/www.themealdb.com\/images\/media\/meals\/uuuspp1511297945.jpg",
      "idMeal": "52846"
    },
    {
      "strMeal": "Chicken Alfredo Primavera",
      "strMealThumb": "https:\/\/www.themealdb.com\/images\/media\/meals\/syqypv1486981727.jpg",
      "idMeal": "52796"
    },
# there are many more meals after
```

So now we know what the id's are of meals based off of a basic filtering of the api.

To filter even further is simple.

https://www.themealdb.com/api/json/v2/9973533/filter.php?i=chicken,garlic,salt

all we have to do is add a comma at the end of "chicken", then add the ingredient we want to filter by. This filtering though means that the meal MUST include all three ingredients otherwise it will show null for meals.

```JSON
# GET output
{
  "meals": [
    {
      "strMeal": "Chicken Alfredo Primavera",
      "strMealThumb": "https:\/\/www.themealdb.com\/images\/media\/meals\/syqypv1486981727.jpg",
      "idMeal": "52796"
    }
  ]
}
```

For this api that filter of chicken, garlic, and salt yeilded only one result. So filtering by many ingredients will often lead to very few results overall.

## Random!!

What if we wanted to generate a random recipe? well that can be done!

https://www.themealdb.com/api/json/v2/9973533/random.php

this wil give you one random recipe and all the desired key value pairs of a usual meal id lookup

but one random recipe is no fun, how about 10?

https://www.themealdb.com/api/json/v2/9973533/randomselection.php

This will give all the details for 10 recipes. So the output will look like a meal id but for 10 total recipes.

