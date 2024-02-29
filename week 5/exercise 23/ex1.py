'''
In this exercise, you’re analyzing test data in a high school. There’s a scores directory on the filesystem containing a number of files in JSON format. 
Each file represents the scores for one class. Write a function, print_scores, that takes a directory
name as an argument and prints a summary of the student scores it finds.
'''

import json
import glob

def print_scores(directory):
    files = glob.glob(f'{directory}/*.json')
    for file in files:
        scores = {}
        with open(file) as f:
            data = json.load(f)
            for dic in data:
                for key, val in dic.items():
                    scores[key] = scores.get(key, []) + [val]
        print(file)
        for key, val in scores.items():
            print(f"{key}: \tmin {min(scores[key])}, \tmax {max(scores[key])}, \taverage {sum(scores[key])/len(scores[key])}")


if __name__ == "__main__":
    print_scores('../scores')