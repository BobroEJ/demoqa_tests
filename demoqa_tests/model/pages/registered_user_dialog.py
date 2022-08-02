from demoqa_tests.model.controls.table_row import TableRow


class RegisteredUserDialog:

    def __init__(self):
        self.full_name = TableRow(0)
        self.email = TableRow(1)
        self.gender = TableRow(2)
        self.mobile_number = TableRow(3)
        self.date_of_birth = TableRow(4)
        self.subjects = TableRow(5)
        self.hobbies = TableRow(6)
        self.picture = TableRow(7)
        self.address = TableRow(8)
        self.state_and_city = TableRow(9)
