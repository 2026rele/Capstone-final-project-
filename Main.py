important flet as ft

def main (page : ft.page) :
page title = "(capstone final - music library"
page.vertical_alignment=ft. MainAxisAlignment.CENTER
page.Horizontal_alignment=ft. CrossAxisAlignment.CENTER
page.padding=20

title=ft.Text(" Capstone Final Project", size=30, weight="bold")
Subtitle = ft.Text(" My Flet Music Library App",Size=16

song_input = ft.TextField(label="Add a song width=300,hint_text="Enter song name)
song_list = ft.column()

def add_song(e):
if song_ input.value:
song_list.controls.append(ft.text(ft.Text(f🎵 song input value:
song_input. value =""
page.update ()

add_ btn = ft.Elevatedbutton("Add song", on_click=add_song)
page.add(title, subtitle ,f.Devider(),song_input,add_btn,song_list)
ft.app(target= main)
