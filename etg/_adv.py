#---------------------------------------------------------------------------
# Name:        etg/_adv.py
# Author:      Robin Dunn
#
# Created:     22-Mar-2012
# Copyright:   (c) 2012 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools
from etgtools import PyFunctionDef, PyCodeDef, PyPropertyDef

PACKAGE   = "wx" 
MODULE    = "_adv"
NAME      = "_adv"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ ]    
    

# The list of other ETG scripts and back-end generator modules that are
# included as part of this module. These should all be items that are put in
# the wxWidgets "adv" library in a multi-lib build.
INCLUDES = [  
             'aboutdlg',
             
             # TODOs - 
             # These modules are also in the C++ adv lib and so should included be here:
             #
             #'animate',
             #'bannerwindow',
             #'bmpcbox',
             #'calctrl',
             #'commandlinkbutton',
             #'datectrl',
             #'dateevt',
             #'editlbox',
             #'hyperlink',
             #'joystick',
             #'laywin',
             #'notifmsg',
             #'odcombo',
             #'richtooltip',
             #'sashwin',
             #'sound',
             #'splash',
             #'taskbar',
             #'timectrl',
             #'tipdlg',
             #'treelist',
             #'wizard',

             # Except for these, which have, or will have their own extension modules
             #'dataview',
             #'grid',   
             #'propdlg',
             ]


# Separate the list into those that are generated from ETG scripts and the
# rest. These lists can be used from the build scripts to get a list of
# sources and/or additional dependencies when building this extension module.
ETGFILES = ['etg/%s.py' % NAME] + tools.getEtgFiles(INCLUDES)
DEPENDS = tools.getNonEtgFiles(INCLUDES)
OTHERDEPS = [  ]


#---------------------------------------------------------------------------
 
def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    module.check4unittest = False

    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode('#include <wxpy_api.h>')
    module.addImport('_core')
    module.addInclude(INCLUDES)
       

    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    

    
#---------------------------------------------------------------------------

if __name__ == '__main__':
    run()
