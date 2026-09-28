## Stratofortress

## Who Did What
| Member | GitHub Username | File |
|---|---|---|
| Aung San Thu Rain Tun | BrianHobbies | test_deposit.py, test_withdraw.py, conftest.py |
| May Than Thar Ko | 6805140051-oss | test_shared.py, test_deposit.py, conftest.py |
| Moe Pyae Kyaw | 6805142010-hue | teardown.py |


##Side Note: Initial event logs above the table are removed. This is the Final Version of README.md

## Our Merge Conflict
Activity: "README.md update" by 6805142010-hue
# We encountered Conflict markers at line 25 and 26. 
# We accepted the incoming branch "a4c40e0df70247927ee309e561cb46757c106bec" since the current branch is empty.
# Both branches modified the same section of README.md, Line 25 and 26. Git could detect that the changes overlapped, but it could not determine which version the team intended to keep. Therefore, a team member had to manually choose the correct version and remove the conflict markers.

## Git Contribution Summary
| GitHub Username | Name and ID |                          
|---|---|---|
| 9  6805142010-hue | Moe Pyae Kyaw, 6805142010 |
| 13  AungSanThuRainTun | Aung San Thu Rain Tun, 6805142005 |
| 3  LaSi | May Than Thar Ko, 6805140051 |
| 1  BrianHobbies | Aung San Thu Rain Tun, 6805142005 |

## Reflection Questions
**Why was your push rejected, and how did you fix it?**
The push was rejected because the remote repository had changes that were not in my local branch. I fixed it by git pull to resolve any merge conflicts and get latest changes then pushing again.

**Why could Git not resolve the README conflict automatically?**
Git could not resolve it because both branches modified the same section of `README.md` in different ways. Git could not determine which version was intended, so it required a manual decision.

**What is the difference between committing and pushing?**
**Committing** saves changes to your local Git repository, while **pushing** uploads those committed changes from your local repository to the remote repository that can be accessed by the Collaborators.

**How do fixtures reduce duplicated setup code in tests?**
Fixtures provide reusable setup code that multiple tests can use. This avoids repeating the same initialization code in every test and makes the tests easier to maintain.


