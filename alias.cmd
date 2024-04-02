@echo off

:: Git Commands
DOSKEY ga=git add
DOSKEY gaa=git add .
DOSKEY gcm=git commit -m
DOSKEY gc=git commit
DOSKEY gs=git status
DOSKEY gb=git branch
DOSKEY gbn=git checkout -b
DOSKEY gck=git checkout
DOSKEY gr=git remote -v

:: -- Log Checking
DOSKEY gl=git log
DOSKEY glo=git log --oneline
DOSKEY glg=git log --graph
DOSKEY gls=git log --stat
DOSKEY glp=git log -p

:: -- Pushing to repository
DOSKEY gps=git push
DOSKEY gpa=git push --all
DOSKEY gpm=git push origin master
DOSKEY gpo=git push origin
DOSKEY gphk=git push heroku
DOSKEY gpgl=git push gitlab
DOSKEY gpgh=git push github
DOSKEY gpbk=git push bitbucket

DOSKEY gpl=git pull

:: -- Adding remote
DOSKEY grahk=git remote add heroku
DOSKEY gragh=git remote add github
DOSKEY gragl=git remote add gitlab
DOSKEY grabk=git remote add bitbucket 


:: Other Commands
DOSKEY clear=cls
DOSKEY ..=cd ..
DOSKEY now=date +%T
DOSKEY liver=live-server
DOSKEY ll=ls -l
DOSKEY la=ls -a
DOSKEY lla=ls -la
DOSKEY open=start
DOSKEY cd~=cd %userprofile%
DOSKEY home=cd %userprofile%
DOSKEY dadb=cd C:\adb
DOSKEY pbs=pocketbase serve 

::DOSKEY npm=pnpm 


:: DOSKEY omp=oh-my-posh 

