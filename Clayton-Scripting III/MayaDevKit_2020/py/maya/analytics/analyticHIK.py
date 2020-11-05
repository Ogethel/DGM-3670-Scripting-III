from maya.analytics.decorators import makeAnalytic
from maya.analytics.decorators import addMethodDocs
from maya.analytics.decorators import addHelp
from maya.analytics.BaseAnalytic import BaseAnalytic


if False:
    from typing import Dict, List, Tuple, Union, Optional

class analyticHIK(BaseAnalytic):
    """
    Scan all of the HIK connections to see if any recognized patterns
    are found.
    
    FBIK pattern:
        A joint connects to an hikEffector through a message attribute.
        Interesting because it causes the EM to fail.
    """
    
    
    
    def run(self):
        """
        Run the analytics on the current scene.
        :return: JSON with the error message if it failed, else None
        """
        pass
    @staticmethod
    def help():
        """
        Call this method to print the class documentation, including all methods.
        """
        pass
    ANALYTIC_DESCRIPTION_DETAILED = 'Scan all of the HIK connections to see if any recognized patterns\nare found.\n\nFBIK pattern:\n    A joint connects to an hikEffector through a message attribute.\n    Interesting because it causes the EM to fail.'
    
    
    ANALYTIC_DESCRIPTION_SHORT = []
    
    
    ANALYTIC_LABEL = []
    
    
    ANALYTIC_NAME = 'HIK'
    
    
    __fulldocs__ = "Scan all of the HIK connections to see if any recognized patterns\nare found.\n\nFBIK pattern:\n    A joint connects to an hikEffector through a message attribute.\n    Interesting because it causes the EM to fail.\nBase class for output for analytics.\n\nThe default location for the anlaytic output is in a subdirectory\ncalled 'MayaAnalytics' in your temp directory. You can change that\nat any time by calling set_output_directory().\n\nClass static member:\n     ANALYTIC_NAME : Name of the analytic\n\nClass members:\n     directory     : Directory the output will go to\n     is_static     : True means this analytic doesn't require a file to run\n     logger        : Logging object for errors, warnings, and messages\n     plug_namer    : Object creating plug names, possibly anonymous\n     node_namer    : Object creating node names, possibly anonymous\n     csv_output    : Location to store legacy CSV output\n     plug_namer    : Set by option 'anonymous' - if True then make plug names anonymous\n     node_namer    : Set by option 'anonymous' - if True then make node names anonymous\n     __options     : Dictionary of per-analytic options\n\n\tMethods\n\t-------\n\tdebug : Utility to standardize debug messages coming from analytics.\n\n\terror : Utility to standardize errors coming from analytics.\n\n\testablish_baseline : This is run on an empty scene, to give the analytic a chance to\n\t                     establish any baseline data it might need (e.g. the nodes in an\n\t                     empty scene could all be ignored by the analytic)\n\t                     \n\t                     Base implementation does nothing. Derived classes should call\n\t                     their super() method though, in case something does get added.\n\n\thelp : Call this method to print the class documentation, including all methods.\n\n\tjson_file : Although an analytic is free to create any set of output files it\n\t            wishes there will always be one master JSON file containing the\n\n\tlog : Utility to standardize logging messages coming from analytics.\n\n\tmarker_file : Returns the name of the marker file used to indicate that the\n\t              computation of an analytic is in progress. If this file remains\n\t              in a directory after the analytic has run that means it was\n\t              interrupted and the data is not up to date.\n\t              \n\t              This file provides a safety measure against machines going down\n\t              or analytics crashing.\n\n\tname : Get the name of this type of analytic\n\n\toption : :param option: Name of option to check\n\t         :return: the current value of the named option\n\n\toutput_files : This is used to get the list of files the analytic will generate.\n\t               There will always be a JSON file generated which contains at minimum\n\t               the timing information. An analytic should override this method only\n\t               if they are adding more output files (e.g. a .jpg file).\n\t               \n\t               This should only be called after the final directory has been set.\n\n\trun : Run the analytics on the current scene.\n\t      :return: JSON with the error message if it failed, else None\n\n\tset_options : Modify the settings controlling the run operation of the analytic.\n\t              Override this method if your analytic has some different options\n\t              available to it, but be sure to call this parent version after since\n\t              it sets common options.\n\t              \n\t              Note: Options are merged with existing options so make sure they are unique\n\t              :param options: Dictionary of OPTION:OPTION_VALUE to be set\n\n\tset_output_directory : Call this method to set a specific directory as the output location.\n\t                       The special names 'stdout' and 'stderr' are recognized as the\n\t                       output and error streams respectively rather than a directory.\n\n\twarning : Utility to standardize warnings coming from analytics.\n"
    
    
    is_static = False




kAnalyticLabel = []

kAnalyticDescriptionShort = []


