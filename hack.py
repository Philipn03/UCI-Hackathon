from lyricsgenius import Genius
from random import randint


token = 'YgA-6bzr9j6WIvfOtp1H2Brr7IUvYD9qRyzO5zCzUhFJQQ11BGiuJ_Wa-M1VDxpD'

def getSong(artist1, song1):
    list1 = []
    list2 = []
    list3 = []
    list4 = []

    genius = Genius(token)
    artist = genius.search_artist(artist1, max_songs=1, sort="title")  # Artist
    song = genius.search_song(song1, artist.name)                        # Song
    song = artist.song(song1)                                           # Song

    
    p = song.lyrics.split('\n')
    t = []
    for i in p:
        t.append(i)
        list1.append(t)
        t = []

    counter2 = 0
    for i in range(0, len(list1)):
        for inner_list in list1[i]:
            word_list = inner_list.split(' ')
            if len(word_list) == 1:
                list2.append(word_list)
            else:
                random_index = randint(0, len(word_list)-1)
                list4.append(word_list[random_index])
                counter2 += 1
                word_list[random_index] = "___"
                list2.append(word_list)

    entire_string = ''        
    for lst in list2:
        for s in lst:
            entire_string += s
            entire_string += " "
        list3.append([entire_string])
        entire_string = ''

    huge_str = ''

    for i in list3:
        for k in i:
            huge_str += k
            huge_str += '\n'

    # user = ["Youngblood", "touch", "bridge", "love", "you", "close", "ghost", "life", "can't", "ecstasy", "life", "miss", "always", "more", "behind", "love", "you", "close", "ghost", "miss", "can't", "memory", "miss", "miss", "close", "settle", "But", "be", "is", "you", "you"]
    # correct = 0
    # incorrect = 0
    # for i in range(len(list4)-1):
    #     if list4[i] == user[i]:
    #         correct += 1
    #     else:
    #         incorrect += 1
    # print(correct, " / ", counter2, "    You got ", incorrect, " lyrics wrong!")

    return {
        'emptyLyrics': huge_str,
        'answers': list4
    }

# getSong('Justin Bieber', 'Ghost')




