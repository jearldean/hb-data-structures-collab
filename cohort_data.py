"""Functions to parse a file containing student data."""

def process_the_data_pack(filename):
  """Return nice parsed data in the given file.

  Arguments:
      - filename (str): the path to a data file

    Return:
      - data_pack[list]: a list of lists where
          data_pack[wizard_index][0] = first_name
          data_pack[wizard_index][1] = last_name
          data_pack[wizard_index][2] = house
          data_pack[wizard_index][3] = head_of_house
          data_pack[wizard_index][4] = cohort
          data_pack[wizard_index][5] = name
  """

  wizard_school_data_pack = []

  for line in open(filename):
    line_pieces = line.split('|')

    try:
      # Strip the trailing carriage return
      stripped_data = [wizard_data.strip() for wizard_data in line_pieces]
      # Add the name
      stripped_data.append(f"{stripped_data[0]} {stripped_data[1]}")
      wizard_school_data_pack.append(stripped_data)
    except TypeError:
      # There's an extra line at the end of the file causing an empty list
      continue

  return wizard_school_data_pack


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - houses[str]: a set of strings
    """

    houses = set()

    for each_wizard in process_the_data_pack(filename):
      this_wizards_house = each_wizard[2]
      if this_wizards_house:  # Ghosts have no house in the data pack.
        houses.add(this_wizards_house)

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
      - students[list]: a list of lists
    """

    students = []

    for each_wizard in process_the_data_pack(filename):
      this_wizards_cohort = each_wizard[4]
      if len(this_wizards_cohort) > 2:
        if cohort == "All":
          students.append(each_wizard[5])
        if this_wizards_cohort == cohort:
          students.append(each_wizard[5])

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
      - names_by_house[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for each_wizard in process_the_data_pack(filename):
      this_wizards_house = each_wizard[2]
      this_wizards_name = each_wizard[5]
      non_student_role = each_wizard[4]
      if this_wizards_house == "Dumbledore's Army":
        dumbledores_army.append(this_wizards_name)
      elif this_wizards_house == "Gryffindor":
        gryffindor.append(this_wizards_name)
      elif this_wizards_house == "Hufflepuff":
        hufflepuff.append(this_wizards_name)
      elif this_wizards_house == "Ravenclaw":
        ravenclaw.append(this_wizards_name)
      elif this_wizards_house == "Slytherin":
        slytherin.append(this_wizards_name)
      elif non_student_role == "G":
        ghosts.append(this_wizards_name)
      elif non_student_role == "I":
        instructors.append(this_wizards_name)
      else:
        continue

    names_by_house = (
      [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), 
      sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)])
    return names_by_house


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
      - all_wizarding_data[tuple]: a list of tuples
    """

    all_wizarding_data = []

    for each_wizard in process_the_data_pack(filename):
      this_wizards_name = each_wizard[5]
      this_wizards_house = each_wizard[2]
      this_wizards_head_of_house = each_wizard[3]
      this_wizards_cohort = each_wizard[4]
      all_wizarding_data.append(
        (this_wizards_name, this_wizards_house, this_wizards_head_of_house, 
        this_wizards_cohort))

    return all_wizarding_data


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

    for each_wizard in process_the_data_pack(filename):
      this_wizards_name = each_wizard[5]
      this_wizards_cohort = each_wizard[4]
      if name == this_wizards_name:
        return this_wizards_cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - wizards_with_siblings{str}: a set of strings
    """

    wizards_with_siblings = set()
    all_wizarding_last_names = list()

    for each_wizard in process_the_data_pack(filename):
      this_wizards_last_name = each_wizard[1]
      all_wizarding_last_names.append(this_wizards_last_name)

    a_list_for_checking_dupes = list()
    for each_wizarding_last_name in all_wizarding_last_names:
      if each_wizarding_last_name not in a_list_for_checking_dupes:
        a_list_for_checking_dupes.append(each_wizarding_last_name)
      else:
        wizards_with_siblings.add(each_wizarding_last_name)

    return wizards_with_siblings


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - housemates{str}: a set of strings
    """

    housemates = set()

    inquiry_wizards_house = ""
    inquiry_wizards_cohort = ""
    for each_wizard in process_the_data_pack(filename):
      this_wizards_name = each_wizard[5]
      if this_wizards_name == name:
        inquiry_wizards_house = each_wizard[2]
        inquiry_wizards_cohort = each_wizard[4]


    for each_wizard in process_the_data_pack(filename):
      this_wizards_cohort = each_wizard[4]
      this_wizards_house = each_wizard[2]
      this_wizards_name = each_wizard[5]
      if this_wizards_cohort == inquiry_wizards_cohort and (
        this_wizards_house == inquiry_wizards_house) and (
          this_wizards_name != name):
        housemates.add(this_wizards_name)

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
        print("EXPECTO PATRONUM!")
