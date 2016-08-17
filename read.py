from __future__ import print_function

import os
import pickle


def read():
    for ls in os.listdir('data'):
        if ls.endswith('.pkl'):
            f = open('data/' + ls, 'rb')
            data = pickle.load(f)
            for datum in data:
                print('ts = {}, t = {}, h= {}'.format(datum['ts'], datum['title'], datum['href']))
            f.close()


if __name__ == '__main__':
    read()
