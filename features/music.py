import random
import webbrowser

def play_music():
    musics = [
        "https://youtu.be/RLzC55ai0eo?si=MXatztxYEeYJrH3O",
        "https://youtu.be/tBgNpc39FJk?si=G23Ndy1Pp-fTuquU",
        "https://youtu.be/5UfGZFrXKig?si=HZ8KK-3grS8YsZjp",
        "https://youtu.be/1BEPDAGR39o?si=7o5YqzwiLh9mJK2O",
        "https://youtu.be/E7ww8Xowydc?si=IJPGoLTHqNZYO1z9",
        "https://youtu.be/gh3FyLT7WVg?si=H9TI-CtdLB9IXt9H",
        "https://youtu.be/MsXdUtlDVhk?si=pW0Lo-gAr_0Z9NrI",
        "https://youtu.be/a6j5lbt6OLQ?si=-3dscX6k28dgsz3T",
        "https://youtu.be/gEg0yuEz15Q?si=dNIn3eWpWDOUG0XF",
        "https://youtu.be/CYDP_8UTAus?si=Q_d4bUmMeKiz2AFR",
        "https://youtu.be/WeiM_vffWAw?si=iJi-FIscY37QnKW8",
        "https://youtu.be/Ccsh_-Cucl4?si=9OFNUL2x1LyYEEfw",
        "https://youtu.be/q5NQqwP7Rxs?si=vFlKXaHokmc3xKF7",
        "https://youtu.be/_looX7vZ3-g?si=6JT_3AoN9EQ4sjhL",
        "https://youtu.be/DEpO-Oh3MAw?si=g_Eyp6amBSYSQgDP",
        "https://youtu.be/HkVIGyMMwv0?si=0-i75f6XvrSxNUYY",
        "https://youtu.be/3uBus1Gduq4?si=c5JGoO-vHnrK9HhJ",
        "https://youtu.be/jgRJip37Skw?si=ofzFfyEYaf0_ThXj",
        "https://youtu.be/iLQ2UX1tUaw?si=mhIEn3bFDxLNRNSA",
        "https://youtu.be/9uYhFfXXtwA?si=mUav6lJUFwnywsQi",
        "https://youtu.be/x48kgfc-_NM?si=dtQfe7oT0ikB66-e",
        "https://youtu.be/W7NWnqB8dQE?si=saKAB2QCGK3s8bft",
        "https://youtu.be/6WhefAhgeQw?si=12a3WSzKzCuaxGSC",
        "https://youtu.be/QNZy8aNPIeE?si=Jyk-6YmEjDcct_VJ",
        "https://youtu.be/_70Q-Xj3rEo?si=rGsFQhr05Dgfi_g6",
        "https://youtu.be/JOQUnRjdqKA?si=as4OeqcQJnAawwck",
    ]

    url = random.choice(musics)  # Use random.choice to get a single string
    print(url)
    webbrowser.open(url)

