# python-movie-recommendation-system
This code is a simple movie recommendation system based on three input features: feature1 (age), feature2 (gender), and feature3 (movie type). Depending on the values of these features, the code recommends a movie to the user.
![1_x8gTiprhLs7zflmEn1UjAQ](https://github.com/ivias2000/python-movie-recommendation-system/assets/125237611/f6908836-24ae-470f-88ed-57e81ccce644)

Here's how the code works:

The code defines three features:

feature1: The age of the user.
feature2: The gender of the user (represented by 'M' for male and 'F' for female).
feature3: The type of movie the user is interested in (represented by 'I' for "I" or "II").
The code defines age ranges in the ages list and gender and movie type options in the gender and m_or_s lists, respectively.

The code then checks the value of feature1 against the age ranges defined in the ages list. Based on the age range, it proceeds to check the values of feature2 and feature3.

The recommendation logic is organized into nested if-else statements:

If the user's age falls within a certain range, the code checks the gender and movie type preferences.
Depending on the combination of features, the code assigns a movie recommendation to the out variable.
If the combination of features does not match any of the defined cases, the code prints an error message.
Finally, the code prints the movie recommendation based on the chosen features.

For example:

If feature1 is between 16 and 35, feature2 is 'M', and feature3 is 'II', the code recommends the movie "'Peacky blinders'" to the user.
If feature1 is between 0 and 16, feature2 is 'F', and feature3 is 'I', the code recommends the movie "'Frozen'" to the user.
Remember, this is a simple recommendation system with a limited number of options. In a real-world scenario, a more extensive database of movies and more sophisticated recommendation algorithms could be used to provide more accurate and personalized recommendations.
