'''
Write a function, myxml, that allows you to create simple XML output. The output
from the function will always be a string. The function can be invoked in a number of
ways, as shown in table 6.3.
'''

def myxml(tag, content='', **kwargs):
    attributes = ''.join([f' {key}={value}' for key,value  in kwargs.items()])
    return  f'<{tag}{attributes}>{content}</{tag}>'



if  __name__ == '__main__':
    print(myxml('person','John Doe', age=45, gender='male'))