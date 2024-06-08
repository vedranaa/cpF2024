```python
from unitgrade import Report, UTestCase, hide
from unittest.mock import patch
import cp
import numpy as np
from io import StringIO
import os

class Task01_DistanceTraveled(UTestCase):
    def test_distance_traveled_0(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(5.5), 148.37625, places = 4)

    def test_distance_traveled_1(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(12.8), 803.6352, places = 4)

    def test_distance_traveled_2(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(0.7), 2.40345, places = 4)

    def test_distance_traveled_3(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(4.2), 86.5242, places = 4)

    def test_distance_traveled_4(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(0.0), 0.0, places = 4)
    
    def test_distance_traveled_5(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(3.9), 74.60505, places = 4)
    
    def test_distance_traveled_6(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(1348.0), 8912895.12, places = 4)
    
    def test_distance_traveled_7(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(0.01), 0.0004905, places = 4)
    
    def test_distance_traveled_8(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(5.002), 122.72311962, places = 4)
    
    def test_distance_traveled_9(self):
        from cp.reexam2024may.tasks.distance_traveled import distance_traveled
        self.assertAlmostEqual(distance_traveled(1.778), 15.50609802, places = 4)


class Task02_BookletLayout(UTestCase):
    def test_booklet_layout_0(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(17), (20, 3)) 

    def test_booklet_layout_1(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(25), (28, 3)) 

    def test_booklet_layout_2(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(31), (32, 1)) 

    def test_booklet_layout_3(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(28), (28, 0)) 

    def test_booklet_layout_4(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(6), (8, 2)) 
    
    def test_booklet_layout_5(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(1), (4, 3)) 
    
    def test_booklet_layout_6(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(11), (12, 1)) 
    
    def test_booklet_layout_7(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(118), (120, 2)) 
    
    def test_booklet_layout_8(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(72), (72, 0)) 
    
    def test_booklet_layout_9(self):
        from cp.reexam2024may.tasks.booklet_layout import booklet_layout
        self.assertEqual(booklet_layout(64), (64, 0)) 

class Task03_ReversedText(UTestCase):
    def test_reversed_text_0(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Hello world we are going to do some programming'
        reversed = 'olleH dlrow ew era gniog ot od emos gnimmargorp'
        self.assertEqual(reversed_text(text, "letters"), reversed) 

    def test_reversed_text_1(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Hello world we are going to do some programming'
        reversed = 'programming some do to going are we world Hello'
        self.assertEqual(reversed_text(text, "words"), reversed) 

    def test_reversed_text_2(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'This is a sentence with words separated by spaces'
        reversed = 'sihT si a ecnetnes htiw sdrow detarapes yb secaps'
        self.assertEqual(reversed_text(text, "letters"), reversed) 

    def test_reversed_text_3(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'This is a sentence with words separated by spaces'
        reversed = 'spaces by separated words with sentence a is This'
        self.assertEqual(reversed_text(text, "words"), reversed) 

    def test_reversed_text_4(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Det er ikke vigtigt om det er Dansk eller Engelsk'
        reversed = 'teD re ekki tgitgiv mo ted re ksnaD relle kslegnE'
        self.assertEqual(reversed_text(text, "letters"), reversed) 
    
    def test_reversed_text_5(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Det er ikke vigtigt om det er Dansk eller Engelsk'
        reversed = 'Engelsk eller Dansk er det om vigtigt ikke er Det'
        self.assertEqual(reversed_text(text, "words"), reversed) 
    
    def test_reversed_text_6(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Yet another sentence to be reversed in two different ways'
        reversed = 'teY rehtona ecnetnes ot eb desrever ni owt tnereffid syaw'
        self.assertEqual(reversed_text(text, "letters"), reversed) 
    
    def test_reversed_text_7(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Yet another sentence to be reversed in two different ways'
        reversed = 'ways different two in reversed be to sentence another Yet'
        self.assertEqual(reversed_text(text, "words"), reversed) 
    
    def test_reversed_text_8(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Nip sip sup i mekke tekke tup'
        reversed = 'piN pis pus i ekkem ekket put'
        self.assertEqual(reversed_text(text, "letters"), reversed) 
    
    def test_reversed_text_9(self):
        from cp.reexam2024may.tasks.reversed_text import reversed_text
        text = 'Nip sip sup i mekke tekke tup'
        reversed = 'tup tekke mekke i sup sip Nip'
        self.assertEqual(reversed_text(text, "words"), reversed) 

class Task04_FirstDoublePeak (UTestCase):
    def test_first_double_peak_0(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [1.2, 2.4, 3.1, 2.9, 3.6, 2.3, 1.9, 2.4]
        self.assertEqual(first_double_peak(sequence), 4)

    def test_first_double_peak_1(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [14.89, 5.44, 9.76, 9.76, 13.61, 12.41, 16.96, 9.29, 7.61, 9.76]
        self.assertEqual(first_double_peak(sequence), 6)

    def test_first_double_peak_2(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [0.7, 2.8, 1.6, 1.6, 0.9, 1.1, 0.4, 1.7, 2.1, 1.6]
        self.assertEqual(first_double_peak(sequence), -1)

    def test_first_double_peak_3(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [22.4, 0.3, 33.3, 11.2, 21.4, 12.4, 34.1, 22.9, 35.6, 21.3, 11.9, 22.4]
        self.assertEqual(first_double_peak(sequence), 2)

    def test_first_double_peak_4(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [12.03, 0.38, 7.93, 6.91, 11.6, 7.49, 16.83, 12.24, 17.42, 11.55, 7.25, 12.03]
        self.assertEqual(first_double_peak(sequence), 8)
    
    def test_first_double_peak_5(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [14.73, 10.45, 10.55, 13.65, 13.35, 14.63, 13.52, 15.84, 14.79, 15.71, 14.62, 13.45, 14.73]
        self.assertEqual(first_double_peak(sequence), 7)
    
    def test_first_double_peak_6(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [3.93, 3.88, 3.64, 3.71, 4.0, 5.0, 3.93, 5.88, 3.64, 5.91, 3.58, 6.63, 3.58, 6.64, 3.72, 3.64, 3.64, 4.15, 4.11, 3.7, 3.73, 3.64, 3.71, 3.58, 3.63, 3.58, 3.64, 3.72, 3.64]
        self.assertEqual(first_double_peak(sequence), 13)
    
    def test_first_double_peak_7(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [12.03]
        self.assertEqual(first_double_peak(sequence), -1)
    
    def test_first_double_peak_8(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [9.0, 10.0, 8.59, 8.27, 5.37, 6.48, 4.16, 5.21, 4.29, 5.38, 6.55, 5.27, 5.27, 9.55, 9.45, 6.35, 6.65, 5.37, 6.48, 4.16, 5.21, 4.29, 5.38, 6.55, 5.27]
        self.assertEqual(first_double_peak(sequence), 10)
    
    def test_first_double_peak_9(self):
        from cp.reexam2024may.tasks.first_double_peak import first_double_peak
        sequence = [3.93, 3.88, 3.64, 3.71, 4.0, 5.0, 3.93, 3.88, 3.64, 3.71, 3.58, 3.63, 3.58, 3.64, 3.72, 3.64, 3.64, 4.15, 4.11, 3.7, 3.73, 3.64, 3.71, 3.58, 3.63, 3.58, 3.64, 3.72, 3.64]
        self.assertEqual(first_double_peak(sequence), 5)

class Task05_RobustValues(UTestCase):
    def assertArrayEqual(self, a, b):
        self.assertIsNotNone(a)
        self.assertIsNone(np.testing.assert_array_equal(a, b))

    def test_robust_values_0(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([41.42, 44.32, 45.56, 63.01, 12.22, 42.82, 43.73, 40.11])
        correct = np.array([41.42, 44.32, 45.56, 42.82, 43.73, 40.11])
        self.assertArrayEqual(robust_values(x), correct)

    def test_robust_values_1(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([61.42, 64.32, 65.56, 83.01, 32.22, 62.82, 63.73, 60.11, 31.42, 34.32, 35.56, 53.01, 2.22, 32.82, 33.73, 30.11])
        correct = np.array([61.42, 64.32, 65.56, 32.22, 62.82, 63.73, 60.11, 31.42, 34.32, 35.56, 53.01, 32.82, 33.73, 30.11])
        self.assertArrayEqual(robust_values(x), correct)

    def test_robust_values_2(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([61.42, 64.32, 65.56, 83.01, 62.82, 63.73, 60.11, 53.01])
        correct = np.array([61.42, 64.32, 65.56, 62.82, 63.73, 60.11])
        self.assertArrayEqual(robust_values(x), correct)

    def test_robust_values_3(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([12.4, 12.4, 12.4, 12.4, 12.4, 12.4, 12.4, 12.4])
        correct = np.array([12.4, 12.4, 12.4, 12.4, 12.4, 12.4, 12.4, 12.4])
        #self.assertArrayEqual(robust_values(x), correct)

    def test_robust_values_4(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([1715.62, 1964.26, 987.22, 1177.86, 1264.51, 2810.06, 4.93, 1077.15, 1137.71, 906.61])
        correct = np.array([1715.62, 1964.26, 987.22, 1177.86, 1264.51, 1077.15, 1137.71, 906.61])
        self.assertArrayEqual(robust_values(x), correct)
    
    def test_robust_values_5(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([5.3, 5.3, 5.3, 5.3, 1.8, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 1.8, 5.3, 5.3, 5.3])
        correct = np.array([5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3])
        self.assertArrayEqual(robust_values(x), correct)
    
    def test_robust_values_6(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([87.23, 94.61, 97.79, 144.31, 20.16, 90.78, 93.1, 83.93, 46.42, 49.32, 50.56, 68.01, 17.22, 47.82, 48.73, 45.11])
        correct = np.array([87.23, 94.61, 97.79, 90.78, 93.1, 83.93, 46.42, 49.32, 50.56, 68.01, 47.82, 48.73, 45.11])
        self.assertArrayEqual(robust_values(x), correct)
    
    def test_robust_values_7(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([49.7, 53.18, 54.67, 75.61, 14.66, 51.38, 38.42, 41.32, 42.56, 60.01, 9.22, 39.82])
        correct = np.array([49.7, 53.18, 54.67, 51.38, 38.42, 41.32, 42.56, 60.01, 39.82])
        self.assertArrayEqual(robust_values(x), correct)
    
    def test_robust_values_8(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([-37.7, -41.18, -42.67, -63.61, -2.66, -39.38, -48.11, -52.75, -54.75, -83.36, -3.7, -50.35])
        correct = np.array([-37.7, -41.18, -42.67, -63.61, -39.38, -48.11, -52.75, -54.75, -50.35])        
        self.assertArrayEqual(robust_values(x), correct)
    
    def test_robust_values_9(self):
        from cp.reexam2024may.tasks.robust_values import robust_values
        x = np.array([1000, 1100])
        correct = np.array([1000, 1100])       
        self.assertArrayEqual(robust_values(x), correct)


class Task06_PopulationConvergence(UTestCase):
    def test_population_convergence_0(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(4.8, 0.65), 6)

    def test_population_convergence_1(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(11.4, 0.45), 5)

    def test_population_convergence_2(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(14.4, 0.5), 5)

    def test_population_convergence_3(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(3.4, 0.2), 25)

    def test_population_convergence_4(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(0.4, 0.8), 9)
    
    def test_population_convergence_5(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(10.4, 0.1), 13)
    
    def test_population_convergence_6(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(18.4, 0.05), 75)
    
    def test_population_convergence_7(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(8.4, 0.05), 58)
    
    def test_population_convergence_8(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(7.2, 0.01), 364)
    
    def test_population_convergence_9(self):
        from cp.reexam2024may.tasks.population_convergence import population_convergence
        self.assertEqual(population_convergence(17.2, 0.01), 373)

class Task07_EventManager(UTestCase): 
    def str_cmp(self, mock_stdout, expected):
        out = mock_stdout.getvalue().strip()
        if out.endswith('.'):
            out = out[:-1]
        self.assertEqual(out, expected)

    def check_register(self, my_event, user, expected_count, expected_message=""):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_event.register(user)
            self.str_cmp(mock_stdout, expected_message)
            self.assertEqual(my_event.get_num_registrations(), expected_count)

    def check_deregister(self, my_event, user, expected_count, expected_message=""):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_event.deregister(user)
            self.str_cmp(mock_stdout, expected_message)
            self.assertEqual(my_event.get_num_registrations(), expected_count)

    def test_event_manager_0(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_deregister(my_event, 'Mike', 0, 'Deregistration failed: User not registered')
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Mike', 1, 'Registration failed: User already registered')
        self.check_register(my_event, 'John', 2)
        self.check_deregister(my_event, 'Mike', 1)

    def test_event_manager_1(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.assertEqual(my_event.get_num_registrations(), 0)

    def test_event_manager_2(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_register(my_event, 'Bjarke', 1)
        self.check_register(my_event, 'Bjarke', 1, 'Registration failed: User already registered')
        self.check_deregister(my_event, 'Bjarke', 0)

    def test_event_manager_3(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_deregister(my_event, 'Lars', 0,  'Deregistration failed: User not registered')
        
    def test_event_manager_4(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Emily', 2, 'Registration failed: User already registered')
        self.check_register(my_event, 'Sara', 3)
        self.check_register(my_event, 'Peter', 4)
        self.check_register(my_event, 'John', 5)
        self.check_deregister(my_event, 'Mike', 4)
        self.check_deregister(my_event, 'Mike', 4, 'Deregistration failed: User not registered')
    
    def test_event_manager_5(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Sara', 3)
        self.check_register(my_event, 'Peter', 4)
        self.check_register(my_event, 'John', 5)
        self.check_register(my_event, 'John', 5, 'Registration failed: User already registered')
        self.check_deregister(my_event, 'Mike', 4)
        self.check_deregister(my_event, 'Emily', 3)
        self.check_deregister(my_event, 'Sara', 2)
        self.check_deregister(my_event, 'Peter', 1)
        self.check_deregister(my_event, 'John', 0)
    
    def test_event_manager_6(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_deregister(my_event, 'Lykke', 0,  'Deregistration failed: User not registered')
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Orla', 2)
        self.check_deregister(my_event, 'Mike', 1)
        self.check_register(my_event, 'Mike', 2)
        self.check_register(my_event, 'Lykke', 3)
    
    def test_event_manager_7(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Sara', 3)
        self.check_register(my_event, 'Peter', 4)
        self.check_register(my_event, 'John', 5)
        self.check_deregister(my_event, 'Mike', 4)
        self.check_deregister(my_event, 'Mike', 4, 'Deregistration failed: User not registered')
        self.check_register(my_event, 'Sara', 4, 'Registration failed: User already registered')
        self.check_deregister(my_event, 'Emily', 3)
        self.check_deregister(my_event, 'Sara', 2)
        self.check_deregister(my_event, 'Peter', 1)
        self.check_deregister(my_event, 'John', 0)
    
    def test_event_manager_8(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_register(my_event, 'Diana', 1)
        self.check_register(my_event, 'Eve', 2)
        self.check_register(my_event, 'Frank', 3)
        self.check_deregister(my_event, 'Diana', 2)
        self.check_deregister(my_event, 'Eve', 1)
        self.check_deregister(my_event, 'Frank', 0)
        self.check_deregister(my_event, 'Frank', 0, 'Deregistration failed: User not registered')
    
    def test_event_manager_9(self):
        from cp.reexam2024may.tasks.event_manager import EventManager
        my_event = EventManager()
        self.check_deregister(my_event, 'Ian', 0, 'Deregistration failed: User not registered')
        self.check_register(my_event, 'Ian', 1)
        self.check_register(my_event, 'Jane', 2)
        self.check_deregister(my_event, 'Ian', 1)
        self.check_register(my_event, 'Ian', 2)
        self.check_register(my_event, 'Kim', 3)
        self.check_deregister(my_event, 'Jane', 2)

class Task08_NameFrequency(UTestCase):
    def test_name_frequency_0(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['Liv Ea Jensen', 'Mads Oliver', 'Steve Madsen', 'Anna Simon', 'Simon Gade','Mads Kai Jensen']
        self.assertDictEqual(name_frequency(names), {'Liv': 1, 'Mads': 2, 'Steve': 1, 'Anna': 1, 'Simon': 1})

    def test_name_frequency_1(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['Anne-Marie Sigurdsen', 'Marie-Anne Jones']
        self.assertDictEqual(name_frequency(names), {'Anne-Marie': 1, 'Marie-Anne': 1})

    def test_name_frequency_2(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['Liv Ea Jensen', 'Mads Oliver', 'Steve Madsen', 'Anna Simon', 'Simon Gade','Mads Kai Jensen', 'Liv Anna Jensen', 'Liv Ea Jensen']
        self.assertDictEqual(name_frequency(names), {'Liv': 3, 'Mads': 2, 'Steve': 1, 'Anna': 1, 'Simon': 1})

    def test_name_frequency_3(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = []
        self.assertDictEqual(name_frequency(names), {})

    def test_name_frequency_4(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['Taylor Swift', 'Taylor Lautner']
        self.assertDictEqual(name_frequency(names), {'Taylor': 2})
    
    def test_name_frequency_5(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['Liv Larsen', 'Mads Oliver', 'Long John Silver']
        self.assertDictEqual(name_frequency(names), {'Liv': 1, 'Mads': 1, 'Long': 1})
    
    def test_name_frequency_6(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['John Michael Doe', 'Michael John Smith']
        self.assertDictEqual(name_frequency(names), {'John': 1, 'Michael': 1})
    
    def test_name_frequency_7(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['John Doe', 'John Doe', 'Jane Doe']
        self.assertDictEqual(name_frequency(names), {'John': 2, 'Jane': 1})
    
    def test_name_frequency_8(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['John-Thomas Larsen', 'Brane-Marie Jensen', 'John-Thomas Larsen', 'John-Thomas Larsen']
        self.assertDictEqual(name_frequency(names), {'John-Thomas': 3, 'Brane-Marie': 1})
    
    def test_name_frequency_9(self):
        from cp.reexam2024may.tasks.name_frequency import name_frequency
        names = ['John Paul Jones', 'Paul John Smith', 'John Paul Stevens', 'The Pope']
        self.assertDictEqual(name_frequency(names), {'John': 2, 'Paul': 1, 'The': 1})

class Task09_CountDifferences(UTestCase):
    def test_count_differences_0(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_A1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_A2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 3)

    def test_count_differences_1(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_B1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_B2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 6)

    def test_count_differences_2(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_C1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_C2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), -1)

    def test_count_differences_3(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_D1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_D2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 0)

    def test_count_differences_4(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_E1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_E2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 1)
    
    def test_count_differences_5(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_F1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_F2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 37)
    
    def test_count_differences_6(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_G1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_G2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 69)
    
    def test_count_differences_7(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_H1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_H2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), -1)
    
    def test_count_differences_8(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_I1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_I2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 153)
    
    def test_count_differences_9(self):
        f1 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_J1.txt')
        f2 = os.path.join(os.path.dirname(cp.__file__), 'reexam2024may/tasks/files/results_J2.txt')
        from cp.reexam2024may.tasks.count_differences import count_differences
        self.assertEqual(count_differences(f1, f2), 134)

class Task10_LimitedEventManager(UTestCase):
    def str_cmp(self, mock_stdout, expected):
        out = mock_stdout.getvalue().strip()
        if out.endswith('.'):
            out = out[:-1]
        self.assertEqual(out, expected)

    def check_register(self, my_event, user, expected_count, expected_message=""):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_event.register(user)
            self.str_cmp(mock_stdout, expected_message)
            self.assertEqual(my_event.get_num_registrations(), expected_count)

    def check_deregister(self, my_event, user, expected_count, expected_message=""):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_event.deregister(user)
            self.str_cmp(mock_stdout, expected_message)
            self.assertEqual(my_event.get_num_registrations(), expected_count)

    def test_limited_event_manager_0(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager, EventManager
        self.assertTrue(issubclass(LimitedEventManager, EventManager))
        my_event = LimitedEventManager(3)
        self.assertEqual(my_event.get_num_registrations(), 0)
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Sara', 3)
        self.check_register(my_event, 'Peter', 3, 'Registration failed: Limit reached')

    def test_limited_event_manager_1(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager
        my_event = LimitedEventManager(2)
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Sara', 2, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Mike', 1)
        self.check_register(my_event, 'Peter', 2)
        self.check_register(my_event, 'Mike', 2, 'Registration failed: Limit reached')

    def test_limited_event_manager_2(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager
        my_event = LimitedEventManager(0)
        self.assertEqual(my_event.get_num_registrations(), 0)
        self.check_register(my_event, 'Mike', 0, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Mike', 0, 'Deregistration failed: User not registered')

    def test_limited_event_manager_2(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager
        my_event = LimitedEventManager(2)
        self.check_register(my_event, 'Bjarke', 1)
        self.check_register(my_event, 'Lars', 2)
        self.check_register(my_event, 'Mike', 2, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Bjarke', 1)
        self.check_register(my_event, 'Mike', 2)
        self.check_register(my_event, 'Bjarke', 2, 'Registration failed: Limit reached')

    def test_limited_event_manager_3(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager
        my_event = LimitedEventManager(3)
        self.check_deregister(my_event, 'NonExistentUser', 0, 'Deregistration failed: User not registered')
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Sara', 3)
        self.check_register(my_event, 'Peter', 3, 'Registration failed: Limit reached')

    def test_limited_event_manager_4(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager
        my_event = LimitedEventManager(2)
        self.check_register(my_event, 'Mike', 1)
        self.check_register(my_event, 'Emily', 2)
        self.check_register(my_event, 'Emily', 2, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Mike', 1)
        self.check_register(my_event, 'Sara', 2)
        self.check_register(my_event, 'Peter', 2, 'Registration failed: Limit reached')
        self.check_register(my_event, 'Mike', 2, 'Registration failed: Limit reached')
    
    def test_limited_event_manager_5(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager, EventManager
        self.assertTrue(issubclass(LimitedEventManager, EventManager))
        my_event = LimitedEventManager(5)
        self.assertEqual(my_event.get_num_registrations(), 0)
        self.check_register(my_event, 'Lars', 1)
        self.check_register(my_event, 'Mette', 2)
        self.check_register(my_event, 'Marianne', 3)
        self.check_register(my_event, 'Pernille', 4)
        self.check_register(my_event, 'Niels', 5)
        self.check_register(my_event, 'Klaus', 5, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Lars', 4)
    
    def test_limited_event_manager_6(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager, EventManager
        self.assertTrue(issubclass(LimitedEventManager, EventManager))
        my_event = LimitedEventManager(2)
        self.check_register(my_event, 'Mads', 1)
        self.check_register(my_event, 'Mette', 2)
        self.check_register(my_event, 'Marianne', 2, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Mads', 1)
        self.check_register(my_event, 'Mads', 2)
        self.check_register(my_event, 'Lars', 2, 'Registration failed: Limit reached')
    
    def test_limited_event_manager_7(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager, EventManager
        #self.assertTrue(issubclass(LimitedEventManager, EventManager))
        my_event = LimitedEventManager(100)
        self.assertEqual(my_event.get_num_registrations(), 0)
        self.check_register(my_event, 'Timian', 1)
        self.check_deregister(my_event, 'Timian', 0)
    
    def test_limited_event_manager_8(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager, EventManager
        self.assertTrue(issubclass(LimitedEventManager, EventManager))
        my_event = LimitedEventManager(1)
        self.assertEqual(my_event.get_num_registrations(), 0)
        self.check_register(my_event, 'Brutus', 1)
        self.check_register(my_event, 'Brutus', 1, 'Registration failed: Limit reached')
        self.check_register(my_event, 'Bronkitis', 1, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Brutus', 0)
    
    def test_limited_event_manager_9(self):
        from cp.reexam2024may.tasks.event_manager import LimitedEventManager, EventManager
        self.assertTrue(issubclass(LimitedEventManager, EventManager))
        my_event = LimitedEventManager(2)
        self.assertEqual(my_event.get_num_registrations(), 0)
        self.check_register(my_event, 'Bruno', 1)
        self.check_register(my_event, 'Bruno', 1, 'Registration failed: User already registered')
        self.check_register(my_event, 'Emilie', 2)
        self.check_register(my_event, 'SazaDaSuzzy', 2, 'Registration failed: Limit reached')
        self.check_deregister(my_event, 'Bruno', 1)
        self.check_register(my_event, 'Peter', 2)
        self.check_register(my_event, 'Bruno', 2, 'Registration failed: Limit reached')

questions = [
            (Task01_DistanceTraveled, 10),
            (Task02_BookletLayout, 10),
            (Task03_ReversedText, 10),
            (Task04_FirstDoublePeak , 10),
            (Task05_RobustValues, 10),
            (Task06_PopulationConvergence, 10),
            (Task07_EventManager, 10),
            (Task08_NameFrequency, 10),
            (Task09_CountDifferences, 10),
            (Task10_LimitedEventManager, 10),
            ]

class ReExam2024May(Report):
    title = "Computer Programming Exam Fall 2023"
    pack_imports = [cp]
    individual_imports = []
    questions = questions

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(ReExam2024May())```
