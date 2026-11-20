# Test Execution Summary: LearnLoop

| | |
|---|---|
| **Application** | LearnLoop (AI-Powered Learning Management System) |
| **Tested by** | Samata H S, Ujwala K V |
| **Execution period** | 11-11-2026 to 21-11-2026 |
| **Environment** | Windows 11, Chrome, Flask app on localhost:5000 (SQLite, offline AI mode where noted) |

## 1. Manual test results

| Metric | Count |
|---|---|
| Test cases designed | 46 |
| Test cases executed | 46 |
| Passed | 42 |
| Failed | 4 |
| Blocked | 0 |
| Pass rate | 91.3% |

### Results by module

| Module | Cases | Passed | Failed |
|---|---|---|---|
| Authentication | 15 | 13 | 2 |
| Access control | 5 | 5 | 0 |
| Courses | 4 | 4 | 0 |
| Study materials | 3 | 3 | 0 |
| Course management | 2 | 2 | 0 |
| AI notes | 4 | 4 | 0 |
| Quiz | 9 | 7 | 2 |
| Dashboard | 4 | 4 | 0 |
| **Total** | **46** | **42** | **4** |

### Results by technique

Equivalence partitioning, boundary value analysis, decision tables and state transition testing were applied to cases TC01 to TC39. Error guessing was applied to the exploratory cases TC40 to TC46, which found all four defects.

## 2. Defects found

| ID | Title | Severity | Status |
|---|---|---|---|
| DEF-001 | All-space password accepted | Medium | Open |
| DEF-002 | Anyone can register as a teacher | High | Open |
| DEF-003 | Quiz scored against the wrong quiz with two tabs open | High | Open |
| DEF-004 | Invalid level in the URL accepted and saved | Low | Open |

Total: 4 defects (2 High, 1 Medium, 1 Low). Details are in `04_Defect_Reports`.

## 3. Automated test results

| Tool | Tests | Passed | Failed |
|---|---|---|---|
| Pytest | 25 | 25 | 0 |
| Selenium | 2 | 2 | 0 |

Reports: `06_Test_Reports/pytest_report.txt` and `06_Test_Reports/selenium_report.txt`.

The first Selenium run failed because the script read the page before the dashboard had finished loading. This was a fault in the test script (missing explicit wait), not in the application, so no defect was raised. The script was fixed and re-run.

## 4. Observations
- The first 39 designed cases (valid, boundary, decision table and state transition) all passed.
- All defects were found by exploratory testing of unusual input and usage, not by the designed cases.
- The most serious problems are in access control (open teacher registration) and quiz state handling (state stored per browser session).
