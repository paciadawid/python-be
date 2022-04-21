import itertools
import unittest
from unittest import TestCase

from hamcrest import *
import requests

# print("|".join(map(str,range(1,6))))

#print("|".join([str(i) for i in range(1,6)))

class TestMonolithic(TestCase):
  def step1(self):
      print("step1")

  def step2(self):
      print("step2")

  def _steps(self):
    for name in dir(self): # dir() result is implicitly sorted
      if name.startswith("step"):
        yield name, getattr(self, name)

  def test_steps(self):
    for name, step in self._steps():
      try:
        step()
      except Exception as e:
        self.fail("{} failed ({}: {})".format(step, type(e), e))


