Technical Documentation

//=============================================================================
//  Tkinter style/GUI classes

Set these up for overview, and to have the style at the start of document before the functions.
//=============================================================================
//  FIRE ASCII animation

        Self built ASCII animation, based upon an image turned ASCII
        mirrored the two, and built a little loop that constantly alternates between the two"""
//=============================================================================
//  Readme launcher

get_readme:                 Grabs the readme from the projectfolder
open_new_window_readme:     runs a new tkinter window with readme data
//=============================================================================
//  Do-not-press programme (virus)

Little easter egg
runs a basic countdown timer that updates screen, and then eventually shutsdown everything.
shutdowncommand:        button to press in GUI
//=============================================================================
//  Review-O-Meter 2000 (review-score-servo)

gradenaanwijziging:     function to change position servo based upon input
args= value between 0-100
//=============================================================================
//  SPLASHSCREEN ~ setup, load list, motion seq., initial fill, main programme

Basic set up of splashscreen
change_label:   Runs to change the loading image from list
delayed_start:  Basic splashscreen programme (.after to update tkinter while running)
//=============================================================================
//  API pulling programme

create:                     creeert een database, als deze al bestaat, dan pass'd ie
insert_alltime_games_page1: requests data from API and coordinates this into a SQL
API_PULL:                   loop to run through an api pull and message into splash
//=============================================================================
//  splashscreen programme:

This loading screen, keeps the user entertained while retrieving data from steamspyAPI"""
//=============================================================================
//  Database functions - Search in database - show in treeview

Showtable: shows the database that was built from the api request
write_searchresults: stores search results in a *.json, for use in the AI search functions.
search(): searches in the DB using user input and SQL query
sort_by(): sorts data based on alphabetical or numeric order
reset(): resets column """
//=============================================================================
//  Treeview programme:


//=============================================================================
//  TREEVIEW ~ window, style, data, scrollbar, column-sorting-function

//=============================================================================
//  Search function Tkinter layout

//=============================================================================
//  AI searched functions

get_lastsearch:                 grabs the last search data from the fresh .json
list_first_game:                lists the first game in the .json from last search
list_game_developers            creates a list of game devs in json from last search
first_gameDev_inlist            shows first gamedev in list from previous function
avg_positive_game_rating:       calculates average amount of pos ratings in list
avg_neg_game_rating:            calculates average amount of pos ratings in list
avg_gamescore:                  defines an avg score of the last searched items between 0-100
**********************************************************************************
//  TREEVIEW ~ Data insert, styles

//=============================================================================
//  GUI - main programme

//=============================================================================

