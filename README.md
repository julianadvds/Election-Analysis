# Election-Analysis
Python Module #3

## Overview of Election Audit
The purpose of the election audit was to analyze the individual votes from 3 different counties.  The audit provides the total number of votes across all candidates and counties, the total number of votes per county and the winning candidate.

## Election-Audit Results
    •There were a total of 369,711 votes cast in the congressional election

    •The votes cast in each county were as follows:
        •Jefferson County: 38,855 votes, 10.5% of the total votees
        •Arapahoe County: 24, 801 votes, 6.7% of the total votes
        •Denver County: 306,055, 82.8% of the population

    •The county with the the largest number of votes is Denver County

    •The votes cast for each candidate were as follows:
        •Charles Casper Stockham:  85,213, 23.0% of the total votes
        •Diana DeGette: 272,892,  73.8% of the total votes
        •Raymon Anthony Doane: 11,606, 3.1% of the total votes

    •The winning candidate of the election was: Diana DeGette, with 272,892 total votes which is 73.8%

## Election Audit Summary
This script is an excellent foundation on which to build the analysis of future elections.  While this election evaluated 3 specific candidates in 3 specific counties, the future this election could be scaled to be used at any level of government and with any number of candidates and counties.  

To modify the current code to scale this analysis to the state/province level, where the code explicitly calls out "county", the code could be updated to show "State", "Province" or even "Country".  These changes would need to happen across all variables to maintain the readability of the code.  An example of where these updates need to be made can be foundhttps://github.com/julianadvds/Election-Analysis/blob/main/Resources/County_images.PNG.  Note that the csv data would need to also be updated. 

The data could also be modified to declare the winning candidate for each county.  That could be further coded to tally the candidates that have won in each county and sum those up to find a regional winner.  By modifying the code to include new for loops to calculate the winning candidate per county and to print that information we can see where each candidate has been sucessful.  Using a for loop as well to tally the number of counties each candidate has won will give further possiblities to evaluate election and make it suitable to scale.

    
