# Test Plan: LearnLoop (AI-Powered Learning Management System)

| | |
|---|---|
| **Document version** | 1.0 |
| **Prepared by** | Samata H S, Ujwala K V |
| **Date** | 15-11-2026 |

## 1. Introduction
LearnLoop is a web-based learning management system. Students enrol in courses, read study materials, generate AI-written notes, take quizzes and view their progress. Teachers create courses, add materials and view student quiz results. This plan describes how the application will be tested.

## 2. Objectives
- Verify that each module works as specified.
- Find defects in validation, access control and data handling.
- Confirm that students and teachers can only perform actions allowed for their role.
- Provide test evidence (cases, results, defects, screenshots, automation reports).

## 3. Scope

### In scope
| # | Module | Main functions tested |
|---|---|---|
| 1 | Authentication | Register, login, logout, role-based access |
| 2 | Course management | Course list, enrolment, teacher creates a course |
| 3 | Study materials | View materials, teacher adds material |
| 4 | AI notes | Notes by topic, level and style |
| 5 | Quiz system | Generate quiz, answer, scoring, saving results |
| 6 | Student dashboard | Enrolled courses, scores, average, recommendation |
| 7 | Teacher dashboard | Course list, enrolment counts, student results |

### Out of scope
- Performance and load testing
- Security penetration testing
- The accuracy and quality of the content written by Gemini
- Availability of the Gemini service

## 4. Test strategy

### Test levels
Functional (system-level) testing of the full application, plus automated unit and integration checks.

### Test design techniques
- Equivalence partitioning
- Boundary value analysis
- Decision table testing
- State transition testing

### Test types
- Functional testing
- Validation and negative testing
- Role-based access testing
- Regression testing, by re-running the Pytest suite

### Tools
| Tool | Purpose |
|---|---|
| Manual execution in browser | Functional test cases |
| Pytest | Automated backend and route tests |
| Selenium | Automated UI test |
| GitHub | Version control and portfolio |

## 5. Test environment
| Item | Details |
|---|---|
| Operating system | Windows 11 |
| Browser | Google Chrome |
| Language and framework | Python 3, Flask |
| Database | SQLite |
| AI service | Gemini API (offline demo mode when no key is set) |
| Test accounts | student@lms.test / Student@123, teacher@lms.test / Teacher@123 |

## 6. Test data
- Valid and invalid emails and passwords, with passwords of 7, 8 and 9 characters
- Topics of different lengths, including empty, long and special-character inputs
- The four seeded courses, and courses created during testing

## 7. Entry and exit criteria
**Entry:** the application starts without errors, the test accounts work, and the test cases are written.

**Exit:** all planned test cases are executed, all high-severity defects are reported, and the execution summary is complete.

## 8. Defect management
Each defect is recorded in `04_Defect_Reports` with an ID, module, steps to reproduce, expected and actual results, severity, priority, status and a screenshot.

| Severity | Meaning |
|---|---|
| High | Feature unusable, or data and security affected |
| Medium | Feature works but gives wrong results |
| Low | Cosmetic or minor issue |

## 9. Roles and responsibilities
| Member | Responsibility |
|---|---|
| Samata H S |  Test plan, test execution, automation |
| Ujwala K V |  Test case design, defect reports, documentation |

## 10. Schedule
| Activity | Planned dates |
|---|---|
| Test plan | 15-11-2026 |
| Test case design | 15-11-2026 |
| Test execution | 16-11-2026 |
| Defect reporting | 17-11-2026 |
| Automation and reports | 18-11-2026 |
| Summary and conclusion | 18-11-2026 |

## 11. Risks and mitigation
| Risk | Mitigation |
|---|---|
| Gemini API is slow or unavailable | Use offline demo mode for functional testing |
| Changing code breaks existing features | Re-run the Pytest suite after every change |
| Little time before the demonstration | Prioritise high-risk modules first: authentication, quiz scoring and role access |
| Two people editing the same files | Each person works on separate folders and pulls before editing |

## 12. Deliverables
Test plan, test cases, execution results, defect reports, automation scripts, test reports with an execution summary, screenshots and `Conclusion.md`.