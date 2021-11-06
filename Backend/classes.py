class PatientProfile:
    """Класс для работы с профилем пациента"""
    def __init__(self, fullName, passport, anamnesis):
        self._fullName = fullName
        self._passport = passport
        self._anamnesis = anamnesis

    @property
    def fullName(self):
        return self._fullName
    @property
    def passport(self):
        return self._passport
    @property
    def anamnesis(self):
        return self._anamnesis

    @fullName.setter
    def fullName(self, value):
        self._fullName = value
    @passport.setter
    def passport(self, value):
        self._passport = value
    @anamnesis.setter
    def anamnesis(self, value):
        self._anamnesis = value
    
    def __str__(self):
        return "Профиль пациента " + {self.fullName} + ", паспорт № " + {self.passport}


class DoctorProfile:
    """Класс для работы с профилем врача"""
    def __init__(self, fullName, qualification, profiling):
        self._fullName = fullName
        self._qualification = qualification
        self._profiling = profiling

    @property
    def fullName(self):
        return self._fullName
    @property
    def qualification(self):
        return self._qualification
    @property
    def profiling(self):
        return self._profiling

    @fullName.setter
    def fullName(self, value):
        self._fullName = value
    @qualification.setter
    def qualification(self, value):
        self._qualification = value
    @profiling.setter
    def profiling(self, value):
        self._profiling = value

    def __str__(self) -> str:
        return "Врач-" + {self.profiling} + " " + {self.fullName} + ". Квалификация: " + {self.qualification}


class Diagnosis:
    """Класс диагнозов"""
    def __init__(self, infAboutDiagnos):
        self._infAboutDiagnos = infAboutDiagnos

    @property
    def infAboutDiagnos(self):
        return self._infAboutDiagnos

    @infAboutDiagnos.setter
    def infAboutDiagnos(self, value):
        self._infAboutDiagnos = value

    def __str__(self) -> str:
        return "Диагноз: " + {self.infAboutDiagnos}


class Recipe:
    """Класс рецептов"""
    def __init__(self, infAboutRecipe):
        self._infAboutRecipe = infAboutRecipe

    @property
    def infAboutRecipe(self):
        return self._infAboutRecipe

    @infAboutRecipe.setter
    def infAboutRecipe(self, value):
        self._infAboutRecipe = value

    def __str__(self) -> str:
        return "Рецепт: " + {self.infAboutRecipe}


class Note(Diagnosis, Recipe):
    """Класс для работы записями на приём"""
    def __init__(self, date, information):
        self._date = date
        self._information = information

    @property
    def date(self):
        return self._date
    @property
    def information(self):
        return self._information

    @date.setter
    def date(self, value):
        self._date = value
    @information.setter
    def information(self, value):
        self._information = value

    def __str__(self) -> str:
        return "Прием назначен на " + {self.date} + "Инф. о приёме: " + {self.information}


class User:
    """Класс для работы с пользователем (пациент или врач)"""
    notes = []

    def __init__(self, Profile):
        self._profile = Profile # записываем объект класса как атрибут
        
    @property
    def profile(self):
        return self._profile
    
    @profile.setter
    def profile(self, value):
        self._profile = value

    def addNote(self, other, Note):
        other.notes.append(Note)
        self.notes.append(Note)