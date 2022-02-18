NetViz: Proposal
================
Lianna Hovhannisyan, Lynn Wu, Simon Guo, Nobby Nguyen

-   [Motivation and Purpose](#motivation-and-purpose)
-   [Description of the data](#description-of-the-data)
-   [Research Questions and Usage
    Scenarios](#research-questions-and-usage-scenarios)

# Motivation and Purpose
#### Our role: The Data Analytics Department in a Company
#### Target Audience: Company's shareholders/stakeholders

Since the end of 2019, we have seen two rather tumultuous years in the entertainment industry. Lockdown measures enforced due to the Covid-19 pandemic brought about a surge in TV watching and online streaming. Therefore, more and more media companies are investing in their own streaming services to accommodate the increasing demand of online streaming of the users. 

In order to pick up on the new trend of online streaming in the next few years, it is integral for new streaming platforms to know where the industry is going. As regional differences have brought some troublesome for users in different countries; hence global consolidation streaming is expected be a new trend. As such, insights extracted from data of global giant name as Netflix are great resources for these platforms to decide their business strategy. 

To overcome this obstacle, we propose building a data visualization app that allows stakeholders in the streaming companies to explore a dataset of Netflix to determine the popular content that they need to provide to their users, or to invest in which genre of the original content. The app will show the distribution of movie genres over time and over the countries of origin, as well as the movie/tvshows rating to target the right market segment.
# Description of the data

We will be visualizing a dataset of approximately 8,800 movies or TV shows on Netflix. In this dataset, 70% of the items are movies and 30% are TV shows, which were added on Netflix from 2008 to 2021. Other than the unique identifier column (`show_id`), each row of record has 11 associated variables that describes the movie or TV show. These variables include movie or TV show identifier (`type`), basic information about the movie or TV show (`title`, `director`, `cast`, `country`, `release_year`, `duration`), date that the movie or TV show was added on Netflix (`date_added`), genre (`listed_in`), rating score on Netflix (`rating`), and a pure text summary column about the movie or TV show (`description`).

# Research Questions and Usage Scenarios

Benjamin is an executive for the new streaming platform, Cinya, which
secured a partnership with such studios as MGM. He understands that it
will be hard to beat such giants as Netflix in streaming movies or TV
shows, thus he decides instead of viewing Netflix as a rival, view them
as a giant on which data insights Cinya should stand. Benjamin wants to
explore a data set of Netflix movies and TV shows to identify the most
popular ratings among viewers for movies, the most popular genres, and
most importantly the Netflix’s preferable month for releasing content.
By exploring NetViz, he also notices that the most popular genre for TV
shows is ‘International’, thus he decides to get partnerships with
international studios for exclusive content for Cinya.

After knowing all of these insights, Benjamin comes up with the strategy
of the releases for each new content, as well as in which genre of
movies to invest more for original content. To convince Cinya’s
shareholders of the righteousness of the decided policy, he shows NetViz
visualizations and highlights the trends/patterns during his
presentation.
