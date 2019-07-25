# -*- coding: utf-8 -*-

__author__ = 'ddSoul'

import pickle

if __name__ == '__main__':
	judge = raw_input('if the project includes a xcworkspace ? (y/n)')
	HAS_XCWORKSPACE = (judge == 'Y' or judge == 'y')
	
        PROJECT_PATH = raw_input('please enter project path : ').strip()
        PROJECT_NAME = raw_input('please enter project name : ')
        TARGET_NAME = raw_input('pleace enter target name : ')
        TARGET_FOLDERPATH = raw_input('pleace enter target folder path : ').strip()

        user_configuration = {"projectPath":PROJECT_PATH, "projectName":PROJECT_NAME , "targetName":TARGET_NAME , "targetPath":TARGET_FOLDERPATH,"hasWorkspace":HAS_XCWORKSPACE}
        pickle_file = open("user_configuration.pkl","wb")
        pickle.dump(user_configuration,pickle_file)
        pickle_file.close()
