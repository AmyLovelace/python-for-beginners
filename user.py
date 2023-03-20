# funciones que le pertenecen a un objeto se llaman metodos methods
class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(
            f"user{self.name} currently works as a {self.current_job_title}. you can contact them at {self.email}")


app_user_one = User("amy@gmail.com", " ami sauria", " ami666", "developer")
app_user_one.get_user_info()

app_user_two=User("adel@gmail.com"," adelin bombin","hermanoso profesional","jedi")
app_user_two.get_user_info()

