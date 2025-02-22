
# Fashion-Trend
#Identifying Current Trends
To extract current trends, we make use of e-commerce websites. But why?
E-commerce websites like Myntra,Flipcart, Nordstorm etc. give a good representation of what people are liking and buying online. The reviews, rating, number of rating, number of reviews give a good impression of what today's trends are. It gives an indirect representation of how a product is doing in the market. A good product would have more positive reviews and higher ratings. This would show that the particular product has features that are being liked by the audience. We can use the images provided by the e-commerce websites to come up with a mood board which showcases what is trending and what is not!


#The Dataset 
The dataset consists of data scraped from various e-commerce websites. The details scraped are shown here.
![Screenshot (52)](https://github.com/user-attachments/assets/a1f79f47-6dcc-4aac-b2de-71feebad3690)



#Judging the Sentiment Attached with Each Product 😄/😐/ 😞
Here, we make use of the rating, number of people who rated, reviews and number of people who reviewed to understand whether the product is doing well in the market. 
The Vader Polarity Score is a measure of how postive or negative a certain piece of text is. The relation between these aspects would be:
![TOTAL score](https://github.com/user-attachments/assets/509aa77e-d78e-43bc-b0bd-14927dd2bf53)

We decided upon this equation because we feel that the positivity score is directly proportional to the above features.
We pick the top 5 and bottom 5 products based on their final score. These products are displayed in the current trends section.

#Concepts and Tech Stack Used 
The concepts and tech stack used here are:

Web scraping (Python)

Natural Language Processing (Python)

a. Sentiment Analysis

b. Bigram Analysis

Data Visualizations

![Current Trend Analysis](https://github.com/user-attachments/assets/a0106525-c46a-45e1-94a2-b48cba3317c9)




