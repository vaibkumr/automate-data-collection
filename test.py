import sys
import os
import re
import numpy as np
from subprocess import PIPE, run
import time
import pandas as pd

df = pd.read_csv('DATA.csv')
print(df['.text'])
