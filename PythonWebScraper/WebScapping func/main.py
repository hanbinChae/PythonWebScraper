from indeed import get_jobs as get_indeed_jobs
from StackOverflow import get_jobs as get_so_jobs
from conversionExcel import save_to_file

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = so_jobs + indeed_jobs
save_to_file(jobs)