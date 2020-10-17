#!/usr/bin/env python3

import glob
import fileinput
import re
import os.path

users_view = set()
project_re = re.compile('.*\(/projects/([^/)]*)/?\).*')
for user_filename in glob.glob('content/users/*.md'):
    user = os.path.splitext(os.path.basename(user_filename))[0]
    with fileinput.input(files=(user_filename)) as f:
            for line in f:
                g = project_re.match(line)
                if g is None:
                    continue
                users_view.add((user, g.group(1)))

projects_view = set()
user_re = re.compile('.*\(/users/([^/)]*)/?\).*')
for project_filename in glob.glob('content/projects/*.md'):
    project = os.path.splitext(os.path.basename(project_filename))[0]
    with fileinput.input(files=(project_filename)) as f:
            for line in f:
                g = user_re.match(line)
                if g is None:
                    continue
                projects_view.add((g.group(1), project))

has_error = False
for (user, project) in users_view.symmetric_difference(projects_view):
    print(("file content/users/%s.md and content/project/%s.md are not consistent" % (user, project)))
    has_error = True

if has_error:
    exit(1)