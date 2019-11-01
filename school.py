class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}
    
    def add_student(self, studentName, grade):
        if grade in self.roster:
            self.roster[grade].append(studentName)
        else:
            self.roster[grade] = [studentName]
    
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        sorted_dict = self.roster
        for key in sorted_dict:
            sorted_dict[key].sort()
        return sorted_dict
            