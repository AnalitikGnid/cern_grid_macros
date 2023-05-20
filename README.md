# Macros for CERN Grid
## Description
This repository contains python codes used to manage jobs in AliMonitor, ALICE (CERN)
## Repository Content
This repository contains:
* this __README__ file;
* __kill_all.py__ file, that kills all your masterjobs;
* __kill_ch.py__ file, that kills masterjobs with ___given status___;
* __auto_res.py__ file, that automatically resubmits jobs (master and not) every ___given time___;
* __auto_res_error.py__ file, that automatically resubmits jobs with given error type (master and not) every ___given time___;
* __ran_analysis__ directory, for more details see below;
## Notice
All programms work in __AliPhysics__ environment
## __run_analysis__ 
This files help us carry out our analysis.
We had to run runAnalysis.C (macro) file 3 times with different settings to get data. Furthermore, each time it is necessary to wait for tasks in grid to complete. 
This programm does it by itself.
