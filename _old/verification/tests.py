"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ([1, 2, 3, 4], 2),
            "answer": 9,
        },
        {
            "input": ([1, 3, 10, 100], 3),
            "answer": 1000000,
        },
        {
            "input": ([0, 1], 0),
            "answer": 1,
        },
        {
            "input": ([1, 2], 3),
            "answer": -1,
        },
    ],
    "Extra": [
        {
            "input": ([0], 0),
            "answer": 1,
        },
        {
            "input": ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9),
            "answer": 1,
        },
        {
            "input": ([1, 1, 1, 1, 1, 1, 1, 1, 1, 100], 9),
            "answer": 1000000000000000000,
        },
        {
            "input": ([29, 82, 45, 10], 3),
            "answer": 1000,
        },
        {
            "input": ([6, 31], 3),
            "answer": -1,
        },
        {
            "input": ([75, 68, 35, 61, 9, 36, 89, 0, 30], 10),
            "answer": -1,
        },
        {
            "input": ([29, 44, 50, 92, 56, 86], 2),
            "answer": 2500,
        },

        {
            "input": ([86, 41, 89, 53, 16, 15, 31, 63, 40], 6),
            "answer": 887503681,
        },
        {
            "input": ([73, 26, 11, 3, 74, 94, 10, 10, 81, 63], 4),
            "answer": 29986576,
        },
        {
            "input": ([96, 92, 94], 3),
            "answer": -1,
        },
        {
            "input": ([42, 69, 86, 55, 30, 35, 28, 84, 61, 40], 17),
            "answer": -1,
        },

        {
            "input": ([7, 36, 82, 38, 50, 47, 62, 44], 6),
            "answer": 56800235584,
        },
        {
            "input": ([68, 81, 3, 10, 96, 67, 55, 83, 63, 11], 9),
            "answer": 2357947691,
        },
        {
            "input": ([47, 77, 80, 48, 40, 21, 65], 1),
            "answer": 77,
        },
        {
            "input": ([28, 30, 48, 89, 31, 66], 4),
            "answer": 923521,
        },
        {
            "input": ([71, 53, 51, 75, 16, 33, 88, 5], 3),
            "answer": 421875,
        },
        {
            "input": ([74, 40, 3, 90, 17, 62, 14], 0),
            "answer": 1,
        },
        {
            "input": ([23, 61, 56, 93], 0),
            "answer": 1,
        },
        {
            "input": ([31, 53, 11, 79, 3, 95, 40, 2], 4),
            "answer": 81,
        },
        {
            "input": ([43, 61, 8, 12, 31, 10, 34, 52], 5),
            "answer": 100000,
        },
        {
            "input": ([32, 25, 93, 1], 2),
            "answer": 8649,
        },
        {
            "input": ([2, 56, 73, 54, 88], 4),
            "answer": 59969536,
        },
        {
            "input": ([65, 18, 93, 94, 36, 21, 65, 95, 30, 43], 6),
            "answer": 75418890625,
        },
        {
            "input": ([79, 70, 88, 19, 12, 92, 27, 52, 48], 5),
            "answer": 6590815232,
        },
        {
            "input": ([72, 3, 8, 25, 15, 16], 1),
            "answer": 3,
        },
    ]
}
