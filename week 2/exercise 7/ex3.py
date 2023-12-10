'''
Remove author names—In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.
'''

def replacer(article, names = []):
    for name in names:
        article = article.replace(name, '_')

    return article




if __name__ == "__main__":
    article = "The authors of this paper are John Doe and Jane Smith. They argue that being short migh lead to self esteem issues and noticed a spike in depression in male subjects below 6 feet."
    names = ["John Doe", "Jane Smith"]
    print(replacer(article, names))