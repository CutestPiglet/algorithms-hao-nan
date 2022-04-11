# coding: utf-8

"""
https://leetcode.com/problems/course-schedule/
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        n = numCourses

        prerequisite_records = {}
        num_of_prerequisite_courses = [0] * n

        for c, prerequisite_course in prerequisites:
            prerequisite_records.setdefault(prerequisite_course, []).append(c)
            num_of_prerequisite_courses[c] += 1

        available_courses = [i for i in range(n) if num_of_prerequisite_courses[i] == 0]

        while available_courses:
            for course in prerequisite_records.get(available_courses.pop(), []):
                num_of_prerequisite_courses[course] -= 1
                if num_of_prerequisite_courses[course] == 0:
                    available_courses.append(course)

        return not any(num_of_prerequisite_courses)
