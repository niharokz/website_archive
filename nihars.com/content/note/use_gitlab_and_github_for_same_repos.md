---
title : "Use GitLab and GitHub together for the same repository" 
subtitle : "use gitlab and github together for same repository on one machine" 
date : 2021-02-14
---

This article is about how to sync Gitlab and Github directly from the command line using git pull or push commands. Unlike mirror repositories, these repositories will be independent of each other. We also don't need different remote names for these repositories.

But if you want to keep a mirror copy of Gitlab in Github or vice-versa, this article [Docs Github](https://docs.gitlab.com/ee/user/project/repository/repository_mirroring.html) is for you.

## Adding SSH-keys to your local machine. [optional step]

Generate SSH keys for Gitlab and Github.
	
	ssh-keygen -t rsa -C "some@mail.com" -f ~/.ssh/id_rsa_gitlab 
	ssh-keygen -t rsa -C "some@mail.com" -f ~/.ssh/id_rsa_github

Add public keys to Gitlab and Github.

	Add ~/.ssh/id_rsa_gitlab.pub to GitLab SSH-keys.
	Add ~/.ssh/id_rsa_github.pub to GitHub SSH-keys.

Register the keys in your local machine

	ssh-add ~/.ssh/id_rsa_github
	ssh-add ~/.ssh/id_rsa_gitlab

Edit ~/.ssh/config  with below content


	Host gitlab.com
		HostName gitlab.com
		User git
		IdentityFile ~/.ssh/id_rsa_gitlab
	Host github.com
		HostName github.com
		User git
		IdentityFile ~/.ssh/id_rsa_github


## Configure repositories and remotes

Clone the original repository from Gitlab/Github to your local machine

	git clone git@github.com:username/repository_name.git

Create a remote instance of the same

	cd repository_name
	git remote set-url origin --add git@gitlab.com:username/repository_name.git

To check all the remote for the repository, run the below

	git remote -v

The command should return something like 

	origin	https://github.com/username/repository_name.git (fetch)
	origin	https://github.com/username/repository_name.git (push)
	origin	https://gitlab.com/username/repository_name.git (push)

Now you can just use git push and it will push on all remote.
