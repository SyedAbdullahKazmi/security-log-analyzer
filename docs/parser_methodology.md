
# CSV Parser Implementation Methodology

## 1. Introduction

The CSV parser is responsible for reading security event records from a CSV file and converting them into a common normalized event structure.

This allows the detection engine to process events in a consistent format.

## 2. Input Format

The parser uses CSV (Comma-Separated Values) as its input format.
The dataset also contains testing metadata fields:
case_id, label, expected_rule, and expected_result.

These fields are not part of the normalized security event.
They are loaded separately by the testing metadata module
for future detection evaluation.

The input dataset contains the following fields:

- event_id
- timestamp
- computer
- username
- source_ip
- event_type
- status
- logon_type
- message
- case_id
- label
- expected_rule
- expected_result

## 3. Parsing Process

The parser performs the following operations:

1. Opens the CSV file.
2. Reads and validates the CSV header.
3. Checks required columns.
4. Reads records one by one.
5. Skips completely blank rows.
6. Rejects rows containing extra values.
7. Checks required fields.
8. Validates timestamps.
9. Converts valid records into normalized event dictionaries.
10. Keeps track of accepted and rejected records.

## 4. Error Handling

The parser handles different types of input errors:

- Missing required columns: The file is rejected.
- Missing required fields: The affected row is rejected.
- Invalid timestamps: The affected row is rejected.
- Extra values: The affected row is rejected.
- Blank rows: They are skipped.

Rejected records include the row number and the reason for rejection.

## 5. Normalized Event Structure

Each accepted record is converted into a dictionary containing:

- event_id
- timestamp
- computer
- username
- source_ip
- event_type
- status
- logon_type
- message
- source

The source field identifies the input as CSV.

## 6. Parser Testing

Unit tests are used to verify the parser's behavior.

The tests cover:

- Original dataset parsing
- Invalid timestamps
- Missing required fields
- Extra values in rows
- Missing required columns
- Blank rows

The original test dataset contains 17 records. All 17 records were accepted successfully, with zero rejected records.

All six parser unit tests passed during testing.
