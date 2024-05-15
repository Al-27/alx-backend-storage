#!/usr/bin/env python3
""" Module Documentation """


def top_students(mongo_collection):
    """
    func
    """
    students = [std for std in mongo_collection.find({})]
    
    for student in students:
        name = student.name
        tot_score = 0
        for topic in student.topics:
            tot_score += topic.scor
        student.update({"averageScore": tot_score/len(student.topics)})
    
    return students
    