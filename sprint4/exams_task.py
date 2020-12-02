class Testpaper:

    def __init__(self, subject, correct_answers_array, pass_mark_grade):
        self.subject = subject
        self.correct_answers_array = correct_answers_array
        self.pass_mark_grade = pass_mark_grade


class Student:

    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test_obj, answers_given) -> None:
        if not isinstance(test_obj, Testpaper):
            raise ValueError(f'Invalid type of test_obj is passed in. It is {type(test_obj)} but {Testpaper} expected!')
        test_mark = self.get_test_mark(correct_answers=test_obj.correct_answers_array, answers_given=answers_given)
        min_pass_mark = float(test_obj.pass_mark_grade.split('%')[0])
        # initialize tests_taken
        if isinstance(self.tests_taken, str):
            self.tests_taken = dict()
        if test_mark >= min_pass_mark:
            self.tests_taken[test_obj.subject] = f'Passed! ({round(test_mark)}%)'
        else:
            self.tests_taken[test_obj.subject] = f'Failed! ({round(test_mark)}%)'

    @staticmethod
    def get_test_mark(correct_answers: list, answers_given: list) -> float:
        correct_answers_given = set(correct_answers) & set(answers_given)
        mark = 100 * len(correct_answers_given) / len(correct_answers)
        return mark


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()
print(student1.tests_taken) #➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken) #➞ {"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken) #➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}
