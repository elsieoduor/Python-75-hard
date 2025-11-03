import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from to_do import TodoList

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'to_do.py')))
# from to_do import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        """Create a temporary TodoList file for each test."""
        self.test_file = "test_tasks.json"
        # Make sure no leftover file exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.todo = TodoList(filename=self.test_file)

    def tearDown(self):
        """Clean up the temporary file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_valid_task(self):
        self.todo.add_tasks("Buy milk")
        self.assertEqual(len(self.todo.list_tasks()), 1)
        self.assertEqual(self.todo.list_tasks()[0]["Title"], "Buy milk")

    def test_add_invalid_task(self):
        with self.assertRaises(ValueError):
            self.todo.add_tasks("")  # Empty string

    def test_remove_existing_task(self):
        self.todo.add_tasks("Study Python")
        self.todo.remove_task("Study Python")
        self.assertEqual(len(self.todo.list_tasks()), 0)

    def test_remove_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.todo.remove_task("Not Here")

    def test_mark_task_complete(self):
        self.todo.add_tasks("Run 5km")
        self.todo.mark_complete("Run 5km")
        task = self.todo.list_tasks()[0]
        self.assertTrue(task["Completed"])

    def test_mark_nonexistent_task_complete(self):
        with self.assertRaises(ValueError):
            self.todo.mark_complete("Unknown Task")

    def test_save_and_load_tasks(self):
        self.todo.add_tasks("Read book")
        # Reload from file
        new_todo = TodoList(filename=self.test_file)
        self.assertEqual(len(new_todo.list_tasks()), 1)
        self.assertEqual(new_todo.list_tasks()[0]["Title"], "Read book")

    def test_load_with_corrupted_json(self):
        # Write bad JSON data
        with open(self.test_file, "w") as f:
            f.write("not valid json")

        # Should not crash; should load empty
        new_todo = TodoList(filename=self.test_file)
        self.assertEqual(len(new_todo.list_tasks()), 0)

    def test_clear_all(self):
        self.todo.add_tasks("Clean room")
        self.todo.add_tasks("Do laundry")
        self.todo.clear_tasks()
        self.assertEqual(len(self.todo.list_tasks()), 0)
        # File should exist but be empty
        with open(self.test_file) as f:
            data = json.load(f)
        self.assertEqual(data, [])


if __name__ == "__main__":
    unittest.main()