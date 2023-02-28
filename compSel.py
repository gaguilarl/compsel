#! /usr/bin/env python3

import json
import pysvn
import os

target = "./target"
compselDir = os.getcwd()

class Component:
    def __init__(self, component, compsData):
        self.name = compsData[component]["name"]
        self.branch = compsData[component]["branch"]
        self.path = compsData[component]["path"]
        self.revision = compsData[component]["revision"]

    def __str__(self):
        return f"{self.name}, {self.branch}, {self.path}"
    def getCompTrunkPath(self, cwd):
        return cwd+"/"+self.path
    def getCompBranchUrl(self, url):
        return url+'/'+self.branch+'/'+self.path

class BuildManifesto:
    def __init__(self, manifestoPath):
        with open(manifestoPath, "r") as file:
            data = json.load(file)

        # Get SVN URL to checkout from
        self.svnUrl = data["svn_url"]

        # Load components data
        self.comps = []
        compsData = data["sw_bom"]["components"]["list"]
        for componentEntry in compsData:
            # Get data about component from JSON
            self.comps.append(Component(componentEntry, compsData))

def main():
    updateComps = False
    manifesto = BuildManifesto("buildManifesto.json")

    if(os.path.isdir(target) == False):
        os.makedirs(target)


    svnClient = pysvn.Client()
    print("Checking out {}/trunk at {}".format(manifesto.svnUrl,target))
    svnClient.checkout(manifesto.svnUrl+'/trunk', target)

    if len(os.listdir(target)) == 0:
            updateComps = True

    for comp in manifesto.comps:
        compTrunkPath = comp.getCompTrunkPath(target)
        if(comp.revision == "HEAD"):
            revision = pysvn.Revision(pysvn.opt_revision_kind.head)
        else:
            revision = int(comp.revision)

        compUrl = comp.getCompBranchUrl(manifesto.svnUrl)
        print("Switching component {}, to {}".format(compTrunkPath, compUrl))
        svnClient.switch(path=compTrunkPath,
                         url=compUrl,
                         ignore_ancestry=True,
                         revision=revision)

if __name__ == "__main__":
    main()