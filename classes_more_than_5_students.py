import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counts = courses.groupby(['class']).size().reset_index(name='count')
    return counts[counts['count'] >= 5][['class']]
