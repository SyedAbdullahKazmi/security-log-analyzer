
import unittest
from pathlib import Path

from src.evaluation.test_metadata import load_test_metadata


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_ROOT / "data" / "test" / "dataset_v1.csv"


class TestMetadataLoader(unittest.TestCase):

    def test_original_dataset_metadata(self):
        records = load_test_metadata(DATASET_PATH)

        self.assertEqual(len(records), 17)

    def test_first_record_metadata(self):
        records = load_test_metadata(DATASET_PATH)

        self.assertEqual(records[0]["case_id"], "N01")
        self.assertEqual(records[0]["label"], "Normal")
        self.assertEqual(records[0]["expected_result"], "No alert")


if __name__ == "__main__":
    unittest.main()
