# WebBrowserStart
Web browser start up project (Python, JSON)

This program allows users to create and save a list of websites as playlists (stored as json files) and quickly open them in their default web browser. The python libraries used in this program are webbrowser, json, and os. The program in its current state can only be run in the terminal.

Program Features:

1. Create a Playlist: 
The user can create a playlist name of their choosing, which will be saved as a .json file with an empty list.

2. Remove a Playlist: 
The user can also choose to remove a playlist. However, doing so will delete all of the playlist data. There is no confirmation to remove yet, so be mindful when utilizing this feature.

3. Add a website to a Playlist: 
The user can select a playlist to add to and then will be asked to enter the website's URL. I would recommend copying the URL from your browser and then pasting it into the terminal. The website will then be appended to the respective .json file.

4. Remove a website from a Playlist: The user can choose a playlist to remove from and then will be prompted with a numbered list of websites in the playlist. The user will then be asked to enter the number that corresponds with the website they want removed.

5. Start a Playlist: The user can select a playlist to run, which will promptly open all of the websites in the playlist in the user's default browser.

Additional Notes: The program will continue to run until told otherwise, so you can make multiple edits without having to continuously run the program. However, the program will end once you decide to start/run a playlist.


  




