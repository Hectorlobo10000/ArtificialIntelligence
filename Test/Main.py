import Functions.Function
import Functions.Human
import Functions.Student
import Functions.Teacher

def main():
    Functions.Function.Greet('Lola')

    hector = Functions.Human.Human('Masculino',24, 'Hector')
    print("{} : sexo es {} y la edad es {}".format(hector.GetName(), hector.GetSex(), hector.GetAge()))

    Fernando = Functions.Student.Student()
    Fernando.SetName('Hector')
    Fernando.SetSex('Masculino')
    Fernando.SetAge(24)
    print("{} : sexo es {} y la edad es {}".format(Fernando.GetName(), Fernando.GetSex(), Fernando.GetAge()))


main()
