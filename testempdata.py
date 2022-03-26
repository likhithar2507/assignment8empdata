import sqlite3 as sql
import unittest

class Checking_name_of_employee(unittest.TestCase):
    def setUp(self):
        self.empname1="Tom"
        self.empname2="John"
        self.empname3="Samuel"
        self.empcode1="1101"
        self.empcode2="1102"
        self.empcode3="1103"
        self.connection=sql.connect("EmployeesData.db")

    def tearDown(self):
        self.empname = " "
        self.empcode = " "
        self.connection.close()

    def test_verify_employee_name1(self):
        result=self.connection.execute("select empname from Employee where empcode="+self.empcode1)
        for i in result:
            fetchedemplyee=i[0]
        self.assertEqual(fetchedemplyee,self.empname1)

    def test_verify_employee_name2(self):
        result=self.connection.execute("select empname from Employee where empcode="+self.empcode2)
        for i in result:
            fetchedemplyee=i[0]
        self.assertEqual(fetchedemplyee,self.empname2)

    def test_verify_employee_name3(self):
        result=self.connection.execute("select empname from Employee where empcode="+self.empcode3)
        for i in result:
            fetchedemplyee=i[0]
        self.assertEqual(fetchedemplyee,self.empname3)


if __name__=="__main__":
    unittest.main()