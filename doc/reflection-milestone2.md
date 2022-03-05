NetViz: Reflection of the MVP
================

As a minimum Viable Product, we implemented four charts in our dashboard for Netflix data: bar chart of rating, line chart for release year, world map chart, and the table displaying available movies title, director name, description. The detailed information for each plot can be found in our readme file. 

All four plots are filtered per the user's choice of the genre of the movie. By default 'comedy' genre is chosen. As an improvement of the filtering, later on, we want to add the option of having an option of `no genre` choice in the dropdown menu. 

The plots overall work well, with each plot showing detailed information while hovering over the point. Rating plot sizing is not perfect, as whenever we have not many genres present after filtering, its size shrinks, making it less than the length of the release plot. Similarly, the map plot is not perfect, as after the second time of filtering the countries where no movie was made based on the genre disappear from the map, making the shape of the shown countries appear unsymmetric. Even though, if we hover over the shape, it will show the country name, we still need to improve this for product launch. 

In our proposal, we considered both `TV show` and `Movie` types of the data set. However, upon discussion, we decided to concentrate on the `Movie` type only for MVP and reconsider having `TV show` back if time allows during product launch. 

Also, we did not implement the duration component/filter, which appeared in our proposal. After discussion as a group, we felt it to be a redundant feature, however further discussions are going to be in place later on of dashboard development. 

Overall, we have a lot of places to improve our UI/UX design, as well a good addition can be the creation of more plots and filtering choices for the users to have more insights into the data.

