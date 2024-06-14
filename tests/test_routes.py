
import unittest

from app import create_app

class RoutesTestCase(unittest.TestCase):

  def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client()
  
  def test_home(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

  def test_get_monitor_data(self):
    response = self.client.get('/monitor')
    self.assertEqual(response.status_code, 200)
    data = response.get_json()
    self.assertIn('cpuUsage', data)
    self.assertIn('memoryUsage', data)
    self.assertIn('diskUsage', data)
    self.assertIn('networkUsage', data)
    self.assertIn('virtualMemoryUsage', data)

  def test_cpu_usage(self):
    response = self.client.get('/monitor/cpu')
    self.assertEqual(response.status_code, 200)

  def test_memory_usage(self):
    response = self.client.get('/monitor/memory')
    self.assertEqual(response.status_code, 200)

  def test_disk_usage(self):
    response = self.client.get('/monitor/disk')
    self.assertEqual(response.status_code, 200)

  def test_network_usage(self):
    response = self.client.get('/monitor/network')
    self.assertEqual(response.status_code, 200)

  def test_virtual_memory_usage(self):
    response = self.client.get('/monitor/virtual_memory')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()