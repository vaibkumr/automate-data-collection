import sys
import os
import re
import numpy as np
import pandas as pd
from subprocess import PIPE, run
import time

COLUMNS = [
        '.interp', '.note.ABI-tag', '.note.gnu.build-i', '.gnu.hash' ,
        '.dynsym','.dynstr','.rela.dyn','.rela.plt','.init','.plt','.text',
        '.fini', '.rodata', '.eh_frame_hdr', '.eh_frame', '.init_array',
        '.fini_array', '.dynamic', '.got', '.got.plt', '.data', '.bss',
        '.comment', '.symtab', '.strtab', '.shstrtab', 'filesize', 'time'
        ]


class Automate:
    def __init__(self, file_name, MAXSIZE, type = 'm'):
        self.type = type
        self.file_name = file_name
        self.MAXSIZE = MAXSIZE
        self.size = 0
        self.data = []

    def collect_data(self):
        for size in range(1,self.MAXSIZE):
            self.size = size
            self.edit_source()
            self.compile()
            self.data.append(self.get_signature())
        df = pd.DataFrame(self.data, columns = COLUMNS)
        self.save_df(df)

    def save_df(self, df):
        print("SAVING TO DATAFRAME")
        try:
            df_old = pd.read_csv('DATA.csv')
            result = pd.concat([df_old, df])
            result.to_csv('DATA.csv', index=False)
        except:
            df.to_csv('DATA.csv', index=False)

    def get_size(self):
        return os.path.getsize(self.source_out_file)

    def save_source_file(self, data):
        self.source_cpp_file = self.file_name[:-4] + "_" + str(self.size) \
                                                         + '.cpp'
        with open(self.source_cpp_file, 'w' ) as handle:
                    handle.write(data)

    def edit_source(self):
        with open(self.file_name) as handle:
            cpp_code = handle.read()
            if(self.type == 'm'):
                matrix_1, matrix_2, result_matrix = self.random_generate_data()
                edited_cpp = cpp_code.replace(
                                            "SIZE", str(self.size)
                                            ).replace(
                                            "ARRAY_1",matrix_1
                                            ).replace(
                                            "ARRAY_2",matrix_2
                                            ).replace(
                                            "RESULT",result_matrix
                                            )
            if(self.type == 'q'):
                matrix = self.random_generate_data()
                edited_cpp = cpp_code.replace(
                                            "SIZE", str(self.size)
                                            ).replace(
                                            "ARRAY_1",matrix
                                            )
            if(self.type == 'f'):
                edited_cpp = cpp_code.replace(
                                            "SIZE", str(self.size)
                                            )
            self.save_source_file(edited_cpp)

    def mstring_modification(self, matrix):
        return np.array2string(matrix, threshold=10000000,
                                    separator=',',
                                    ).replace(
                                            ']','}'
                                            ).replace(
                                            '[','{'
                                            ).replace(
                                            '\n',''
                                            ).replace(
                                            ' ',''
                                            )

    def random_generate_data(self):
        np.random.seed(self.size)
        if(self.type == 'm'):
            matrix_1 = np.random.randint(0, 100, size=(self.size, self.size))
            matrix_2 = np.random.randint(0, 100, size=(self.size, self.size))
            result_matrix = np.zeros((self.size, self.size), dtype=int)
            matrix_1 = self.mstring_modification(matrix_1)
            matrix_2 = self.mstring_modification(matrix_2)
            result_matrix = self.mstring_modification(result_matrix)
            return matrix_1, matrix_2, result_matrix
        if(self.type == 'q'):
            matrix = np.random.randint(0, self.size, size=self.size)
            matrix = self.mstring_modification(matrix)
            return matrix


    def compile(self):
        self.source_out_file = self.source_cpp_file[:-4]+'.o'
        print("compiling: ", self.source_cpp_file, "to", self.source_out_file)
        command = "g++ " + self.source_cpp_file + " -o " + self.source_out_file
        output = run(command, stdout=PIPE, stderr=PIPE,
                    universal_newlines=True,
                    shell=True
                    )
        if(output.stderr):
            print(f'{output.stderr} error in file {self.source_cpp_file}')
            input()
        return True

    def get_time(self):
        print("running: ", self.source_out_file)
        command = "./" + self.source_out_file
        start = time.time()
        output = run(command, stdout=PIPE, stderr=PIPE,
                    universal_newlines=True,
                    shell=True
                    )
        end = time.time()
        return end-start

    def extract_it(self, line):
        for word in line.split(' '):
            if len(word) == 16 :
                return word

    def get_signature(self):
        command = 'readelf -S '+ self.source_out_file
        output = run(command, stdout=PIPE, stderr=PIPE,
                    universal_newlines=True,
                    shell=True
                    ).stdout
        output = str(output).split('\n')
        signature = []
        for i, x in enumerate(output):
            for c in COLUMNS[:-1]:
                if c in x.split(' '):
                    signature.append(self.extract_it(output[i+1]))
        signature.append(self.get_size())
        signature.append(self.get_time())
        return signature




if __name__ == "__main__":
    a = Automate('quick_sort/quick_sort.cpp',1000, type = 'q')
    a.collect_data()
    a = Automate('matrix_mult/matrix_mult.cpp',500, type = 'm')
    a.collect_data()
    a = Automate('fib/fib.cpp',45, type = 'f')
    a.collect_data()
