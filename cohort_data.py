"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    # TODO: replace this with your code
    for line in open(filename):
      item = line.split('|')
      if item[2] != '':
        houses.add(item[2])
    

    return houses


def students_by_cohort(filename, cohort="All"):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    for line in open(filename):
      item = line.split('|')
      if item[4] != "G\n" and item[4] != "I\n":
        if cohort == "All":
          students.append(f"{item[0]} {item[1]}")
        elif cohort == item[4].strip():
          students.append(f"{item[0]} {item[1]}")
        else:
          pass
      
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for line in open(filename):
      item = line.split('|')
      if item[2] == "Dumbledore's Army":
        dumbledores_army.append(f"{item[0]} {item[1]}")
      elif item[2] == "Gryffindor":
        gryffindor.append(f"{item[0]} {item[1]}")
      elif item[2] == "Hufflepuff":
        hufflepuff.append(f"{item[0]} {item[1]}")
      elif item[2] == "Ravenclaw":
        ravenclaw.append(f"{item[0]} {item[1]}")
      elif item[2] == "Slytherin":
        slytherin.append(f"{item[0]} {item[1]}")
      elif item[4].strip() == 'G':
        ghosts.append(f"{item[0]} {item[1]}")
      elif item[4].strip() == 'I':
        instructors.append(f"{item[0]} {item[1]}")
 
    return [sorted(dumbledores_army),sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    for line in open(filename):
      items = line.split('|')
      stripped_items = [item.strip() for item in items]
      name = f"{stripped_items[0]} {stripped_items[1]}"
      house = stripped_items[2]
      head_of_house = stripped_items[3]
      cohort = stripped_items[4]
      all_data.append((name, house, head_of_house, cohort))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    for line in open(filename):
      items = line.split('|')
      stripped_items = [item.strip() for item in items]
      name_on_list = f"{stripped_items[0]} {stripped_items[1]}"
      if name == name_on_list:
        return stripped_items[4]


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    super_dupers = set()
    list_of_last_names = list()

    for line in open(filename):
      items = line.split('|')
      stripped_items = [item.strip() for item in items]
      list_of_last_names.append(stripped_items[1])
      
    another_empty_list = list()
    for each_last_name in list_of_last_names:
      if each_last_name not in another_empty_list:
        another_empty_list.append(each_last_name)
      else:
        super_dupers.add(each_last_name)

    return super_dupers


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    housemates = set()
    
    for line in open(filename):
      items = line.split('|')
      stripped_items = [item.strip() for item in items]
      name_on_list = f"{stripped_items[0]} {stripped_items[1]}"
      if name == name_on_list:
        house = stripped_items[2]
        cohort = stripped_items[4]


    for line in open(filename):
      items = line.split('|')
      stripped_items = [item.strip() for item in items]
      for item in stripped_items:
        if stripped_items[4] == cohort and stripped_items[2] == house and f"{stripped_items[0]} {stripped_items[1]}" != name:
          housemates.add(f"{stripped_items[0]} {stripped_items[1]}")

    return housemates
      



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == "__main__":
    import doctest

    result = doctest.testfile(
        "doctests.py",
        report=False,
        optionflags=(doctest.REPORT_ONLY_FIRST_FAILURE),
    )
    doctest.master.summarize(1)
    if result.failed == 0:
        print("ALL TESTS PASSED")
