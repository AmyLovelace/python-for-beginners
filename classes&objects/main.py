from user import User
from post import Post
app_user_one = User("amy@gmail.com", " ami sauria", " ami666", "developer")
app_user_one.get_user_info()

app_user_two=User("adel@gmail.com"," adelin bombin","hermanoso profesional","jedi")
app_user_two.get_user_info()

new_post=Post("on a mission to be the baddest bitch alive", app_user_two.name)
new_post.get_post_info()