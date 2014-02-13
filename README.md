Python_Extract_Data
===================

This python script is mainly extract EPL soccer scores and line-up of two teams of each battle from 
http://espnfc.com/results/_/league/eng.1/barclays-premier-league?cc=5901

These data are used for training data for the Machine Learning Project, which predicts the outcome of socer competitions.

This script is writen in 2.7.5 using BS4 to parsing the html of webpages.
The csv file contains the home team, socres and away team.
The txt file records line-up of each team in each battle. Due to the txt is ascii, I skip the unascii content of some player.

