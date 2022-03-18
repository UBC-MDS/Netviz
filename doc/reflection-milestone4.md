# Milestone 4 Reflection: NetViz: Dashboard App
================
> Authors: Lianna Hovhannisyan, Lynn Wu, Simon Guo, Nobby Nguyen

## 1. What we have implemented:

Within the scope of this course, we have implemented most of the points outlined in our proposal, including:

1.  An interactive bar chart of `Genres` and `Ratings` to describe rating distribution of each genre.

2.  An interactive line chart of `Genres` and `Release Year` to descibe how many movies of the genre were released over time.

3.  An interactive map of `Genres` and `country` of origin to illustrate movie counts by country for each genre.

4.  An interactive table of the movies in the selected `Genres`  with information about movie title, description, director, release year and duration.

These implementations are included in both `Python` and `R` with almost identical outlook and functionalities. 

- [Python Dashboard](https://dsci532-2022-group3-netviz.herokuapp.com/)

- [R Dashboard](https://dsci532-2022-group3-netviz-r.herokuapp.com/)

The only major difference between the dashboard in `R` and `Python` is that: in `R` the table of movies has only 3 columns compared to 5 in `Python` dasboard. Other minor differences include styling colors, plot names, widget position.

## 2. What we all agreed not to implement:

In our proposal, we considered both `TV show` and `Movie` types of the data set. However, after thorough discussion, we decided to concentrate on the `Movie` type only. Because the data of `TV show` only accounts for 30% of the dataset, if we included `TV show`, the dashboard would have not given much meaningful insights. 

In addition, we did not implement the duration sliding bar, which appeared in our proposal. After discussion as a group, we felt it to be a redundant feature since we can find that information from the table of movies.  

## 3. How we have improved our Dashboard in this Milestone: 

We welcome and appreciate all feedback received from TA and our peers. Our work can be enhanced with the views from different angles so that the dashboard can be more user friendly and bring more values to stakeholders. 

Some of the very helpful feedback include: (1) the styling of our dashboard such as plot coloring for readability, (2) plot size for the map, (3) better description of variables in our readme document, and last but not least (4) widget to input country of interest.

- In response to our peers' feedback, we have fixed our dashboard with details in the following link: 
[Addressing the feedback from peers](https://github.com/UBC-MDS/DSCI532-peer-review/issues/7)

## 4. NetViz: Dashboard App Usability

- The dashboard is well organized and plots overall work well, with each plot showing detailed information while hovering over the point.

- The widget and the interactivity work as expected. 

- The documentation was very clear and intuitive for users to use and follow.


## 5. NetViz: Dashboard App Limitations

The limitations of our dashboard include:

- The dashboard can only utilize the movie part of the dataset. It could have been better if we also included `TV Show`.
- The number of features are limited in this dataset. We could have included more interactive widgets if we had more features of the data to work on such as `vote counts`, `budget`, `revenue`, `profit`
-  It would be great if we can implement complete reproducibility. For example, this dashboard will not get updated if Kaggle/Netflix releases more recent dataset on their website.


## 6. Potential improvements

If we had more time in the future, we could implement the following features:

-   Implement complete reproducibility. This is most especially important for the underlying dataset so that the dashboard gets updated as soon as Kaggle/Netflix releases updated data.
-   Also, we would use a larger dataset and/or dataset with more features to include `TV Show`, or to add more widgets to our dashboard.
-   We would add another widget to input the country of interest that users want to target to display just the figure for that specific country.
