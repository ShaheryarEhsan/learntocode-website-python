import webbrowser
import websitecode
#Different Classes For Learn To Code
class Tutorials():

    
    def __init__(self, vid_title, vid_poster, vid_description,vid_link):
        self.title = vid_title
        self.poster_image_url = vid_poster
        self.description = vid_description
        self.trailer_youtube_url = vid_link


    def playlecture(self):
        webbrowser.open(self.link)








#User Program
l1 = Tutorials(vid_title="Programming 101",
                         vid_poster="D:\Learn To Code Python Presentations\How A Computer Understands Data\Slide1.JPG",
                         vid_description="Welcome to our first lecture on the basics of Programming",
                         vid_link="https://www.youtube.com/watch?v=lJnvq0A_7WQ")


l2= Tutorials(vid_title="Different Data Types",
                         vid_poster="D:\Learn To Code Python Presentations\Different Variable Data Types In Python\Slide1.JPG",
                         vid_description="A variable is a character whose value is unknown or is bound to change. In our second lecture, we’ll study different data types of variables in Python.",
                         vid_link="https://www.youtube.com/watch?v=657yt4gYjRo")

l3= Tutorials(vid_title="Integers, Strings and Floats",
                         vid_poster="D:\Learn To Code Python Presentations\Different Variable Data Types In Python\Slide2.JPG",
                         vid_description="A variable is a character whose value is unknown or is bound to change. In our second lecture, we’ll study different data types of variables in Python.",
                         vid_link="https://www.youtube.com/watch?v=2qRhruGoJ2Y")


l4= Tutorials(vid_title="Boolean Data Types",
                         vid_poster="D:\Learn To Code Python Presentations\Different Variable Data Types In Python\Slide3.JPG",
                         vid_description="A variable is a character whose value is unknown or is bound to change. In our second lecture, we’ll study different data types of variables in Python.",
                         vid_link="https://www.youtube.com/watch?v=9OK32jb_TdI")


l5= Tutorials(vid_title="Integers",
                         vid_poster="D:\Learn To Code Python Presentations\Different Variable Data Types In Python\Slide4.JPG",
                         vid_description="A variable is a character whose value is unknown or is bound to change. In our second lecture, we’ll study different data types of variables in Python.",
                         vid_link="https://www.youtube.com/watch?v=DuJmL-YUa4A")

l6= Tutorials(vid_title="Strings",
                         vid_poster="D:\Learn To Code Python Presentations\Different Variable Data Types In Python\Slide5.JPG",
                         vid_description="A variable is a character whose value is unknown or is bound to change. In our second lecture, we’ll study different data types of variables in Python.",
                         vid_link="https://www.youtube.com/watch?v=HWRnnfkeEW8")

l7= Tutorials(vid_title="Floats",
                         vid_poster="D:\Learn To Code Python Presentations\Different Variable Data Types In Python\Slide6.JPG",
                         vid_description="A variable is a character whose value is unknown or is bound to change. In our second lecture, we’ll study different data types of variables in Python.",
                         vid_link="https://www.youtube.com/watch?v=g4bYN2GVeHc")


vid_list=[l1,l2,l3,l4,l5,l6,l7]
websitecode.open_movies_page(vid_list)
