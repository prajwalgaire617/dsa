import unittest
from src.Insertion_sort import insertion_sort
from random_array import generate_random_array
import matplotlib.pyplot as plt
import numpy


class TestSum(unittest.TestCase):
    def test_sum(self):
        length=[]
        time=[]
        for i in range(5):
         input_data=generate_random_array(min_length=1000,max_length=10000,min_value=0,max_value=100)
         result =insertion_sort(input_data)
         input_data.sort()
         self.assertEqual(result[0],input_data)
         length.append(len(input_data))
         time.append(result[1])
        plt.xlabel('length of array')
        plt.ylabel('time (ms)')
        plt.plot(numpy.array(length), numpy.array(time),'o')
        plt.grid(True)
        plt.show()
if __name__=="__main__":
    unittest.main()