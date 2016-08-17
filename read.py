from __future__ import print_function

import pickle


def read():
    import os
    c = 0
    for ls in os.listdir('data'):
        if ls.endswith('.pkl'):
            f = open('data/' + ls, 'rb')
            data = pickle.load(f)
            for datum in data:
                print('ts = {}, t = {}, h= {}'.format(datum['ts'], datum['title'], datum['href']))
            print(c)
            f.close()
    print(c)


if __name__ == '__main__':
    read()
