# -*- coding: utf-8 -*-

__author__ = 'ddSoul'

import os
import time
import pickle

def readConfiguration():	
        global PROJECT_PATH
        global PROJECT_NAME
        global TARGET_NAME
        global TARGET_FOLDERPATH
        global HAS_WORKSPACE

        userConfiguation = open('user_Configuration.pkl','rb')
        userList = pickle.load(userConfiguation)
        print userList

        PROJECT_PATH = userList["projectPath"]
        PROJECT_NAME = userList["projectName"]
        TARGET_NAME = userList["targetName"]
        TARGET_FOLDERPATH = userList["targetPath"]
        HAS_WORKSPACE = userList["hasWorkspace"]

def chooseOption():
        global RELEASE_TYPE

        theType = raw_input('choose build type:\n----------debug ----------> 0\n----------release ----------> 1\n:')

        if theType == '0':
              RELEASE_TYPE = 'Debug'
        elif theType == '1':
              RELEASE_TYPE = 'Release'
        else:
              RELEASE_TYPE = 'Release'

        return waitConfirm()

def waitConfirm():
	isConfirmed = raw_input('you have choose build type : %s , confirm to release?(y/n) : ' %(RELEASE_TYPE))
	if isConfirmed == 'Y' or isConfirmed == 'y':
		return True
	elif isConfirmed == 'N' or isConfirmed == 'n':
		return chooseOption()
	else:
		return waitConfirm()

def createFolder(targetName):	
	d = time.ctime().split(' ')
	curTime = d[3]
	dirStr = '%s/%s%s' %(TARGET_FOLDERPATH,targetName,curTime)
	os.system('mkdir %s' %(dirStr))
	return dirStr

def createTempFolder():
	dirStr = '%s/temp' %(TARGET_FOLDERPATH)
	os.system('mkdir %s' %(dirStr))
	return dirStr

def release():
	cdStr = 'cd %s' %(PROJECT_PATH)
	os.system(cdStr + '\n')

	cleanStr = 'xcodebuild -project "%s/%s.xcodeproj" -target "%s" -configuration "%s" clean' %(PROJECT_PATH,PROJECT_NAME,TARGET_NAME,RELEASE_TYPE)
	os.system(cleanStr)

	tempDirPath = createTempFolder()

	if HAS_WORKSPACE:
		buildStr = 'xcodebuild -workspace %s/%s.xcworkspace -sdk iphoneos  -scheme "%s" -configuration "%s" CONFIGURATION_BUILD_DIR="%s"' %(PROJECT_PATH,PROJECT_NAME,TARGET_NAME,RELEASE_TYPE,tempDirPath)
	else:
		buildStr = 'xcodebuild -project %s/%s.xcodeproj -sdk iphoneos  -scheme "%s" -configuration "%s" CONFIGURATION_BUILD_DIR="%s"' %(PROJECT_PATH,PROJECT_NAME,TARGET_NAME,RELEASE_TYPE,tempDirPath)
        os.system(buildStr)

        folderStr = createFolder(TARGET_NAME)
        releaseStr = 'xcrun -sdk iphoneos packageApplication -v  %s/%s.app -o %s/%s.ipa' %(tempDirPath,TARGET_NAME,folderStr,TARGET_NAME)
        os.system(releaseStr)

        os.system('rm -rf %s' %(tempDirPath))



readConfiguration()
if chooseOption() == True  :
	release()

	
