from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QLineEdit,
                             QRadioButton,
                             QSpinBox,
                             QComboBox,
                             QPushButton,
                             QFormLayout
                             )

class Survey(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Survey")
        self.setStyleSheet("font-size: 20px")
        
        self.init_ui()

    def init_ui(self):

        self.Name_input = QLineEdit(self)
        self.Name_input.setStyleSheet("font-size: 25px")
        self.Surname_input = QLineEdit(self)
        self.Surname_input.setStyleSheet("font-size: 25px")
        self.Phone_number_input = QLineEdit(self)
        self.Phone_number_input.setStyleSheet("font-size: 25px")
        self.Fakultet_input = QLineEdit(self)
        self.Fakultet_input.setStyleSheet("font-size: 25px")

        self.gender_radio_Male = QRadioButton('Male', self)
        self.gender_radio_Woman = QRadioButton('Woman', self)

        self.Age_spinbox = QSpinBox(self)
        self.Age_spinbox.setMinimum(0)  
        self.Age_spinbox.setMaximum(60) 

        self.Course_combobox = QComboBox(self)
        self.Course_combobox.addItems(["1","2","3","4"])
        self.Address_combobox = QComboBox(self)
        self.Address_combobox.addItems(["Toshkent",
                                        "Sirdaryo", 
                                        "Navoiy", 
                                        "Jizzax", 
                                        "Xorazm", 
                                        "Buxoro", 
                                        "Surxondaryo", 
                                        "Namangan", 
                                        "Andijon", 
                                        "Qashqadaryo", 
                                        "Samarqand", 
                                        "Farg`ona",  
                                        "Qoraqalpog`iston Respublikasi"])

        self.Write_data_to_a_file_btn = QPushButton('Write data to a file', self)
        self.Write_data_to_a_file_btn.clicked.connect(self.Write_data_to_a_file)
        hbox = QHBoxLayout()
        hbox.addWidget(self.gender_radio_Male)
        hbox.addWidget(self.gender_radio_Woman)
        layout = QFormLayout()
        layout.addRow('Name:', self.Name_input)
        layout.addRow('Surname:', self.Surname_input)
        layout.addRow('Age:', self.Age_spinbox)
        layout.addRow('gender:', hbox)
        layout.addRow('Address:', self.Address_combobox)
        layout.addRow('Phone number:', self.Phone_number_input)
        layout.addRow('Faculty:', self.Fakultet_input)
        layout.addRow('Course:', self.Course_combobox)
        layout.addRow('', self.Write_data_to_a_file_btn)
        self.Write_data_to_a_file_btn.setStyleSheet("font-size: 25px")


        self.setLayout(layout)

    def Write_data_to_a_file(self):
        Name = self.Name_input.text()
        Surname = self.Surname_input.text()
        Phone_number = self.Phone_number_input.text()  # Fix here
        Faculty = self.Fakultet_input.text()
        gender = 'Male' if self.gender_radio_Male.isChecked() else 'Woman'
        Age = self.Age_spinbox.value()
        Address = self.Address_combobox.currentText()
        Course = self.Course_combobox.currentText()
        fayl_nomi = f"{Surname}.txt"
        with open(fayl_nomi, 'w') as file:
            file.write(f'Name: {Name}\nSurname: {Surname}\nAge: {Age}\ngender: {gender}\nAddress: {Address}\nPhone number: {Phone_number}\nFaculty: {Faculty}\nCourse: {Course}')

        self.close()

app = QApplication([])
# app.setStyleSheet("font-size: 30px")
Surv = Survey()
Surv.show()
app.exec_()
