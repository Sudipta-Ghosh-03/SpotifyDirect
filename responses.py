import spotipytest


def handle_response(message) -> str:
    p_message = message
    if p_message == 'hello' or p_message == 'hi':
        return 'Hey there!'

    if p_message == '!help':
        return "`Send song to add to the Collaborative Playlist. I can also say Hi`"
    
    if p_message.startswith("https://open.spotify.com/track/"):
        return "Song added to playlist"
    
    
