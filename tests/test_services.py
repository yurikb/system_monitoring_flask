import unittest

from app import create_app
from app.services import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage, get_virtual_memory_usage

class ServicesTestCase(unittest.TestCase):

  def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client()

  def test_get_cpu_usage(self):
    cpu_usage = get_cpu_usage()
    self.assertIsInstance(cpu_usage, float)
    self.assertGreaterEqual(cpu_usage, 0.0)
    self.assertLessEqual(cpu_usage, 100.0)

  def test_get_memory_usage(self):
    memory_usage = get_memory_usage()
    self.assertIsInstance(memory_usage, float)
    self.assertGreaterEqual(memory_usage, 0.0)
    self.assertLessEqual(memory_usage, 100.0)

  def test_get_disk_usage(self):
    disk_usage = get_disk_usage()
    self.assertIsInstance(disk_usage, float)
    self.assertGreaterEqual(disk_usage, 0.0)
    self.assertLessEqual(disk_usage, 100.0)

  def test_get_network_usage(self):
    network_usage = get_network_usage()
    self.assertIsInstance(network_usage, int)
    self.assertGreaterEqual(network_usage, 0.0)

  def test_get_virtual_memory_usage(self):
    virtual_memory_usage = get_virtual_memory_usage()
    self.assertIsInstance(virtual_memory_usage, float)
    self.assertGreaterEqual(virtual_memory_usage, 0.0)

if __name__ == '__main__':
    unittest.main()