---
title: "Deprecating the Forge in 2017"
no_index: true
---

**This news was initially published as `forge.ocamlcore.org/forum/forum.php?forum_id=958` on 2016-12-30, it has been**
__migrated to this static website later.__

The OCaml Forge was launched 9 years ago. Today, the OCaml community will probably benefit to switch to a more popular
hosting option, like Github. Over the course of 2017, the content of the current forge will be transferred to a static
website or given back to its author for a migration to another hosting provider.

# Background

The main reason of the deprecation is that the overall activity on the forge is low and I am mostly managing spammers
on it.

- The number of projects starting on the forge is now close to 0 for the last 6 months.
- The number of users is only growing because of password renewals and spammers.
- The overall activity on the forge is only driven by a couple of people.
- The main traffic on the forge is actually robots and OPAM downloading archives.
- Most of the very active projects have already migrated to Github or are in the process to do so.

# Timeline

The plan is as follow, depending on the time I can spend on this:

**Now: this announcement**

At this point the forge will not accept any new projects.

Goal:
Make the OCaml Forge users aware of the upcoming migration.

**Now to April 2017: cleanup**

Deprecate 2nd level websites and cleanup content of the forge:
- git.ocamlcore.org, scm.ocamlcore.org and all other SCM related websites
- remove empty or default project websites (e.g. siteadmin.forge.ocamlcore.org)
- remove useless mailing list (e.g *-commits mailing with no mailing lists, empty mailing lists)
- remove spammy content (e.g. .html uploaded as bug attachments/patches)

Goal:
Have a clean dataset to give back to author and be ready to migrate a clean forge to a static website.

**March to November 2017: provide archive of project to users**

Generate downloadable archive of projects, including:
- Bugs/Features requests
- Files section
- SCM dump
- Mailing list archive as mbox
- Content of the home directory of the project site
- News

I will drop:
- wiki
- patches or custom trackers
- *-commits mailing lists
- workflow

There is no plan to provide a script to migrate the downloadable archive to a new project on Github, since there are a
lot of possible options for this kind of migration. I will provide a way to read the data in the archive, as an OCaml
library, probably with my own migration scripts for the migration.

I will consider the option to do an HTTP redirect from the forge to the new hosting website, if it makes sense.

Goal:
Allow former OCaml Forge users to migrate their project to a new hosting.

**December 2017: 6. migrate to a static website for the forge.**

Final step of the plan, everything switch to a static website.

Goal:
Finalize the migration to a static host.

# Other options considered

Things I have considered but I won't do:
- Migrate from forge.ocamlcore.org to forge.ocaml.org and give control of the forge to another maintainer(s)

The ideas is to move the burden from me to another set of people. This may work for a time but I think ultimately
Github is a better option. Better take the decision to end it myself.

# Last words

I would like to thank everyone for their support over the years. The OCaml Forge was a great learning experience. At a
personal level, I was a big user and it helped me to better work on some of my projects.

See you all on Github
https://github.com/gildor478