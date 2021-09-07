REM pytest -s -v -m "sanity"  --html=./reports/report.html testCases/ --browser chrome
REM pytest -s -v -m "sanity or regression"  --html=./reports/report.html testCases/ --browser chrome
pytest -v -m "sanity and regression"  --html=./reports/report.html testCases/ --browser chrome
REM pytest -s -v -m "regression"  --html=./reports/report.html testCases/ --browser chrome