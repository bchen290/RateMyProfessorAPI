from json import JSONDecodeError
from sqlite3 import IntegrityError
from .models import db, Reviews, Professor

import requests
import json
import math


class RateMyProfessorScraper:
    def __init__(self, school_id):
        self.school_id = school_id
        self.professor_list = []

        self.BASE_URL = "http://www.ratemyprofessors.com/filter/professor/?&page={page}&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid={id}"
        self.BASE_PROFESSOR_URL = "https://www.ratemyprofessors.com/paginate/professors/ratings?tid={id}&filter=&courseCode=&page={page}"
        self.RESULT_PER_PAGE = 20

    def get_number_of_professors(self):
        page = requests.get(self.BASE_URL.format(page=1, id=self.school_id))
        page_json = json.loads(page.content)

        # Add 20 because the first page already contains 20 results
        return page_json['remaining'] + self.RESULT_PER_PAGE

    def get_all_professors(self):
        number_of_professors = self.get_number_of_professors()
        number_of_pages = math.ceil(number_of_professors / self.RESULT_PER_PAGE)
        print(number_of_pages)

        for i in range(number_of_pages + 1):
            page = requests.get(self.BASE_URL.format(page=i, id=self.school_id))
            page_json = json.loads(page.content)

            print(i)

            for professor in page_json['professors']:
                try:
                    name = ' '.join((professor['tFname'], professor['tMiddlename'], professor['tLname']))
                    professor_id = professor['tid']

                    professor_detail = self.get_professor_detail(professor_id)
                    professor_class_set = set()

                    for detail in professor_detail:
                        db.session.add(Reviews(rate_my_professor_id=detail[0], professor_id=professor_id, comment=detail[1]))
                        db.session.commit()

                        professor_class_set.add(detail[2])

                    db.session.add(Professor(id=professor_id, name=name, overall_rating=professor['overall_rating'], classes=json.dumps(list(professor_class_set))))
                    db.session.commit()
                except (JSONDecodeError, IntegrityError) as e:
                    continue

    def get_professor_detail(self, professor_id):
        professor_detail_list = []

        number_of_reviews = self.get_number_of_reviews(professor_id)
        number_of_pages = math.ceil(number_of_reviews / self.RESULT_PER_PAGE)

        for i in range(number_of_pages + 1):
            page = requests.get(self.BASE_PROFESSOR_URL.format(page=i, id=professor_id))
            page_json = json.loads(page.content)

            for rating in page_json['ratings']:
                professor_detail_list.append((rating['id'], rating['rComments'], rating['rClass']))

        return professor_detail_list

    def get_number_of_reviews(self, professor_id):
        page = requests.get(self.BASE_PROFESSOR_URL.format(page=1, id=professor_id))
        page_json = json.loads(page.content)
        return page_json['remaining'] + self.RESULT_PER_PAGE
