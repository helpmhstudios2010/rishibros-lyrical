import customtkinter as CTk
import core.lyrics as lyrics
import core.spotify_link as spotify_link

def sync_spotify():
    try:
        link = spotify_link.SpotifyLink()
        name,artist = link.name()
        song_lyrics = lyrics.get_lyrics(name,artist)
        display_lyrics(name + " by " + ",".join(artist) + "\n\n" +song_lyrics)
        time_left = link.time_remaining()
        if time_left!=None:
            window.after(ms=time_left+50,func=sync_spotify)
    except TypeError:
        window.after(ms=10000,func=sync_spotify)
        countdown()
        

timer = 10
def countdown():
    global timer
    if timer > 0:
        display_lyrics(f"Error. Retrying in {timer} seconds")
        timer-=1
        window.after(ms=1000,func=countdown)
    else:
        timer= 10

def display_lyrics(lyrics:str):
    lyrics_textbox.configure(state="normal")
    lyrics_textbox.delete("0.0","end")
    lyrics_textbox.insert("0.0",lyrics)
    lyrics_textbox.configure(state="disabled")

        
window = CTk.CTk()
window.title("Lyrical")
window.geometry("600x420")
CTk.set_appearance_mode("system")
CTk.set_default_color_theme("dark-blue")
#making a larger font
font = CTk.CTkFont(size=18)
#button to sync with spotify
    


lyrics_textbox = CTk.CTkTextbox(window,font=font,state="disabled",height = 420,width= 780,fg_color="#242424")
def change_height(instance):
    window.unbind("<Configure>")
    lyrics_textbox.configure(height=instance.height)
    window.bind("<Configure>", func=change_height)

sync_button = CTk.CTkButton(window,text="Resync", fg_color="#111111", text_color="#1bc256", corner_radius=30,height=30,width=75,command=sync_spotify)





#placing all the elements

lyrics_textbox.place(x=20,y=20)
sync_button.place(x=475,y=20)
window.bind("<Configure>", func=change_height)
sync_spotify()
window.mainloop()