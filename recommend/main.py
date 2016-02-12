# -*- coding: utf-8 -*-

import sys,os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

import time
import cmdln

from hacker_news import hrn

class Main(cmdln.Cmdln):
    name = "main"

    @cmdln.option("-v", "--verbose", action="store_true",
                  help="print extra information")
    def do_recommend(self, subcmd, opts, *algorithm):
        """${cmd_name}: asynchronously do recommended algorithms

        ${cmd_usage}
        ${cmd_option_list}
        """
        algorithms =  list(set(algorithm))

        for al in algorithms:
             if al == 'hnr':
                 hrn()




if __name__ == "__main__":
    main = Main()
    sys.exit(main.main())
