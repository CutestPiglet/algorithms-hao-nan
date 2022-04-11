# coding: utf-8

import unittest

from problems.course_schedule import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'numCourses': 2, 'prerequisites': [[1, 0]]},
            {'numCourses': 2, 'prerequisites': [[1, 0], [0, 1]]},
            {'numCourses': 20, 'prerequisites': [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]},
            {'numCourses': 3, 'prerequisites': [[1, 0], [0, 2], [2, 1]]},
        ]
        expected_output = [
            True,
            False,
            False,
            False,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.canFinish(data['numCourses'], data['prerequisites']), output)


if __name__ == '__main__':
    unittest.main()
