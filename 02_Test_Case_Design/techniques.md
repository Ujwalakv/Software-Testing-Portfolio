# Test Design Techniques Used

## 1. Equivalence partitioning
Inputs are split into groups that the application should treat the same way.

| Input | Valid partition | Invalid partitions |
|---|---|---|
| Email | name@domain.com | empty; no @; no domain dot; already registered |
| Name | any non-empty text | empty |
| Topic | any non-empty text | empty |
| Quiz answer | one option chosen | none chosen |

## 2. Boundary value analysis
**Password minimum length is 8.** Tested at 7 (invalid), 8 (valid) and 9 (valid). See TC06 to TC08.

**Recommendation threshold is 70%** (the quiz has 5 questions). 3/5 is 60% and gives "Revisit". 4/5 is 80% and gives "Strong results". See TC37 and TC38.

## 3. Decision table: login
| Rule | Email registered? | Password correct? | Result |
|---|---|---|---|
| R1 | Yes | Yes | Dashboard shown (TC09) |
| R2 | Yes | No | Error message (TC10) |
| R3 | No | Yes | Error message (TC11) |
| R4 | No | No | Error message (TC12) |

## 4. Decision table: dashboard recommendation
| Rule | Quizzes taken? | Weakest latest score at least 70%? | Message |
|---|---|---|---|
| R1 | No | n/a | Generate notes and take the quiz (TC36) |
| R2 | Yes | No | Revisit the weakest topic (TC37) |
| R3 | Yes | Yes | Strong results; try a higher level (TC38) |

## 5. State transition: quiz
| Current state | Event | Next state | Test case |
|---|---|---|---|
| No quiz | Open quiz for a topic | Quiz shown | TC29 |
| Quiz shown | Submit answers | Result shown and saved | TC30 to TC33 |
| Quiz shown | Leave without submitting | Quiz abandoned; nothing saved | TC35 |
| Result shown | Resubmit | Redirected to AI notes; no duplicate | TC34 |

## 6. State transition: session and enrolment
| Current state | Event | Next state | Test case |
|---|---|---|---|
| Logged out | Log in with valid details | Logged in | TC09 |
| Logged in | Log out | Logged out; protected pages blocked | TC15 |
| Not enrolled | Enrol | Enrolled | TC19 |