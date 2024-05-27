import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QListWidget, QTextEdit

class ResumeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Резюме")
        self.setGeometry(0, 0, 1728, 750)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        resume_label = QLabel("<h2>РЕЗЮМЕ</h2>")
        layout.addWidget(resume_label)

        self.add_personal_info(layout)
        self.add_experience(layout)
        self.add_education(layout)
        self.add_skills(layout)
        self.add_additional_info(layout)

    def add_personal_info(self, layout):
        personal_info_label = QLabel("<h3>Личная информация:</h3>")
        layout.addWidget(personal_info_label)

        personal_info_text = QTextEdit()
        personal_info_text.setReadOnly(True)
        personal_info_text.setHtml(
            "<b>ФИО:</b> Борис Иванов<br>"
            "<b>Электронная почта:</b> borisivanov@example.com<br>"
            "<b>Телефон:</b> +7 (777) 777-77-77"
        )
        layout.addWidget(personal_info_text)

    def add_experience(self, layout):
        experience_label = QLabel("<h3>Опыт работы:</h3>")
        layout.addWidget(experience_label)

        experience_list = QListWidget()
        experience_list.addItems([
            "Место работы: Художественная галерея 'АртМир'\n"
            "Должность: Художник-иллюстратор\n"
            "Срок: Август 2018 - настоящее время\n"
            "- Создание иллюстраций для книг и журналов\n"
            "- Оформление выставок и мероприятий\n"
            "- Разработка дизайна промо-материалов",

            "Место работы: Рекламное агентство 'Креатив'\n"
            "Должность: Графический дизайнер\n"
            "Срок: Июнь 2015 - Июль 2018\n"
            "- Разработка рекламных баннеров и логотипов\n"
            "- Создание макетов для печати и цифровых рекламных материалов\n"
            "- Участие в концептуальных проектах"
        ])
        layout.addWidget(experience_list)

    def add_education(self, layout):
        education_label = QLabel("<h3>Образование:</h3>")
        layout.addWidget(education_label)

        education_text = QTextEdit()
        education_text.setReadOnly(True)
        education_text.setPlainText(
            "Учебное заведение: Институт искусств и дизайна\n"
            "Специальность: Графический дизайн\n"
            "Годы обучения: 2011 - 2015\n\n"
            "Школа искусств имени А. С. Пушкина\n"
            "Специализация: Живопись и рисунок\n"
            "Годы обучения: 2007 - 2011"
        )
        layout.addWidget(education_text)

    def add_skills(self, layout):
        skills_label = QLabel("<h3>Профессиональные навыки:</h3>")
        layout.addWidget(skills_label)

        skills_text = QTextEdit()
        skills_text.setReadOnly(True)
        skills_text.setPlainText(
            "- Владение программами Adobe Photoshop, Adobe Illustrator, CorelDRAW\n"
            "- Опыт работы с графическими планшетами Wacom\n"
            "- Знание основ композиции и цветоведения\n"
            "- Умение работать в команде и соблюдать дедлайны\n"
            "- Опыт создания иллюстраций различных стилей и направлений"
        )
        layout.addWidget(skills_text)

    def add_additional_info(self, layout):
        additional_info_label = QLabel("<h3>Дополнительно:</h3>")
        layout.addWidget(additional_info_label)

        additional_info_text = QTextEdit()
        additional_info_text.setReadOnly(True)
        additional_info_text.setPlainText(
            "В свободное время занимаюсь созданием собственных проектов в области искусства, "
            "участвую в выставках и арт-мероприятиях. Люблю экспериментировать с разными техниками "
            "и материалами, стремлюсь к постоянному развитию в области художественного творчества."
        )
        layout.addWidget(additional_info_text)

def main():
    app = QApplication(sys.argv)
    window = ResumeApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
