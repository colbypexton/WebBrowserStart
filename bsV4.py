#playlists.json required to use program.
#work.json & coding.json are example playlists.

import webbrowser
import json
import os


def dataopen():
    playlistnames = []
    with open('playlists.json') as file:
        extplaylists = json.load(file)
    playlists = extplaylists
    for i in playlists:
        new = i.replace('.json','')
        playlistnames.append(new)
    return playlistnames

def newpl():
    plnames = dataopen()
    plnames.append(input('Enter the name of your new playlist:'))
    print('\n\nPlaylists:')
    for i in range(len(plnames)):
        print(f'{i+1}. {plnames[i]}')
    print('Playlist has been added!')
    for i in range(len(plnames)):    
        cvjson = plnames[i]+'.json'
        plnames[i] = cvjson
    target = len(plnames)
    with open(plnames[target-1], 'w') as newfile:
        json.dump([], newfile)
    with open('playlists.json', 'w') as upfile:
        json.dump(plnames, upfile)
    
def removepl():
    plnames = dataopen()
    print('\n\nPlaylists:')
    for i in range(len(plnames)):
        print(f'{i+1}. {plnames[i]}')

    position = int(input("Enter the number that corresponds to the playlist you want to remove:"))
    if position-1 > len(plnames) or position-1 < 0:
        print("Not a valid choice.")
    elif position-1 in range(len(plnames)):
        folderpath = os.getcwd()
        targetfile = f'{folderpath}\{plnames[position-1]}.json'
        os.remove(targetfile)
        del plnames[position-1]
         
        print('\n\nPlaylists:')
        for i in range(len(plnames)):
            print(f'{i+1}. {plnames[i]}')
        print('Playlist has been removed!')

        for i in range(len(plnames)):    
            cvjson = plnames[i]+'.json'
            plnames[i] = cvjson
        
        with open('playlists.json', 'w') as upfile:
            json.dump(plnames, upfile)
    
def convjson(playlistname):
    cvjson = playlistname+'.json'
    return cvjson   

def add_website():
    plnames = dataopen()
    print('\n\nPlaylists:')
    for i in range(len(plnames)):
            print(f'{i+1}. {plnames[i]}')
    decision = int(input('Enter the number that corresponds with the playlist you want to edit:'))
    if decision-1 > len(plnames) or decision-1 < 0:
        print("Not a valid choice.")
    elif decision-1 in range(len(plnames)):
        playlist = convjson(plnames[decision-1])
        storeadd(playlist)

def storeadd(filename):
    with open(filename, 'r+') as f:
        filedata = json.load(f)

    filedata.append(input("Enter the URL of the website you want to add:"))

    with open(filename, 'w') as upfile:
        json.dump(filedata, upfile)
    print('\n\nWebsites:')
    for i in range(len(filedata)):
            print(f'{i+1}. {filedata[i]}')
    print('\nWebsite has been added!')
    
def remove_website():
    plnames = dataopen()
    print('Playlists:')
    for i in range(len(plnames)):
        print(f'{i+1}. {plnames[i]}')
    decision = int(input('Enter the number that corresponds with the playlist you want to edit:'))
    if decision-1 > len(plnames) or decision-1 < 0:
        print("Not a valid choice.")
    elif decision-1 in range(len(plnames)):
        playlist = convjson(plnames[decision-1])
        storeremove(playlist)

def storeremove(filename):
    with open(filename, 'r+') as f:
        filedata = json.load(f)
    
    print('\n\nWebsites:')
    for i in range(len(filedata)):
        print(f'{i+1}. {filedata[i]}')
    
    position = int(input('Enter the number that corresponds with the website you want removed:'))
    del filedata[position-1]

    with open(filename, 'w') as upfile:
        json.dump(filedata, upfile)
    print('\n\nWebsites:')
    for i in range(len(filedata)):
            print(f'{i+1}. {filedata[i]}')
    print('\nWebsite has been removed!')

def check_action():
    if action == 'm':
        decision = input('Do you want to add or remove a playlist? type [add or remove]:')[:1].lower()
        if decision == 'a':
            newpl()
        elif decision == 'r':
            removepl()
        else:
            print('Invalid Option!')
    elif action == 'e':
        decision = input('Do you want to add or remove a website from a playlist? type [add or remove]:')[:1].lower()
        if decision == 'a':
            add_website()
        elif decision == 'r':
            remove_website()
        else:
            print('Invalid Option!')
    else:
        print('Invalid Start Mode!')

def runplaylist():
    plnames = dataopen()
    print('\n\nPlaylists:')
    for i in range(len(plnames)):
        print(f'{i+1}. {plnames[i]}')
    decision = int(input('Enter the number that corresponds with the playlist you want to run:?'))
    if decision > len(plnames) or decision-1 < 0:
        print("Not a valid choice.")    
    elif decision-1 in range(len(plnames)):    
        playlist = convjson(plnames[decision-1])
        with open(playlist, 'r+') as f:
            playlistdata = json.load(f)
        for website in playlistdata:
            webbrowser.open(website)
        

#Actual Script
print('Welcome to the browser start-up!')
decision = 'Y'
while decision.upper() == 'Y':
    action = input('Do you want to start the program, manage your playlists, or edit your playlists? \ntype [start, manage, or edit]:')[:1].lower()
    mode = check_action()
    if action != 's':
        decision = input('Do you want to run the program again?')[:1]
    elif action == 's':
        runplaylist()
        break
