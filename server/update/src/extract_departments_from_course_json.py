#!/usr/bin/env python3

from collections import defaultdict
import json
import sys

from utils import *


departments = {}
subject_areas = {}
department_courses = defaultdict(list)
subject_area_courses = defaultdict(list)


def store_course_info(course):
    departments[course['departmentCode']] = course['departmentDescription']
    department_courses[course['departmentCode']].append(course)
    subject_areas[course['subjectAreaCode']] = course['subjectAreaDescription']
    subject_area_courses[course['subjectAreaCode']].append(course)


def run_for_range(start, end):
    for course_number in range(start, end):
        try:
            print('extracting course_number {}'.format(course_number))
            with open(extracted_courses(course_number), 'r') as f:
                for c in json.load(f):
                    store_course_info(c)
        except IOError as e:
            print(e)

    # Save out departments and subject-areas
    with open(departments(), 'w') as f:
        json.dump({
            'subjectAreas': subject_areas,
            'departments': departments
        }, f, indent=4)

    # Save out courses
    for department, courses in department_courses.items():
        with open(course_listing_by_department(department), 'w') as f:
            json.dump(courses, f, indent=4)
    for subject_area, courses in subject_area_courses.items():
        with open(course_listing_by_subject_area(subject_area), 'w') as f:
            json.dump(courses, f, indent=4)

    return 0


if __name__ == '__main__':
    sys.exit(run_for_range(1, 400))
