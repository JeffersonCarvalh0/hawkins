# Some utility functions

from hawkins.settings import LANGUAGES

def documentPath(instance, filename):
    '''
        Function used to save student's documents in a path with his or her
        registry.
    '''
    return '%s/%s' %(instance.registry, filename)

def getLanguageChoices():
    '''
        Returns a list of tuples conatining the choices for the application's
        language, based on what is defined in the LANGUAGES tuple in settings.py
        file.
    '''
    choices_size = len(LANGUAGES)
    choices = [''] * choices_size

    for i in range(choices_size):
        choices[i] = (LANGUAGES[i][0], LANGUAGES[i][1])

    return choices

def partial_average(grade_queryset):
    '''
        Calculates the partial average from a queryset of grades.
    '''
    partial_avg = 0.00
    grade_counter = 0

    for grade in grade_queryset:
        if grade.value is not None:
            partial_avg += grade.value
            grade_counter += 1

    return 0 if grade_counter == 0 else partial_avg / grade_counter

def total_average(grade_queryset):
    '''
        Calculates the total average from a queryset of grades.
    '''
    total_avg = 0.00
    grade_counter = 0

    for grade in grade_queryset:
        if (not grade.retake) or grade.value is not None:
            total_avg += 0 if grade.value is None else grade.value
            grade_counter += 1

    return 0 if grade_counter == 0 else total_avg / grade_counter
