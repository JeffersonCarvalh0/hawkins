# Some utility functions

from hawkins.settings import LANGUAGES

def documentPath(instance, filename):
    '''
        Function used to save student's documents in a path with his or her
        registry.
    '''
    return '%s/%s' %(instance.student.registry, filename)

def getLanguageChoices():
    '''
        Returns a list of tuples conatining the choices for the application's
        language, based on what is defined in the LANGUAGES tuple in settings.py
        file.
    '''
    choices_size = len(LANGUAGES)
    choices = [''] * choices_size

    for i in range(choices_size):
        choices[i] = (LANGUAGES[1], LANGUAGES[0])

    return choices

def breadcrumbUpdate(breadcrumb, new_value):
    for i in range(len(breadcrumb)):
        if breadcrumb[i]['name'] == new_value['name']:
            breadcrumb = breadcrumb[:i + 1]
            return breadcrumb
    breadcrumb.append(new_value)
    return breadcrumb
