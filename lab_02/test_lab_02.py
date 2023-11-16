import pytest
import lab_02
import csv
from io import StringIO

@pytest.fixture
def TestingData():
	return [
		{"name": "Bob", "phone": "1112233", "age": "20", "email": "bob@example.com"},
		{"name": "Dilan", "phone": "2223344", "age": "21", "email": "Dilan@example.com"},
		{"name": "Zak", "phone": "3334455", "age": "23", "email": "zak@example.com"}
	]

def test_FileLoad(TestingData, tmp_path):
	PathFile = tmp_path / "lab2.csv"
	with open(PathFile, "w", newline="", encoding="utf-8") as file:
		ResFile = csv.DictWriter(file, fieldnames=["name", "phone", "age", "email"])
		ResFile.writeheader()
		ResFile.writerows(TestingData)

	LData = lab_02.FileLoad(PathFile)
	assert LData == TestingData

def test_SaveFile(TestingData, tmp_path):
	PathFile = tmp_path / "test_save_file.csv"
	lab_02.SaveFile(PathFile, TestingData)

	LData = lab_02.FileLoad(PathFile)
	assert LData == TestingData

def test_addNewElement(tmp_path):
	lab_02.list = []
	lab_02.AFile = None

	TestInputAns = iter(["Test", "123", "25", "test@example.com"])

	def TestInput(prompt):
		return next(TestInputAns)

	lab_02.input = TestInput
	lab_02.addNewElement()

	assert len(lab_02.list) == 1
	assert lab_02.list[0] == {"name": "Test", "phone": "123", "age": 25, "email": "test@example.com"}

def test_deleteElement(capsys):
	lab_02.list = [{"name": "John", "phone": "123", "age": 25, "email": "john@example.com"}]
	TestInputAns = iter(["John"])

	def TestInput(prompt):
		return next(TestInputAns)

	lab_02.input = TestInput
	lab_02.deleteElement()
	captured = capsys.readouterr()
	assert "Del position" in captured.out

def test_updateElement(tmp_path, capsys):
	lab_02.list = [{"name": "John", "phone": "123", "age": "25", "email": "john@example.com"}]
	TestInputAns = iter(["John", "Jane", "123", "30", "john@example.com"])

	def TestInput(prompt):
		return next(TestInputAns)

	lab_02.input = TestInput
	lab_02.updateElement()
	captured = capsys.readouterr()
	assert "Element has been updated" in captured.out
	assert lab_02.list[0] == {"name": "Jane", "phone": "123", "age": 30, "email": "john@example.com"}

def test_printAllList(capsys):
	lab_02.list = [{"name": "John", "phone": "123", "age": 25, "email": "john@example.com"}]
	lab_02.printAllList()
	captured = capsys.readouterr()
	assert "Student name is John, Phone is 123, Age is 25, Email is john@example.com" in captured.out
