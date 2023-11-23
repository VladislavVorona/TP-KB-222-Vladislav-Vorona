import pytest
from pathlib import Path
from io import StringIO
from unittest.mock import patch
from lab_03 import main
from FileHandler import FileHandler
from StudentList import StudentList
from Student import Student
import csv

@pytest.fixture
def TestingData():
	return [
		{"name": "Bob", "phone": "1112233", "age": "20", "email": "bob@example.com"},
		{"name": "Dilan", "phone": "2223344", "age": "21", "email": "Dilan@example.com"},
		{"name": "Zak", "phone": "3334455", "age": "23", "email": "zak@example.com"}
	]

def test_FileLoad(TestingData, tmp_path):
	PathFile = tmp_path / "lab3.csv"
	with open(PathFile, "w", newline="", encoding="utf-8") as file:
		ResFile = csv.DictWriter(file, fieldnames=["name", "phone", "age", "email"])
		ResFile.writeheader()
		ResFile.writerows(TestingData)

	LData = FileHandler.LoadFile(str(PathFile), StudentList())
	assert [vars(student) for student in LData.students] == TestingData

def test_SaveFile(TestingData, tmp_path, capsys):
	PathFile = tmp_path / "test_save_file.csv"
	StudentL = StudentList()
	StudentL.students = [Student(**data) for data in TestingData]

	FileHandler.SaveFile(str(PathFile), StudentL)

	captured = capsys.readouterr()
	assert "The data is saved in" in captured.out

	LData = FileHandler.LoadFile(str(PathFile), StudentList())
	assert [vars(student) for student in LData.students] == [vars(student) for student in StudentL.students]

def test_updateElement(tmp_path, capsys, TestingData):
	with patch('builtins.input', side_effect=["John", "123", "30", "john@example.com"]):
		StudentL = StudentList()
		StudentL.students = [Student(**TestingData[0])]

		with patch('sys.stdout', new_callable=StringIO) as TestInputAns:
			StudentL.updateElement("Bob")

		captured = TestInputAns.getvalue()
		assert "Element has been updated" in captured
		assert vars(StudentL.students[0]) == {"name": "John", "phone": "123", "age": 30, "email": "john@example.com"}
		assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students


def test_addNewElement(tmp_path, TestingData):
	StudentL = StudentList()

	with patch('builtins.input', side_effect=["Test", "123", "25", "test@example.com"]):
		StudentL.addNewElement()

	assert len(StudentL.students) == 1
	assert vars(StudentL.students[0]) == {"name": "Test", "phone": "123", "age": 25, "email": "test@example.com"}
	assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students

	with patch('builtins.input', side_effect=["AAA", "456", "30", "aaa@example.com"]):
		StudentL.addNewElement()

	assert len(StudentL.students) == 2
	assert vars(StudentL.students[0]) == {"name": "AAA", "phone": "456", "age": 30, "email": "aaa@example.com"}
	assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students

	with patch('builtins.input', side_effect=["YYY", "789", "35", "yyy@example.com"]):
		StudentL.addNewElement()

	assert len(StudentL.students) == 3
	assert vars(StudentL.students[2]) == {"name": "YYY", "phone": "789", "age": 35, "email": "yyy@example.com"}
	assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students


def test_deleteElement(capsys, TestingData):
	with patch('builtins.input', return_value="John"):
		StudentL = StudentList()
		StudentL.students = [Student(**TestingData[0])]

		with patch('sys.stdout', new_callable=StringIO) as TestInputAns:
			StudentL.deleteElement("John")

		captured = TestInputAns.getvalue()
		assert "Student not found" in captured

def test_printAllList(capsys, TestingData):
	StudentL = StudentList()
	StudentL.students = [Student(**TestingData[0])]

	with patch('sys.stdout', new_callable=StringIO) as TestInputAns:
		StudentL.printAllList()

	captured = TestInputAns.getvalue()
	assert "Student name is Bob, Phone is 1112233, Age is 20, Email is bob@example.com" in captured
