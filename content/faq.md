---
title: "FAQ"
no_index: true
---

# What was the OCaml Forge?

The OCaml Forge was setup in 2008 by a few administrators to increase the visibility of OCaml projects and provide them
with a common infrastructure (bug trackers, file downloads). At this time, Github was not yet very popular and the
other options didn't offer the type of visibility for OCaml we wanted. It has hosted up to 300 OCaml projects.

# Why shutting down the forge?

The OCaml Forge was using [FusiongForge](https://fusionforge.org/). It was a great platform, but it requires a lot of
maintenance. The OCaml Forge has been the target of constant attacks (esp. SSH attacks and creating 30k fake user
accounts to create link farms) which has increased a lot the required maintenance. 

Given the rise of Github and the lack of time to maintain the OCaml Forge, the main administrator decided to deprecate
the forge in 2017 ([announcement](/deprecation_announcement)). 

# How can I help with the new static website?

The website is hosted on Github and we welcome PR to improve it. See [forge.ocamlcore.org repository].

# Who do I contact with questions and requests?

You can file a bug against on the [forge.ocamlcore.org issue] page.

# Projects

## How to get back project data (forge dump)? {#get_forge_dump}

If you were an admin of the project and want to get the project data dump (forge dump) for a project, open a bug on
the [forge.ocamlcore.org issue] page asking for it. You will need to provide a way to identify you as an admin of the
project and depending on the size of the dump, we will need either your email or a GMail address to share a file in
Google Drive. We will only transfer the dump to a single person, in order to avoid having the same project duplicated. 
We also kindly ask the recipient to update the project page with the new host (see [here](#update_project_page)).

If you were not an admin, we will still need one of the former admin to confirm that it is acceptable to transfer
the project. The former admin will have to give his agreement on the bug. 

The identification is not yet a solved issue. We will accept Github profile that are matching former admin name or 
email, if the profile has been created prior 2020-09-01. If you don't have a Github profile, explain how to check your
identity in the bug. 

Only public projects are available. If the project were not public on the OCaml Forge, we have no forge dump for it.

## How to update a project page? {#update_project_page}

On the project page, you can update the description and add `new_website` field. The `new_website` field will display
a specific message at the beginning of the page (auto-generated, [example](/projects/oasis)). Send a PR to
[forge.ocamlcore.org repository] where the file content/projects/$project.md has been updated.

A typical project page looks like this:
```
---
title: "abach"
no_index: true
new_website: https://github.com/... # TODO
---

Abach is a scientific computing library supporting research in mathematics

* Admins:
  * [user111](/users/user111)
* Members:
  * [user111](/users/user111)
* Registered: 2008-04-27 07:29:09
* Archived data:
  * 0 open bugs
  * 0 open feature requests
  * 0 mailing list
  * 2 VCS
  * 0 released files
```

## What is contained in a project dump? {#forge_dump}

Here is the typical content of a forge dump:

- $project/frs/$package/$version/$files: all the released files.
- $project/frs.json: JSON file describing all the released files.
- $project/home: project site home directory on the old ssh.ocamlcore.org.
- $project/mailman/$list_name.mbox: mbox for public mailing list.
- $project/mailman/$list_name.members: list of members of the mailing if mbox is present.
- $project/scm/{darcs,svn,git,hg,cvs}root/: existing SCM for the project.
- $project/group.json: JSON file describing the project/group.
- $project/artifact.json: JSON file describing the artifacts of the project (bugs, patches).
- $project/news.json: JSON file describing the news of the project.
- $project/mediawiki.sql: SQL dump of Mediawiki (v1.15.5) of the project.

The description of the content of all the JSON files is
[here](https://github.com/ocaml-forge/forge-dump-tools/blob/master/src/lib/forge-dump-tools/forge_dump.atd).

You can use the [forge-dump-tools](https://github.com/ocaml-forge/forge-dump-tools) to read it. 

## What can I do with the project data (forge dump)?

One of the main reason to dump all the projects was the ability to migrate the open bugs and feature requests. This
is actually possible using
[forge-dump-tools](https://github.com/ocaml-forge/forge-dump-tools#forge-dump-migrate-bugs-to-github).

## How do I entirely remove my project from the static website?

If you want to entirely remove the project from the static website, send a PR to [forge.ocamlcore.org repository] where:

- the project page content/projects/$project.md is removed
- the project is removed in every admins/members page (content/users/*.md)

You should also consider removing all the released files of the project from download.ocamlcore.org, see
[here](#remove_frs).  

# Users

## Why all the user names have been dropped?

User names (and email address) are just a way to send you spam. Since I didn't have the user consent to republish their
names on the static website, I decided to remove them and only keep the user id. It is not great in terms of UI, but it
was the safest option for me.  

## How to update a user page? {#users_page}

On the user page, you can update the description to include for example your Github profile. Send a PR to
[forge.ocamlcore.org repository] where the file content/users/$user.md has been updated.

A typical user page looks like this ([example](/users/user102)):
```
---
title: "user102"
no_index: true
---

* Github profile: https://github.com/gildor478
* Projects:
  * [camera-rescue](/projects/camera-rescue/) (admin)
  * [darckup](/projects/darckup/) (admin)
  * [debian-formats](/projects/debian-formats/) (admin)
```

# Mailing lists

## What happened to the mailing lists?

The mailing lists have been shut down. There is no auto-responder in place and sending emails to the old address will
just fail. 

## Can I get back the data of the mailing lists?

The mbox file and the member list for all project mailing lists are present in the project [forge dump](#forge_dump).
Request to get back [the project data](#get_forge_dump) to get the mailing lists as well. 

# Project sites

## What happened to project sites, such as "mascot.forge.ocamlcore.org"?

All project sites page are redirecting by default to the matching project page on `forge.ocamlcore.org`. For example,
`mascot.forge.ocamlcore.org` will redirect to `forge.ocamlcore.org/projects/mascot`. Some sites are redirecting directly
to the new website of the project (see [redirecting](#site_redirect)). Just as before, we don't support SSL for project site.

# How to redirect a project site page to a new host? {#site_redirect}

If you want to redirect $project.forge.ocamlcore.org to a new host, open a bug on the [forge.ocamlcore.org issue] page.

## Can I get back the data that were hosted on website? 

The data in the directory `/home/groups/$project` have been copied to the project [forge dump](#forge_dump). Request
to get back [the project data](#get_forge_dump) to get the project site data as well.

# Released files

## What happened to all the released files?

All the released files have moved to [download.ocamlcore.org](https://download.ocamlcore.org) and the links in
[OPAM](https://github.com/ocaml/opam-repository) have been updated. 

## Some download URLs are now broken! What do I do?

The best way is to fix the old link to point [download.ocamlcore.org](https://download.ocamlcore.org). If this is really
critical, we can set up a redirect, although it is not always possible.

File a bug on the [forge.ocamlcore.org issue] page.

## Can I send a PR to add new files?

No, we only accept PR against [download.ocamlcore.org repository](https://github.com/ocaml-forge/download.ocamlcore.org)
to remove files.

## Can I remove all the released files of my project? {#remove_frs}

Yes. Send PR against [download.ocamlcore.org repository](https://github.com/ocaml-forge/download.ocamlcore.org)
to remove files.

## Can I get back all the released files? 

The released files have been copied to the project [forge dump](#forge_dump). Request to get back
[the project data](#get_forge_dump) to get them as well.

# Source repositories

## What happened to all the VCS data?

The various VCS have been shut down (git, hg, cvs, svn, hg, bzr). It is not possible anymore to access them.

## Can I get back my VCS data?

The VCS data have been copied to the project [forge dump](#forge_dump). Request to get back
[the project data](#get_forge_dump) to get them as well.

# Bug and features trackers

## What happened to all the Bugs and features tracker data?

The bugs, feature requests and patches tracker have been shut down. It is not possible to use them anymore. 

## Can I get back the tracker data?

The tracker artifacts have been copied to the project [forge dump](#forge_dump). Request to get back
[the project data](#get_forge_dump) to get them as well.


<!-- Links -->
[forge.ocamlcore.org repository]: https://github.com/ocaml-forge/forge.ocamlcore.org
[forge.ocamlcore.org issue]: https://github.com/ocaml-forge/forge.ocamlcore.org/issues/new/choose
