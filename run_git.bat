@echo off
git status > d:\Final-year-project-main\git_out.txt 2>&1
git log -n 5 --oneline >> d:\Final-year-project-main\git_out.txt 2>&1
git diff --name-status >> d:\Final-year-project-main\git_out.txt 2>&1
echo DONE >> d:\Final-year-project-main\git_out.txt
