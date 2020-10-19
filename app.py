from flask import Flask, render_template
app = Flask(__name__)

students = [
    {
        'Id': 1,
        'Name' : 'koki',
        'Surname' : 'suleymanov',
        'Gender' : 'Male',
        'Status' : True,
        'Image' : 'https://image.shutterstock.com/image-vector/brunette-boy-curly-hairstyle-illustration-260nw-1310545991.jpg',
        'Bio' : ''
    },
    {
        'Id': 2,
        'Name' : 'Samir',
        'Surname' : 'Kerimli',
        'Gender' : 'Male',
        'Status' : False,
        'Image' : 'https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg',
        'Bio' : ''

    },
    {
        'Id': 3,
        'Name' : 'Nergiz ',
        'Surname' : 'Agayeva',
        'Gender' : 'Female',
        'Status' : True,
        'Image' : 'https://i.pinimg.com/originals/f0/a6/4e/f0a64e32194d341befecc80458707565.jpg',
        'Bio' : 'Doctor'
    },
    {
        'Id': 4,
        'Name' : 'XXX ',
        'Surname' : 'YYY',
        'Gender' : 'FFF',
        'Status' : True,
        'Image' : 'https://i.pinimg.com/originals/f0/a6/4e/f0a64e32194d341befecc80458707565.jpg',
        'Bio' : 'Doctor'
    }

]

@app.route("/students/")
def student_list():
    return render_template('main.html', students=students)

@app.route('/students/<int:student_index>')
def student_bio(student_index):

    student = list(filter(lambda student: student['Id'] == student_index, students))[:1]
    print(list(filter(lambda student: student['Id'] == student_index, students)))
    print(student)
    return render_template('index.html', students   =student)


if __name__ == '__main__':
    app.run(debug=True, port=5000)