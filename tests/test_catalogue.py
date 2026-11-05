import unittest
from catalogue import validate,catalogue,summary


def item(id="one",category="Education",title="Schools"):
    return {"id":id,"title":title,"description":"Sample dataset","category":category,"license":"CC0","url":"https://example.org/data.csv"}


class CatalogueTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate(item())["id"],"one")
    def test_missing_field(self):
        with self.assertRaises(ValueError): validate({"id":"one"})
    def test_bad_url(self):
        with self.assertRaises(ValueError): validate({**item(),"url":"javascript:alert(1)"})
    def test_duplicate_id(self):
        with self.assertRaises(ValueError): catalogue([item(),item()])
    def test_search(self):
        self.assertEqual(len(catalogue([item(),item("two","Health","Clinics")],query="school")),1)
    def test_category(self):
        self.assertEqual(len(catalogue([item(),item("two","Health","Clinics")],category="health")),1)
    def test_license(self):
        self.assertEqual(len(catalogue([item()],license_name="CC0")),1)
    def test_summary(self):
        self.assertEqual(summary([item()])["categories"]["Education"],1)


if __name__=="__main__":
    unittest.main()
